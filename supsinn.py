from manimlib.imports import *


class Title(Scene):
    def construct(self):
        txt = TexMobject("\\sup\\{sin(n)\\}=", "?")
        txt.set_height(1.8)

        self.play(Write(txt))
        self.wait()
        self.play(FadeOut(txt))


class Gh(GraphScene, MyScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 40,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": (FRAME_X_RADIUS - 1) * LEFT,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(0, 41),
        "y_labeled_nums": range(-1, 2),
        "x_axis_width": FRAME_WIDTH - 2,
        "y_axis_height": FRAME_HEIGHT - 1,
        "x_axis_label": False
    }

    def construct(self):
        self.setup_axes(animate=True)
        fun_sin = self.get_graph(np.sin, color=self.function_color)
        vert_line = self.get_vertical_line_to_graph(2, fun_sin)
        dot = Dot(vert_line.get_edge_center(UP))
        value = DecimalNumber(np.sin(2), num_decimal_places=3, group_with_commas=False)
        value.next_to(dot.get_center(), UR)
        self.play(ShowCreation(fun_sin))
        self.wait()
        cpt = TextMobject("$sin(n)$这个数列显然是取不到1的")
        cpt.to_edge(DOWN)
        self.play(Write(cpt))
        self.wait(2)
        cpt_ = TextMobject("那么它大能大到多大呢？").to_edge(DOWN)
        self.play(ReplacementTransform(cpt, cpt_))
        self.wait(2)
        self.play(*map(ShowCreation, [vert_line, dot, value]))
        cpt = TextMobject("你可能觉得sin(2)已经足够大了")
        cpt.to_edge(DOWN)
        self.play(ReplacementTransform(cpt_, cpt))
        self.wait(2)
        cpt2 = TextMobject("但我们可以很轻易的找到一个更大的数").to_edge(DOWN)
        self.play(Transform(cpt, cpt2))
        all_to_move = VGroup(self.x_axis, fun_sin)
        self.remove(vert_line, dot, value)
        self.play(all_to_move.shift, 2 * 5 * LEFT, run_time=1)
        vert_line = self.get_vertical_line_to_graph(8, fun_sin)
        dot = Dot(vert_line.get_edge_center(UP))
        value = DecimalNumber(np.sin(8), num_decimal_places=3, group_with_commas=False)
        value.next_to(dot.get_center(), RIGHT)
        self.play(*map(ShowCreation, [vert_line, dot, value]))
        self.wait()
        cpt3 = TextMobject("这样的点似乎可以一直找下去，没有尽头").to_edge(DOWN)
        self.play(Transform(cpt, cpt3))
        self.remove(vert_line, dot, value)
        self.play(all_to_move.shift, 2 * 25 * LEFT, run_time=1)
        vert_line = self.get_vertical_line_to_graph(33, fun_sin)
        dot = Dot(vert_line.get_edge_center(UP))
        value = DecimalNumber(np.sin(33), num_decimal_places=7, group_with_commas=False)
        value.next_to(dot.get_center(), RIGHT)
        self.play(*map(ShowCreation, [vert_line, dot, value]))
        self.wait(2)
        cpt4 = TextMobject("而且这些点的函数值似乎在无限接近1").to_edge(DOWN)
        self.play(Transform(cpt, cpt4))
        self.wait(2)
        cpt5 = TextMobject("事实是否也是如此呢？让我们来证明一下").to_edge(DOWN)
        self.play(Transform(cpt, cpt5))
        self.wait(2)
        self.fade_all_out()
        self.wait()

    def setup_axes(self, animate=False):
        """
        This method sets up the axes of the graph.

        Parameters
        ----------
        animate (bool=False)
            Whether or not to animate the setting up of the Axes.
        """
        # TODO, once eoc is done, refactor this to be less redundant.
        x_num_range = float(self.x_max - self.x_min)
        self.space_unit_to_x = 2
        if self.x_labeled_nums is None:
            self.x_labeled_nums = []
        if self.x_leftmost_tick is None:
            self.x_leftmost_tick = self.x_min
        x_axis = NumberLine(
            x_min=self.x_min,
            x_max=self.x_max,
            unit_size=self.space_unit_to_x,
            tick_frequency=self.x_tick_frequency,
            leftmost_tick=self.x_leftmost_tick,
            numbers_with_elongated_ticks=self.x_labeled_nums,
            color=self.axes_color
        )
        x_axis.shift(self.graph_origin - x_axis.number_to_point(0))
        if len(self.x_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.x_labeled_nums = [x for x in self.x_labeled_nums if x != 0]
            x_axis.add_numbers(*self.x_labeled_nums)
        if self.x_axis_label:
            x_label = TextMobject(self.x_axis_label)
            x_label.next_to(
                x_axis.get_tick_marks(), UP + RIGHT,
                buff=SMALL_BUFF
            )
            x_label.shift_onto_screen()
            x_axis.add(x_label)
            self.x_axis_label_mob = x_label

        y_num_range = float(self.y_max - self.y_min)
        self.space_unit_to_y = self.y_axis_height / y_num_range

        if self.y_labeled_nums is None:
            self.y_labeled_nums = []
        if self.y_bottom_tick is None:
            self.y_bottom_tick = self.y_min
        y_axis = NumberLine(
            x_min=self.y_min,
            x_max=self.y_max,
            unit_size=self.space_unit_to_y,
            tick_frequency=self.y_tick_frequency,
            leftmost_tick=self.y_bottom_tick,
            numbers_with_elongated_ticks=self.y_labeled_nums,
            color=self.axes_color,
            line_to_number_vect=LEFT,
            label_direction=LEFT,
        )
        y_axis.shift(self.graph_origin - y_axis.number_to_point(0))
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))
        if len(self.y_labeled_nums) > 0:
            if self.exclude_zero_label:
                self.y_labeled_nums = [y for y in self.y_labeled_nums if y != 0]
            y_axis.add_numbers(*self.y_labeled_nums)
        if self.y_axis_label:
            y_label = TextMobject(self.y_axis_label)
            y_label.next_to(
                y_axis.get_corner(UP + RIGHT), UP + RIGHT,
                buff=SMALL_BUFF
            )
            y_label.shift_onto_screen()
            y_axis.add(y_label)
            self.y_axis_label_mob = y_label

        if animate:
            self.play(Write(VGroup(x_axis, y_axis)))
        else:
            self.add(x_axis, y_axis)
        self.x_axis, self.y_axis = self.axes = VGroup(x_axis, y_axis)
        self.default_graph_colors = it.cycle(self.default_graph_colors)


class PreProof(MyScene):
    def construct(self):
        #     txt = TexMobject("\\sup\\{\\sin(n)\\}=1").scale(1.5).to_edge(UP)
        #     tex_sin = txt[0][4:10]
        #     self.play(Write(txt))
        #     self.wait()
        #
        #     self.cpt = TextMobject("由上确界的定义，易知我们只需证明", color=BLUE).to_edge(DOWN)
        #     self.play(Write(self.cpt))
        #     self.wait(0.5)
        #     prf = TexMobject("\\forall \\epsilon >0,\\exists N,s.t.|\\sin(N)-1|<\\epsilon").scale(1.8)
        #     self.play(Write(prf))
        #     self.wait(2)
        #
        #     cpt = "从这里出发证明似乎并不容易"
        #     self.add_caption(cpt)
        #     self.wait(1)
        #     cpt = "因此我们把它放在一边，考虑换个思路"
        #     self.add_caption(cpt)
        #     prf.generate_target()
        #     prf.target.set_height(txt.get_height()).next_to(txt, DOWN)
        #     self.play(MoveToTarget(prf))
        #     self.wait(2)
        #
        #     cpt = "我们先单独讨论sin(n)"
        #     self.add_caption(cpt)
        #     self.wait()
        #     start_point = tex_sin.get_center()
        #     tex_sin.generate_target()
        #     tex_sin.target.move_to(ORIGIN).scale(2)
        #     self.play(MoveToTarget(tex_sin))
        #     self.wait(1)
        #
        #     cpt = "我们将n写成$2k\\pi +\\varphi$的形式"
        #     self.add_caption(cpt)
        #     tex_sin2 = TexMobject("sin(", "2k\\pi+", "\\varphi )").move_to(tex_sin.get_center()).scale(2)
        #     self.play(ReplacementTransform(tex_sin, tex_sin2))
        #     self.wait(2)
        #
        #     cpt = "由三角函数的周期性，我们将该式转换为"
        #     self.add_caption(cpt)
        #     self.play(tex_sin2[1].shift, DOWN * 8)
        #     self.play(tex_sin2[2].next_to, tex_sin2[0], RIGHT, buff=0)
        #     self.wait()
        #     res = VGroup(tex_sin2[0], tex_sin2[2])
        #     res.generate_target()
        #     res.target.move_to(start_point).scale(0.65)
        #     self.play(MoveToTarget(res))
        #     self.wait(2)
        #
        #     cpt = "由之前的关系,我们得到$\\varphi$的表达式"
        #     self.add_caption(cpt)
        #     rlt = TexMobject("\\varphi =", "n-2k\\pi ").scale(2)
        #     self.play(ShowCreation(rlt))
        #     self.wait(2)
        #
        #     cpt = "接下来我们便对右式的性质进行探究"
        #     self.add_caption(cpt)
        #     rec = Rectangle(color=RED)
        #     rec.move_to(rlt[1].get_center()).set_height(rlt[1].get_height()).set_width(rlt[1].get_width())
        #     self.play(ShowCreation(rec))
        #     self.wait(2)
        #
        #     self.play(*map(FadeOut, chain([rlt[0]], [prf, rec], [tex_sin2, txt[0][0:4], txt[0][10:]])))
        #     self.play(ApplyMethod(rlt[1].move_to, ORIGIN), FadeOut(self.cpt))
        #     self.wait()

        txt = TexMobject("\\sup\\{\\sin(n)\\}=1").scale(1).to_edge(UP)
        tex_sin = txt[0][4:10]
        self.play(Write(txt))
        self.wait()

        self.add_caption("由上确界的定义，易知我们只需证明")
        prf = TexMobject("\\forall \\varepsilon >0,\\exists N,s.t.", "|\\sin(N)-1|<\\varepsilon").scale(1.6)
        prf[1].set_color(YELLOW)
        self.play(Write(prf))
        self.wait(2)

        self.add_caption("由于三角函数的周期性")
        self.add_caption("我们想办法把这个问题放到$(0,2\\pi)$的区间内考虑")
        self.play(prf.become, prf.copy().scale(1 / 1.6).next_to(txt, DOWN))
        self.wait(2)

        self.add_caption("即找到一个正整数k")
        prf2 = TexMobject("\\exists k\\in \\mathbb{N}\\quad", "s.t.\\;\\varphi=N-2k\\pi\\in", "(0,2\\pi)")
        prf2[2].set_color(BLUE)
        prf2[1][4].set_color(RED)
        self.play(Write(prf2[0]))

        self.add_caption("使N减去$2k\\pi$后落入区间$(0,2\\pi)$内")
        self.play(Write(prf2[1:]))
        self.wait(2)

        self.add_caption("因此，我们的研究情形就变成了")
        prf3 = TexMobject("\\forall \\varepsilon >0,\\exists N,s.t.", "|\\sin(\\varphi)-1|<\\varepsilon")
        prf3[1].set_color(YELLOW)
        prf3[1][5].set_color(RED)
        self.play(ApplyMethod(prf2.next_to, prf3, UP), Transform(prf, prf3))
        sqr = SurroundingRectangle(VGroup(prf, prf2))
        self.play(ShowCreationThenDestruction(sqr), run_time=1.5)
        self.wait(5)
        # prf_ad = TexMobject("\\varphi=N-2k\\pi\\in", "(0,2\\pi)")
        self.play(*map(FadeOut, self.mobjects), run_time=2)


class Proof0(GraphScene, MyScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 2 * PI,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": (FRAME_X_RADIUS - 2.4) * LEFT,
        "function_color": BLUE,
        "axes_color": WHITE,
        "x_labeled_nums": range(0, 9),
        "y_labeled_nums": range(-1, 2),
        "x_axis_width": FRAME_WIDTH - 2.5,
        "y_axis_height": FRAME_HEIGHT - 3,
        "x_axis_label": False
    }

    # def no_use_construct(self):
    #     txt = TexMobject("n-2k\\pi").scale(2)
    #     self.add(txt)
    #     self.wait()
    #     self.cpt = TextMobject("对上式，我们总可以通过调整k的大小", color=BLUE).to_edge(DOWN)
    #     self.play(Write(self.cpt))
    #     cpt = "使上式落入$(0,2\\pi)$范围内"
    #     self.add_caption(cpt)
    #     add_tex = TexMobject("\\in (0, 2\\pi)").scale(2)
    #     add_tex.next_to(txt, RIGHT, buff=0.2)
    #     self.play(FadeIn(add_tex))
    #     self.wait(2)
    #     self.play(FadeOut(VGroup(txt, add_tex)))
    #
    #     cpt = "又注意到，sin(x)=1在这个区间内只有一个解"
    #     self.add_caption(cpt)
    #
    #     def sin_anim(mob):
    #         x = -FRAME_X_RADIUS * 0.8 + FRAME_WIDTH * 0.8 * theta.get_value() / (2 * PI)
    #         y = 2 * np.sin(theta.get_value())
    #         mob.move_to(np.array([x, y, 0]))
    #
    #     theta = ValueTracker(0)
    #     dot = Dot()
    #     dot.add_updater(sin_anim)
    #     path = TracedPath(dot.get_center, stroke_width=5, color=RED)
    #     self.add(dot, path)
    #     self.play(theta.increment_value, 2 * PI, run_time=3)
    #     dot_1 = Dot(np.array([-FRAME_X_RADIUS * 0.8 + FRAME_WIDTH * 0.8 * PI / 2 / (2 * PI), 2, 0]), color=YELLOW)
    #     crd = TexMobject("(\\frac{\\pi}{2},1)").next_to(dot_1, UR)
    #     self.play(ShowCreation(dot_1), Write(crd))
    #     path.clear_updaters()
    #     dot.clear_updaters()
    #     self.wait(2)
    #
    #     cpt = "至此，我们再次回到之前的证明"
    #     self.add_caption(cpt)
    #     prf = TexMobject("&\\forall \\epsilon >0,\\exists N,\\\\", "&s.t.|\\sin(N)-1|<\\epsilon").scale(1.8)
    #     self.play(ReplacementTransform(VGroup(dot, path, dot_1, crd), prf))
    #     self.wait(2)
    #
    #     cpt = "它便可以改写为"
    #     self.add_caption(cpt)
    #     phi = TexMobject('\\varphi').scale(1.8).move_to(prf[1][9].get_center())
    #     self.play(Transform(prf[1][9], phi))
    #     self.wait()
    #     k = TexMobject("k,").scale(1.8).next_to(prf[0], RIGHT)
    #     self.play(FadeInFrom(k, UP))
    #     chg_prf = TexMobject("&s.t.|\\sin(N-2k\\pi)-1|<\\epsilon").scale(1.8).next_to(prf[0], DOWN, aligned_edge=LEFT)
    #     self.play(ReplacementTransform(prf[1], chg_prf))
    #     self.wait(2)
    #
    #     cpt = "又根据sin(x)的连续性，以及之前得到的范围"
    #     self.add_caption(cpt)
    #     prf2 = TexMobject("|(N-2k\\pi)-\\frac{\\pi}{2}|<\\epsilon", color=RED).scale(1.8)
    #     prf2.next_to(chg_prf[0][4], DOWN, aligned_edge=LEFT)
    #     lra = TexMobject("\\Leftrightarrow").scale(1.8).next_to(prf2, LEFT)
    #     self.play(FadeInFrom(prf2, UP))
    #     self.play(ShowCreation(lra))
    #     cpt = "我们就将证明中的sin去掉了，这样会方便很多"
    #     self.add_caption(cpt)
    #     self.wait(2)
    #
    #     self.play(*map(lambda a: FadeOut(a, ORIGIN), self.mobjects), prf2.to_edge, UP)

    def construct(self):
        self.setup_axes(animate=True)
        fun_sin = self.get_graph(np.sin, color=BLUE, x_max=2 * PI)
        self.play(ShowCreation(fun_sin))

        self.add_caption("这是sin(x)在$(0,2\\pi)$上的图像")
        self.add_caption("观察到，函数在这个区间内只有一个点函数值为1")
        vert_line = self.get_vertical_line_to_graph(PI / 2, fun_sin, color=WHITE)
        vdot = Dot(vert_line.get_edge_center(UP), color=YELLOW)
        self.play(ShowCreation(vert_line))
        self.play(GrowFromCenter(vdot))
        label = TexMobject("(\\frac{\\pi}{2},1)").next_to(vdot, UR).scale(0.85)
        self.play(Write(label))
        self.wait()
        self.add_caption("我们要$\\sin(\\varphi)\\to 1$")
        prf1 = TexMobject("\\sin(\\varphi)\\to 1").to_edge(UR, buff=1).shift(LEFT * 1.5)
        prf1[0][4].set_color(RED)
        prf2 = TexMobject("\\Leftrightarrow", "\\varphi\\to \\frac{\\pi}{2}").next_to(prf1, DOWN, aligned_edge=LEFT)
        prf2.shift(LEFT * prf2[0].get_width())
        prf2[0].set_color(BLUE)
        prf2[1][0].set_color(RED)
        self.play(Write(prf1))
        self.wait()
        self.add_caption("也就是让$\\varphi\\to \\frac{\\pi}{2}$")
        self.play(Write(prf2[1]))
        self.play(ShowCreation(prf2[0]))

        self.add_caption("由函数的连续性，这是很显然的，此处给出图像示意")

        fixed_vline = vert_line.copy().set_color(RED)
        theta = ValueTracker(PI / 2)
        vert_line.add_updater(lambda a: a.become(self.get_vertical_line_to_graph(
            theta.get_value(), fun_sin, color=WHITE)))
        hline = Line(vert_line.get_edge_center(UP), self.y_axis.n2p(1))
        self.play(ShowCreation(hline))

        fixed_hline = hline.copy().set_color(RED)
        fixed_xlabel = TexMobject("\\frac{\\pi}{2}", color=RED)
        fixed_ylabel = TexMobject("1", color=RED)

        vdot.add_updater(lambda a: a.move_to(vert_line.get_end()))
        hline.add_updater(lambda a: a.put_start_and_end_on(
            vdot.get_center(), self.y_axis.n2p(np.sin(theta.get_value()))))
        deciaml_y_label = DecimalNumber(1).scale(0.6)
        deciaml_y_label.add_updater(lambda a: a.set_value(np.sin(theta.get_value())))
        deciaml_y_label.add_updater(lambda a: a.next_to(hline.get_edge_center(LEFT), LEFT, buff=0.2))
        decimal_x_label = DecimalNumber(PI / 2).scale(0.6)
        decimal_x_label.add_updater(lambda a: a.set_value(theta.get_value()))
        decimal_x_label.add_updater(lambda a: a.next_to(vert_line.get_start(), DOWN, buff=0.2))
        x_label = TexMobject("\\varphi=", color=RED).scale(0.6).add_updater(lambda a: a.next_to(decimal_x_label, LEFT))
        y_label = TexMobject("\\sin(\\varphi)=", color=BLUE).scale(0.6).add_updater(
            lambda a: a.next_to(deciaml_y_label, LEFT))
        self.play(*map(ShowCreation, VGroup(x_label, y_label, decimal_x_label, deciaml_y_label)))
        fixed_xlabel.move_to(decimal_x_label.get_center())
        fixed_ylabel.move_to(deciaml_y_label.get_center())
        self.play(theta.increment_value, -PI / 2 + 0.01, run_time=3)
        self.play(*map(ShowCreation, VGroup(fixed_xlabel, fixed_ylabel, fixed_hline, fixed_vline)))
        self.play(theta.increment_value, PI - 0.01, run_time=6)
        self.play(*map(FadeOut, self.mobjects))


class Proof1(MyScene):
    def construct(self):
        prfpp = TexMobject("|\\sin(\\varphi)-1|<\\varepsilon", color=BLUE).to_edge(UP)
        prfp = TexMobject("|\\varphi-\\frac{\\pi}{2}|<\\varepsilon", color=BLUE).to_edge(UP)
        prf = TexMobject("|(N-2k\\pi)-\\frac{\\pi}{2}|<\\varepsilon", color=BLUE).to_edge(UP)
        self.play(ShowCreation(prfpp))
        self.wait(2)
        self.add_caption("从这里出发，根据刚才得到的推论")
        self.add_caption("我们要证明的结论就变成了")
        self.play(ReplacementTransform(prfpp, prfp))
        self.add_caption("又根据先前得到的$\\varphi$的表达式得到")
        self.play(ReplacementTransform(prfp, prf))
        self.wait(2)
        self.add_caption("当$\\varepsilon$充分小时，一定会有整数部分相等，即：")
        prf2 = TexMobject("[N-2k\\pi]=[\\frac{\\pi}{2}]", "=1").next_to(prf, DOWN)
        prf2[1].set_color(YELLOW)
        self.play(Write(prf2[0]))
        self.play(Write(prf2[1]))
        self.add_caption("由于N是整数，只需取$N=[2k\\pi]+2$即可", wait_time=2)
        prff = TexMobject("&[N-2k\\pi]\\\\", "=&\\;[[2k\\pi]+2-2k\\pi]\\\\", "=&\\;[2-\\{2k\\pi\\}]\\\\", "=&\\;1"
                          ).next_to(prf2, DOWN, buff=LARGE_BUFF)
        self.play(ReplacementTransform(prf2[:7].copy(), prff[0]))
        self.wait()
        for i in range(1, len(prff)):
            self.play(Write(prff[i]))
            self.wait()
        sqr = SurroundingRectangle(prff, color=YELLOW)
        self.play(ShowCreation(sqr))
        self.play(FadeOut(prff), FadeOut(sqr))
        self.add_caption("这样我们就得到了N与k的关系")
        prf3 = TexMobject("N=[2k\\pi]+2", color=RED).next_to(prf2, DOWN)
        self.play(FadeInFrom(prf3, UP))
        self.wait()

        self.add_caption("将此关系带入最初的式子，化简得到")
        self.play(prf.to_edge, UP, FadeOut(VGroup(prf3, prf2)))
        prf4 = TexMobject("|([2k\\pi]+2-2k\\pi)-\\frac{\\pi}{2}|<\\varepsilon").next_to(prf, DOWN)
        self.play(FadeInFrom(prf4, UP))
        self.wait(2)
        prf5 = TexMobject("|-\\{2k\\pi\\}+2-\\frac{\\pi}{2}|<\\varepsilon").next_to(prf4, DOWN)
        self.play(FadeInFrom(prf5, UP))
        self.add_caption("这是一个只与k有关的式子")
        self.add_caption("我们将$2\\pi$看作一个整体，记为$\\alpha$")
        srect1 = SurroundingRectangle(prf5[0][3:6], color=RED)
        self.play(ShowCreation(srect1))
        lalpha = TexMobject("k\\alpha", color=RED).next_to(srect1, DOWN)
        lalpha[0][0].set_color(WHITE)
        self.play(FadeInFrom(lalpha, UP))
        self.add_caption("将$2-\\frac{\\pi}{2}$看作一个整体，记为$\\beta$")
        srect2 = SurroundingRectangle(prf5[0][8:12], color=BLUE)
        srect2.stretch(factor=1.45, dim=1, about_edge=UP)
        self.play(ShowCreation(srect2))
        lbeta = TexMobject("\\beta", color=BLUE).next_to(srect2, DOWN)
        self.play(FadeInFrom(lbeta, UP))

        self.add_caption("这个式子就被化简为")
        prff = TexMobject("|\\{k\\alpha\\} -\\beta|<\\varepsilon").scale(2)
        prff[0][3].set_color(RED)
        prff[0][6].set_color(BLUE)
        self.play(ReplacementTransform(VGroup(prf, prf4, prf5, srect1, srect2, lalpha, lbeta), prff))

        self.add_caption("事实上我们可以将这个问题推广")
        self.add_caption("$\\forall \\alpha\\in$ 无理数，$\\beta \\in (0,1)$都是成立的")

        self.add_caption("接下来我们就来证明这个问题")
        self.fade_all_out()
        self.wait()


class Proof2(MyScene):
    def construct(self):
        def generate_number_line(frequency):
            axs = NumberLine(x_min=0,
                             x_max=1,
                             unit_size=0.8 * FRAME_WIDTH,
                             tick_frequency=1 / frequency,
                             number_at_center=0.5,
                             include_numbers=True,
                             numbers_to_show=[0, 1],
                             include_tip=True).shift(DOWN * 1.5)
            number_group = VGroup()
            for i in range(1, frequency):
                num = TexMobject("%d/%d" % (i, frequency)).scale(0.75)
                num.next_to(axs.n2p(i / frequency),
                            direction=DOWN,
                            buff=MED_SMALL_BUFF)
                number_group.add(num)
            number_group.add(axs)
            return number_group

        def add_dot(axs, num, color=BLUE):
            dot = Dot(axs.n2p(num), color=color)
            return dot

        self.add_caption("由于$\\{k\\alpha\\}$与$\\beta$都是(0,1)之间的数")
        self.add_caption("因此我们构造一个(0,1)的数轴")
        axiss = generate_number_line(5)
        axis = axiss[-1]
        nums = axiss[:-1]
        self.play(ShowCreation(axis))
        self.wait()

        self.add_caption("将其均分为n等份(此处以n=5为例)")
        self.play(FadeInFromDown(nums))
        self.wait()

        self.add_caption("在中间任取一个$\\beta$")
        aim_dot = add_dot(axis, 0.88, color=RED)
        beta_label = TexMobject("\\beta", color=RED).next_to(aim_dot, DOWN)
        self.play(GrowFromCenter(aim_dot))
        self.wait(0.5)
        self.play(FadeInFrom(beta_label, UP))
        self.wait()

        self.add_caption("我们的思路是，找到一个$\\{k\\alpha\\}$")
        origin_label = TexMobject("\\{k\\alpha\\}",
                                  "\\in (\\frac{i-1}{n}, \\frac{i}{n})",
                                  "\\, \\text{其中}(\\frac{i-1}{n}<\\beta < \\frac{i}{n})").shift(2 * UP)
        origin_label[1].set_color(BLUE)
        origin_label[2].set_color(GREY)
        self.play(FadeInFrom(origin_label[0], UP))
        self.wait()
        self.add_caption("我们想要让这个数离$\\beta$足够近")
        self.add_caption("也就是让它落在$\\beta$所在的区间内")
        self.play(Write(origin_label[1:]))
        self.wait(2)
        self.add_caption("先尝试取几个点看看能不能做到")

        self.add_caption("接下来我们选取n个$\\{k\\alpha\\}$(此处以$\\alpha=\\pi$为例)", wait_time=3)
        dots_group = VGroup()
        label_group = VGroup()
        aim_label_group = VGroup()
        arrow_group = VGroup()

        for i in range(1, 6):
            dot = add_dot(axis, i * PI - int(i * PI))
            dots_group.add(dot)
            label = TexMobject("\\{%d\\alpha\\}" % i, color=BLUE).shift(2 * UP). \
                shift(RIGHT * (-0.9 * FRAME_X_RADIUS + i / 5 * 0.8 * FRAME_WIDTH))
            label_group.add(label)
            arr = Arrow(start=label.get_edge_center(DOWN),
                        end=dot.get_edge_center(UP) + MED_SMALL_BUFF * UP,
                        color=BLUE)
            arrow_group.add(arr)
            aim_label_group.add(label.copy().next_to(dot, UP))
        self.play(FadeOutAndShift(origin_label, UP),
                  *map(lambda a: ReplacementTransform(origin_label.copy(), a), label_group))
        self.wait(2)
        self.play(ShowCreation(arrow_group), GrowFromCenter(dots_group), run_time=1)
        self.wait(2)
        # TODO: 加个update
        self.play(FadeOut(arrow_group), ReplacementTransform(label_group, aim_label_group))
        self.wait(2)

        self.add_caption("若是此处有点落在$\\beta$所在区间内，证明就结束了", wait_time=2)
        sqr_00 = Rectangle(width=0.22 * 0.8 * FRAME_WIDTH, height=1, color=YELLOW).move_to(axis.n2p(0.9))
        self.play(ShowCreation(sqr_00))
        self.add_caption("但事实上这些点都没落入这个区间")
        sqr0 = SurroundingRectangle(VGroup(dots_group, label_group), color=YELLOW).scale(1.1)
        self.play(ReplacementTransform(sqr_00, sqr0))
        self.wait()
        self.add_caption("再取n个点试试看？")
        self.add_caption("显然这种盲目的取点是说明不了问题的")
        self.add_caption("这个点能不能根据已知点构造出来呢？")
        self.add_caption("我们接下来注意此处")
        sqr = SurroundingRectangle(VGroup(dots_group[0], label_group[0]), color=YELLOW).scale(1.2)
        self.play(ReplacementTransform(sqr0, sqr))
        self.wait()

        self.add_caption("我们找到了一个$\\{k_i\\alpha\\}$落在$(0, \\frac{1}{n})$内", wait_time=2)
        self.add_caption("我们可以通过将它放大适当的倍数，使它落入$\\beta$所在区间")
        prf = TexMobject("\\exists N \\in \\mathbb{N}\\quad",
                         "s.t.\\; N\\{k_i\\alpha\\} \\in (\\frac{i-1}{n}, \\frac{i}{n})",
                         color=BLUE).move_to(TOP + LEFT_SIDE + 0.5 * DR, aligned_edge=UL)
        prf[0].set_color(WHITE)
        self.play(Write(prf))
        self.wait()
        self.add_caption("这样的N显然是存在的，此处仅给图像证明", wait_time=2)
        line_group = VGroup()
        origin_line = Line(axis.n2p(PI - 3), axis.n2p(0), color=YELLOW)
        c_origin_line = origin_line.copy()
        self.play(ShowCreation(origin_line), Uncreate(sqr))
        self.play(c_origin_line.shift, 1.2 * UP)
        for i in range(1, 6):
            line = origin_line.copy().shift(origin_line.get_width() * RIGHT * i)
            line_group.add(line)
            self.play(ReplacementTransform(c_origin_line.copy(), line), run_time=0.3)

        ldot = Dot(axis.n2p(6 * PI - int(6 * PI)), color=YELLOW)
        self.wait()
        self.play(GrowFromCenter(ldot), FadeOutAndShift(line_group, UP), FadeOutAndShift(c_origin_line, UP))

        self.add_caption("又有我们容易证明上述引理(还是证易证者留自证)")
        thm = TexMobject("\\{k_i\\alpha\\}\\pm\\{k_j\\alpha\\}=\\{(k_i\\pm k_j)\\alpha\\}",
                         "(\\text{其中}0<\\{k_i\\alpha\\}\\pm\\{k_j\\alpha\\}<1)", color=RED)
        thm[1].set_color(GREY)
        thm.next_to(prf, DOWN, aligned_edge=LEFT)
        self.play(Write(thm))
        self.wait(2)
        self.add_caption("这个定理说的是")
        self.add_caption("在不进位的情况下，和差的小数部分等于小数部分的和差")

        self.add_caption("因此该式中的N可以移到花括号里")
        prf1 = TexMobject("\\{Nk_i\\alpha\\}\\in (\\frac{i-1}{n}, \\frac{i}{n})", color=BLUE).next_to(
            thm, DOWN, aligned_edge=LEFT)
        self.play(ReplacementTransform(prf.copy(), prf1))
        self.wait()
        self.add_caption("于是就有")
        prf2 = TexMobject("|\\{Nk_i\\alpha\\}-\\beta|<", "\\frac{i}{n}-\\frac{i-1}{n}", color=RED).shift(UP)
        self.play(ReplacementTransform(VGroup(prf, prf1, thm), prf2))
        self.wait()
        prf_t = TexMobject("\\frac{1}{n}", color=YELLOW).next_to(prf2[0], RIGHT, buff=SMALL_BUFF)
        self.play(Transform(prf2[1], prf_t))
        self.wait()
        sqr = SurroundingRectangle(VGroup(prf2[0], prf_t), color=YELLOW)
        self.play(ShowCreationThenDestruction(sqr))
        self.wait()

        self.add_caption("由n的任意性，我们就证明了这个定理")
        self.add_caption("但如果$(0,\\frac{1}{n})$上也没有点呢？")
        self.add_caption("例如以下这种情况")

        self.play(dots_group[0].shift,
                  axis.n2p(0.9) - dots_group[0].get_center(),
                  FadeOutAndShift(origin_line, UP),
                  aim_label_group[0].shift,
                  axis.n2p(0.9) - dots_group[0].get_center(),
                  FadeOut(prf2), FadeOut(ldot), run_time=1)
        self.play(aim_dot.move_to, axis.n2p(0.1),
                  beta_label.shift, axis.n2p(0.1)-aim_dot.get_center(), run_time=1)
        self.wait(2)

        self.add_caption("注意到，此处一共有n个区间n个点")
        self.add_caption("我们只需考虑$\\beta$所在区间没有点的情况")
        self.add_caption("也就是说，剩下n-1个区间内共有n个点")
        self.add_caption("由抽屉原理，一定存在一个区间包含两个点")
        self.add_caption("例如此处", wait_time=1)
        sqr = SurroundingRectangle(VGroup(dots_group[2:4], label_group[2:4]), color=YELLOW)
        self.play(ShowCreation(sqr))
        self.wait(2)
        self.add_caption("将这两个点分别记为$\\{k_i\\alpha\\}$和$\\{k_j\\alpha\\}$")
        j_label = TexMobject("\\{k_j\\alpha\\}", color=YELLOW).move_to(aim_label_group[2].get_center())
        i_label = TexMobject("\\{k_i\\alpha\\}", color=YELLOW).move_to(aim_label_group[3].get_center())
        self.play(ReplacementTransform(aim_label_group[2:4], VGroup(j_label, i_label)))
        self.wait(2)
        self.add_caption("此时有两种情况")
        prf1 = TexMobject("i)", "k_i>k_j\\text{且}\\{k_i\\alpha\\}>\\{k_j\\alpha\\}",
                          color=YELLOW).next_to(ORIGIN + UP, UP)
        prf1[0].set_color(WHITE)
        prf2 = TexMobject("ii)", "k_i>k_j\\text{且}\\{k_i\\alpha\\}<\\{k_j\\alpha\\}",
                          color=YELLOW).next_to(ORIGIN + UP, DOWN)
        prf2[0].set_color(WHITE)
        self.play(Write(VGroup(prf1, prf2)))
        self.wait(2)
        self.add_caption("我们先来讨论第一种情况")
        self.play(prf1.to_edge, UP, FadeOut(prf2))
        self.wait()
        self.add_caption("我们让这两式相减")
        prf3 = TexMobject("&\\{k_i\\alpha\\}-\\{k_j\\alpha\\}", "\\in (0,\\frac{1}{n})\\\\",
                          "=&\\{(k_i-k_j)\\alpha\\}",
                          color=BLUE).next_to(prf1, DOWN)
        prf3[1].set_color(RED)
        self.play(Write(prf3[0]))
        self.wait(2)
        self.add_caption("显然这个结果是在$(0,\\frac{1}{n})$之间的数")
        self.play(Write(prf3[1]))
        self.wait()
        self.add_caption("有根据之前的结论，左式可以转换为")
        self.play(Write(prf3[2]))
        self.wait(2)
        self.add_caption("于是我们就找到了一个位于$(0,\\frac{1}{n})$的$\\{k\\alpha\\}$")
        sqr1 = SurroundingRectangle(prf3[1], color=YELLOW)
        sqr2 = SurroundingRectangle(prf3[2], color=YELLOW)
        self.play(ShowCreationThenDestruction(VGroup(sqr1, sqr2)))
        self.wait()
        self.add_caption("之后就可以套用先前的证明了")

        self.play(FadeOut(prf3))
        self.wait()
        self.add_caption("对于第二种情况")
        distance = dots_group[3].get_center()-dots_group[2].get_center()
        self.play(VGroup(dots_group[2], j_label).shift, distance,
                  VGroup(dots_group[3], i_label).shift, -distance)
        self.wait()
        prf2.to_edge(UP)
        self.play(FadeOutAndShift(prf1, UP), FadeInFrom(prf2, DOWN))
        self.wait()
        prf4 = TexMobject("&\\{k_i\\alpha\\}-\\{k_j\\alpha\\}<0\\\\",
                          "\\neq &\\{(k_i-k_j)\\alpha\\}>0", color=BLUE).next_to(prf2, DOWN)
        prf4[1][0:2].set_color(RED)
        self.add_caption("此时如果按照之前的方法来，会发现")
        self.play(Write(prf4[0]))
        self.play(Write(prf4[1]))
        self.wait(3)
        self.add_caption("两个数字在相减时，小数部分出现了负数")
        sqr = SurroundingRectangle(prf4[0], color=YELLOW)
        self.play(ShowCreation(sqr))
        self.wait(2)
        self.add_caption("而正常情况下，小数部分一定是非负数")
        sqr1 = SurroundingRectangle(prf4[1][1:], color=YELLOW)
        self.play(ReplacementTransform(sqr, sqr1))
        self.wait(2)
        self.add_caption("解决方案也很简单，只需向整数部分借一个1即可")
        self.add_caption("这样我们就有")
        res = TexMobject("&\\{(k_i-k_j)\\alpha\\}\\\\",
                         "= &\\{k_i\\alpha\\}-\\{k_j\\alpha\\}", "+1",
                         "\\in (\\frac{n-1}{n},1)", color=RED).scale(1.2).shift(UP+RIGHT*1.5)
        res[2].set_color(YELLOW)
        res[3].set_color(GREY)
        self.play(ReplacementTransform(VGroup(sqr1, prf4), res[0:2]))
        self.play(ShowCreation(res[2]))
        self.wait(3)
        self.add_caption("这是一个属于$(\\frac{n-1}{n},1)$的数")
        self.play(Write(res[3]))
        self.wait(2)
        self.add_caption("我们同样可以对它的内部乘以N让它落入目标区间")
        spf = TexMobject("&\\{N(k_i-k_j)\\alpha\\}\\\\",
                         "=&N\\{(k_i-k_j)\\alpha\\}-(N-1)\\\\",
                         "=&N(1+\\{k_i\\alpha\\}-\\{k_j\\alpha\\})-(N-1)\\\\",
                         "=&1-Nx(\\text{其中x为}(0,\\frac{1}{n})\\text{中的一个数})"
                         ).scale(0.9).next_to(prf2, DOWN)
        self.play(FadeOut(res), Write(spf[0]))
        self.play(Write(spf[1]))
        self.add_caption("此处进位了N-1次，故减去(N-1)", wait_time=3)
        self.play(Write(spf[2]))
        self.wait(3)
        self.play(Write(spf[3]))
        self.wait(3)

        sqr = SurroundingRectangle(spf[3][3:5], color=YELLOW)
        self.play(ShowCreation(sqr))
        self.add_caption("由于先前结论，Nx可以是$(\\frac{i-1}{n}, \\frac{i}{n})$中的任意的数")
        self.play(Uncreate(sqr))
        self.wait()

        self.add_caption("因此1-Nx也同样如此")
        self.add_caption("这样原式便能够落入$\\beta$所在的区间了")

        self.add_caption("由此，我们讨论完了所有的情况，证明了最终的结论")
        final_prf = TexMobject("|\\{k\\alpha\\}-\\beta|<\\varepsilon").scale(2)
        final_prf[0][3].set_color(RED)
        final_prf[0][6].set_color(BLUE)
        final_prf[0][9].set_color(YELLOW)
        self.play(ReplacementTransform(VGroup(*self.mobjects), final_prf))
        self.wait(3)
        sqr = SurroundingRectangle(final_prf, color=YELLOW)
        self.play(ShowCreation(sqr))
        self.play(FadeOut(VGroup(final_prf, sqr)))
        self.wait(5)





run("-p")
