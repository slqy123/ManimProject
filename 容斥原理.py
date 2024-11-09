from utils.mobjects.BooleanOperationsOnPolygons import *
from manimlib.imports import *


class P01(MyScene):
    def construct(self):
        self.add_caption("我们先来看看什么是容斥原理")
        title = TextMobject("容斥原理", color=YELLOW).to_edge(UP)
        cline = Line(start=LEFT_SIDE, end=RIGHT_SIDE, color=GREY).set_stroke(GREY, opacity=0.3)
        cline.next_to(title, DOWN)
        self.play(AnimationGroup(Write(title), ShowCreation(cline), lag_ratio=0.3))
        self.wait()

        df1 = TextMobject("对n个集合", "$A_1,\\cdots,A_n$", "并集与交集之间有如下关系").scale(0.8)
        df1[1].set_color(BLUE)
        df1.next_to(cline, DOWN).to_edge(LEFT)
        self.play(Write(df1))
        self.wait()

        df2 = TexMobject("\\left|\\bigcup_{i=1}^{n}A_i\\right|",  # 0
                         "=",  # 1
                         "\\sum_{k=1}^{n}",  # 2
                         "(-1)^{k-1}",  # 3
                         "\\sum_{1\\le i_1 < \\cdots < i_k \\le n}",  # 4
                         "|A_{i_1}\\cap \\cdots \\cap A_{i_k}|").scale(0.8)  # 5
        df2.next_to(df1, DOWN, aligned_edge=LEFT)
        self.play(Write(df2), run_time=3)
        self.wait(3)

        self.add_caption("看不懂不要紧，我们以n=3的情况举例说明含义")
        c1 = Circle(radius=2, color=WHITE).shift(LEFT)
        c2 = Circle(radius=2, color=WHITE).shift(RIGHT)
        c3 = Circle(radius=2, color=WHITE).shift(1.5 * UP)
        cgroup = VGroup(c1, c2, c3)
        cgroup.scale(0.75).to_corner(DR, buff=0.8)

        splits = set_split(mobs=cgroup,
                           case=[[1, 0, 0],  # 0
                                 [0, 1, 0],  # 1
                                 [0, 0, 1],  # 2
                                 [1, 1, 0],  # 3
                                 [1, 0, 1],  # 4
                                 [0, 1, 1],  # 5
                                 [1, 1, 1]],  # 6
                           color_list=[RED, GREEN, BLUE, ORANGE, PINK, LIGHT_BROWN, YELLOW])
        self.play(AnimationGroup(*map(ShowCreation, cgroup), lag_ratio=0.15), run_time=0.7)
        self.wait()

        self.add_caption("三个圆相交在一起把整个图形分成了若干块")
        self.add_caption("我们染上颜色以示区别")
        self.play(AnimationGroup(*map(GrowFromCenter, splits), lag_ratio=0.15),
                  FadeOut(cgroup), run_time=1)
        a1 = TexMobject("A_1").next_to(c1, LEFT)
        a2 = TexMobject("A_2").next_to(c2, RIGHT)
        a3 = TexMobject("A_3").next_to(c3, UP)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, UP), [a1, a2, a3]), lag_ratio=0.2))
        self.wait()

        self.add_caption("接下来我们来看等式左边")
        sr = SurroundingRectangle(df2[0], color=YELLOW)
        self.play(ShowCreation(sr))
        self.wait()
        self.add_caption("这是对所有集合求并集，也就是所有小块的面积之和")
        eq1 = self.join(splits, range(len(splits)),
                        TexMobject("+").scale(2)).scale(0.3). \
            next_to(df2, DOWN, aligned_edge=LEFT)
        self.play(ReplacementTransform(splits.copy(), eq1))
        self.wait()

        self.add_caption("再来看右边第一个求和符号")
        sr2 = SurroundingRectangle(df2[2], color=YELLOW)
        self.play(Transform(sr, sr2))
        self.wait()
        self.add_caption("这里的k代表做交集的集合个数")
        self.add_caption("当k=1时，结果就是所有单个集合相加")
        sr2 = SurroundingRectangle(df2[4:], color=YELLOW)
        self.play(Transform(sr, sr2))
        self.wait()
        pre_eq2 = TexMobject("|A_1|", "+|A_2|", "+|A_3|").scale(0.6).next_to(eq1, DOWN, aligned_edge=LEFT)
        equal_sign = TexMobject("=").scale(0.6).next_to(pre_eq2, LEFT)
        self.play(ShowCreation(VGroup(equal_sign, pre_eq2)))
        self.wait()

        self.add_caption("当k=2是就是所有两个集合的交集之和，k=3也同理")
        pre_eq3 = TexMobject("-", "(", "|A_1\\cap A_2|", "+|A_2\\cap A_3|", "+|A_3\\cap A_1|", ")").scale(0.6).next_to(
            pre_eq2, DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(pre_eq3))
        self.wait()
        pre_eq4 = TexMobject("+|A_1\\cap A_2\\cap A_3|").scale(0.6).next_to(pre_eq3, DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(pre_eq4))
        self.wait()

        self.add_caption("注意k=2时结果为负")
        sr2 = SurroundingRectangle(df2[3], color=YELLOW)
        sr3 = SurroundingRectangle(pre_eq3, color=BLUE)
        self.play(AnimationGroup(Transform(sr, sr2), ShowCreationThenDestruction(sr3), lag_ratio=0.5))
        self.wait()

        self.add_caption("我们分别将他们用图形表示出来")
        # 重排正项
        pre_eq2.generate_target().arrange(DOWN, center=False, aligned_edge=LEFT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER).next_to(eq1, DOWN,
                                                                                                aligned_edge=LEFT)
        pre_eq4.generate_target().next_to(pre_eq2.target, DOWN, aligned_edge=LEFT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        pre_eq3.generate_target().next_to(pre_eq2.target, RIGHT, buff=2.1)
        self.play(AnimationGroup(*map(MoveToTarget, [pre_eq2, pre_eq3, pre_eq4]), lag_ratio=0.1))

        # 重排负项
        target_coord = pre_eq3[3].get_center()
        tgt = pre_eq3[2:5].copy().arrange(DOWN, center=False, aligned_edge=RIGHT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER).move_to(target_coord)
        self.play(Transform(pre_eq3[2:5], tgt))
        pre_eq3_left = pre_eq3[0:2].copy().scale(5).next_to(pre_eq3[2:5], LEFT)
        pre_eq3_left[0].scale(0.2).next_to(pre_eq3_left[1], LEFT)
        pre_eq3_right = pre_eq3[5].copy().scale(5).next_to(pre_eq3[2:5], RIGHT)
        self.play(Transform(pre_eq3[0:2], pre_eq3_left), Transform(pre_eq3[5], pre_eq3_right))

        # 替换正项
        eq2_1 = self.join(splits, (0, 3, 4, 6), TexMobject("+").scale(2))
        eq2_2 = self.join(splits, (1, 3, 5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq2_3 = self.join(splits, (2, 4, 5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq4 = self.join(splits, (6,), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq2and4 = VGroup(eq2_1, eq2_2, eq2_3, eq4)
        eq2and4.arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.3).next_to(eq1, DOWN, aligned_edge=LEFT)
        select = lambda a: map(lambda x: splits[x], a)
        self.play(ReplacementTransform(VGroup(*select([0, 3, 4, 6])).copy(), eq2_1), FadeOut(pre_eq2[0]))
        self.play(ReplacementTransform(VGroup(*select([1, 3, 5, 6])).copy(), eq2_2), FadeOut(pre_eq2[1]))
        self.play(ReplacementTransform(VGroup(*select([2, 4, 5, 6])).copy(), eq2_3), FadeOut(pre_eq2[2]))
        self.play(ReplacementTransform(splits[6].copy(), eq4), FadeOut(pre_eq4))

        # 替换负项
        eq3_1 = self.join(splits, (3, 6), TexMobject("+").scale(2))
        eq3_2 = self.join(splits, (5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq3_3 = self.join(splits, (4, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq3 = VGroup(eq3_1, eq3_2, eq3_3).scale(0.3).arrange(DOWN).move_to(target_coord)
        pre_eq3_right.generate_target().next_to(eq3, direction=RIGHT, coor_mask=[1, 0, 1])
        self.play(MoveToTarget(pre_eq3_right))
        self.play(ReplacementTransform(VGroup(*select([3, 6])).copy(), eq3_1), FadeOut(pre_eq3[2]))
        self.play(ReplacementTransform(VGroup(*select([5, 6])).copy(), eq3_2), FadeOut(pre_eq3[3]))
        self.play(ReplacementTransform(VGroup(*select([4, 6])).copy(), eq3_3), FadeOut(pre_eq3[4]))
        self.wait()

        self.add_caption("我们再来看看等式左边")
        # fadeout 无关物件
        fadeout_group = VGroup(title, cline, df1, df2, sr)
        self.play(FadeOutAndShift(fadeout_group, UP), eq1.to_edge, UP)
        self.wait()

        # 加框
        self.add_caption("我们对这里所有的图形分为三类")
        sr1 = SurroundingRectangle(eq1[0:5], color=RED)
        sr2 = SurroundingRectangle(eq1[6:11], color=RED)
        sr3 = SurroundingRectangle(eq1[12], color=RED)
        self.play(ShowCreation(VGroup(sr1, sr2, sr3)))
        self.wait()

        # 显示下标文字
        self.add_caption("记为$I_1,I_2,I_3$")
        i1 = TexMobject("I_1", color=YELLOW).next_to(sr1, DOWN)
        i2 = TexMobject("I_2", color=YELLOW).next_to(sr2, DOWN)
        i3 = TexMobject("I_3", color=YELLOW).next_to(sr3, DOWN)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, DOWN), [i1, i2, i3]), lag_ratio=0.15))
        self.wait()
        self.add_caption("其中$I_i$中的图形仅属于i个集合的相交部分")
        self.add_caption("例如$I_1$中的任何一个图形，都只被唯一的一个集合包含")

        # 加框eq2 I_1
        self.add_caption("分类后我们再来看右边第一项")
        sr_eq2 = SurroundingRectangle(VGroup(eq2_1, eq2_2, eq2_3), color=YELLOW)
        self.play(ShowCreation(sr_eq2))
        self.wait()
        self.add_caption("注意到，$I_1$中的元素全部来自于这一项")
        sr_eq2_1 = SurroundingRectangle(eq2_1[0], color=YELLOW)
        sr_eq2_2 = SurroundingRectangle(eq2_2[1], color=YELLOW)
        sr_eq2_3 = SurroundingRectangle(eq2_3[1], color=YELLOW)
        self.play(ReplacementTransform(sr_eq2, VGroup(sr_eq2_1, sr_eq2_2, sr_eq2_3)))
        self.wait()

        # 移动 I_1
        self.add_caption("这很好地解释了为何他们前面的系数都是1")
        eq2_1[0].generate_target().next_to(eq1[0], DOWN).shift(DOWN * 0.7)
        eq2_2[1].generate_target().next_to(eq1[2], DOWN).shift(DOWN * 0.7)
        eq2_3[1].generate_target().next_to(eq1[4], DOWN).shift(DOWN)
        self.play(Uncreate(VGroup(sr_eq2_1, sr_eq2_2, sr_eq2_3)),
                  AnimationGroup(*map(MoveToTarget, [eq2_1[0], eq2_2[1], eq2_3[1]]), lag_ratio=0.1))
        self.wait()
        self.add_caption("我们把其他项整理一下")
        eq2_1[2].generate_target().next_to(eq1[6], DOWN).shift(DOWN * 0.8)
        eq2_1[4].generate_target().next_to(eq1[8], DOWN).shift(DOWN * 0.7)
        eq2_1[6].generate_target().next_to(eq1[12], DOWN).shift(DOWN * 0.7)
        eq2_2[3].generate_target().next_to(eq2_1[2].target, DOWN)
        eq2_2[5].generate_target().next_to(eq1[10], DOWN).shift(DOWN * 0.7)
        eq2_2[7].generate_target().next_to(eq2_1[6].target, DOWN)
        eq2_3[3].generate_target().next_to(eq2_1[4].target, DOWN)
        eq2_3[5].generate_target().next_to(eq2_2[5].target, DOWN)
        eq2_3[7].generate_target().next_to(eq2_2[7].target, DOWN)

        self.play(AnimationGroup(*map(MoveToTarget,
                                      (eq2_1[2], eq2_1[4], eq2_1[6],
                                       eq2_2[3], eq2_2[5], eq2_2[7],
                                       eq2_3[3], eq2_3[5], eq2_3[7])), lag_ratio=0.05))
        self.wait()

        # 移动第二项
        self.add_caption("接下来看第二项", wait_time=1)
        self.add_caption("处理完第一项后，$I_2$中的剩下的元素就都在第二项里了")
        sr_eq3_1 = SurroundingRectangle(eq3_1[0], color=YELLOW)
        sr_eq3_2 = SurroundingRectangle(eq3_2[1], color=YELLOW)
        sr_eq3_3 = SurroundingRectangle(eq3_3[1], color=YELLOW)
        self.play(ShowCreation(VGroup(sr_eq3_1, sr_eq3_2, sr_eq3_3)))
        self.wait()

        self.add_caption("注意这里是负号，就是为了抵消第一项中$I_2$中的重复元素", anim=(ShowPassingFlash(pre_eq3[0]),))
        eq3_1[0].generate_target().next_to(eq2_2[3], DOWN)
        eq3_2[1].generate_target().next_to(eq2_3[5], DOWN)
        eq3_3[1].generate_target().next_to(eq2_3[3], DOWN)
        self.play(AnimationGroup(*map(
            MoveToTarget, [eq3_1[0], eq3_2[1], eq3_3[1]]
        ), lag_ratio=0.05))
        grp_fo = VGroup(eq3_1[0], eq3_2[1], eq3_3[1],
                        eq2_2[3], eq2_3[5], eq2_3[3])
        sr_offset1 = SurroundingRectangle(grp_fo, color=BLUE)
        self.play(ShowCreation(sr_offset1))
        self.play(FadeOut(VGroup(sr_offset1, grp_fo)))
        self.wait()
        self.add_caption("这样$I_2$中的元素也相等了")

        self.add_caption("接下来是第二部分")
        i3_of_2 = VGroup(eq3_1[2], eq3_2[3], eq3_3[3])
        i3_of_2.generate_target().arrange(DOWN).next_to(eq2_2[7], RIGHT)
        self.play(MoveToTarget(i3_of_2))
        self.wait()
        self.add_caption("同理可以消除")
        fo_g2 = VGroup(i3_of_2, eq2_1[6], eq2_2[7], eq2_3[7])
        sr_offset2 = SurroundingRectangle(fo_g2, color=BLUE)
        self.play(ShowCreation(sr_offset2))
        self.play(FadeOut(VGroup(fo_g2, sr_offset2)))
        self.wait()
        self.add_caption("剩下的就是第三项了")
        eq4[1].generate_target().next_to(eq1[12], DOWN).shift(DOWN * 0.7)
        self.play(MoveToTarget(eq4[1]))

        self.add_caption("至此，左右完全相等，验证完毕")
        self.play(ShowCreationThenDestruction(SurroundingRectangle(VGroup(eq1[0], eq4[1], eq2_1[0]), color=BLUE)))
        self.fade_all_out()
        self.wait(3)

    @staticmethod
    def join(group, idxs, j, left=None, right=None):
        idxs = list(idxs)
        r_group = VGroup()
        if left:
            r_group.add(left)
        r_group.add(group[idxs[0]].copy())
        for i in range(1, len(idxs)):
            r_group.add(j.copy(), group[idxs[i]].copy())
        if right:
            r_group.add(right)
        r_group.arrange()
        return r_group


class P02(MyScene, GraphScene):
    CONFIG = {"axes_color": WHITE}

    def construct(self):
        c1 = Circle(radius=2, color=WHITE).shift(LEFT)
        c2 = Circle(radius=2, color=WHITE).shift(RIGHT)
        c3 = Circle(radius=2, color=WHITE).shift(1.5 * UP)
        cgroup = VGroup(c1, c2, c3)
        splits = set_split(mobs=cgroup,
                           case=[[1, 0, 0],  # 0
                                 [0, 1, 0],  # 1
                                 [0, 0, 1],  # 2
                                 [1, 1, 0],  # 3
                                 [1, 0, 1],  # 4
                                 [0, 1, 1],  # 5
                                 [1, 1, 1]],  # 6
                           color_list=[RED, GREEN, BLUE, ORANGE, PINK, LIGHT_BROWN, YELLOW])
        self.play(AnimationGroup(*map(Write, splits), lag_ratio=0.05), run_time=0.7)
        self.add_caption("我们对之前直观理解的思路，用严谨的语言表述")
        self.add_caption("就得到了证明的思路")
        splits.generate_target().scale(0.8).to_corner(DR)
        cgroup.scale(0.8).to_corner(DR)
        self.play(MoveToTarget(splits))

        self.add_caption("以此处的3个集合为例，他们把平面分割成了这样七个图形")
        self.play(AnimationGroup(*map(
            Indicate, splits
        ), lag_ratio=0.2), run_time=1.4)

        self.add_caption("我们定义一个图形的坐标来唯一地确定一个图形的信息")
        self.add_caption("就如同确定二维平面上一个点的坐标一样")
        self.setup_axes(animate=False)
        self.axes.scale(0.7).move_to(DOWN*0.9+LEFT*2)
        self.play(ShowCreation(self.axes))
        point = Dot(self.coords_to_point(5, 6), color=YELLOW)
        self.play(ShowCreation(point))
        vline = Line(self.coords_to_point(5, 0), point.get_center(), color=BLUE, buff=0.1)
        cline = Line(self.coords_to_point(0, 6), point.get_center(), color=BLUE, buff=0.1)
        self.play(ShowCreation(VGroup(vline, cline)))
        coord = TexMobject("(5, 6)", color=RED).next_to(point, UR)
        self.play(ShowCreation(coord))
        self.wait()
        self.add_caption("这样就将点与坐标一一对应起来了")
        lra = TexMobject("\\Leftrightarrow").next_to(point, RIGHT)
        coord.generate_target().next_to(lra, RIGHT)
        self.play(ShowCreation(lra), MoveToTarget(coord))
        self.play(ShowCreationThenDestruction(
            SurroundingRectangle(VGroup(point, lra, coord), color=YELLOW).scale(1.2)), run_time=0.6)
        self.wait()
        self.play(FadeOut(VGroup(cline, vline, coord, point, self.axes, lra)))
        self.wait()

        self.add_caption("因此我们引入一个三维向量")
        vector_eg = ListTex("1", "0", "0", sep=",\\quad ", brace="()",
                            color_list=[(0, YELLOW), (1, YELLOW), (2, YELLOW)]).scale(2).to_edge(UP)
        self.play(ShowCreation(vector_eg[0::2]))
        self.wait()

        self.add_caption("以图中这个图形为例")
        self.play(Indicate(splits[0], scale_factor=1.25), run_time=1.5)

        self.add_caption("我们先观察集合$A_1$")
        self.play(ShowCreationThenDestruction(c1.copy().set_color(YELLOW).set_stroke(width=5)), run_time=1)
        self.wait()
        self.add_caption("该图形在$A_1$中，因此我们记第一个分量为1")
        self.play(ShowCreation(vector_eg.idx(0)))

        self.add_caption("接着，我们依次验证$A_2$与$A_3$")
        self.play(AnimationGroup(ShowCreationThenDestruction(c2.copy().set_color(YELLOW).set_stroke(width=5)),
                                 ShowCreationThenDestruction(c3.copy().set_color(YELLOW).set_stroke(width=5)),
                                 lag_ratio=0.2),
                  Indicate(splits[0], scale_factor=1.25),
                  run_time=1.5)
        self.add_caption("该图形均不在这两个集合中，因此另外两个分量为0")
        self.play(ShowCreation(vector_eg.idx(1)), ShowCreation(vector_eg.idx(2)))

        self.add_caption("这样我们就用一个三维坐标表示了这个图形")
        coord_txt = TextMobject("Coord=", color=BLUE).scale(2).next_to(vector_eg, LEFT)
        self.play(ShowCreation(coord_txt))
        self.wait()

        self.add_caption("我们定义的坐标和图形的一一对应关系是很显然的")
        equivalence = VGroup(coord_txt, vector_eg, TexMobject("\\Leftrightarrow", color=RED).scale(2), splits[0])
        equivalence.generate_target().arrange(RIGHT)
        splits.save_state()
        self.play(*map(Uncreate, [splits[1:], cgroup, ]), MoveToTarget(equivalence))
        splits.restore()
        splits[0].next_to(equivalence[2], RIGHT)
        self.wait()
        coordix = [[0, 1, 0],
                   [0, 0, 1],
                   [1, 1, 0],
                   [1, 0, 1],
                   [0, 1, 1],
                   [1, 1, 1]]
        for i in range(6):
            animation_list = []
            for j in range(3):
                txt = TexMobject(str(coordix[i][j]), color=YELLOW).scale(2).move_to(vector_eg.idx(j))
                animation_list.append(Transform(vector_eg.idx(j), txt))
            splits[1+i].move_to(splits[0])
            animation_list.append(Transform(splits[0], splits[i + 1]))
            self.play(*animation_list, run_time=0.6)
            self.wait(0.4)
        self.add_caption("所以我们就用此坐标来唯一地代表这些图形")
        equivalence.generate_target().scale(0.5).to_corner(UL)
        self.play(MoveToTarget(equivalence))
        self.wait()
        # left = equivalence[0:2]
        # left.generate_target().scale(0.5).to_corner(UL)
        # self.play(MoveToTarget(left))
        # general_vector = ListTex("i_1", "i_2", "\\cdots", "i_n",
        #                          sep=",", brace="()", color_list=[(2, YELLOW)]).next_to(equivalence[0], RIGHT)
        # self.play(Transform(equivalence[1], general_vector))
        # self.wait()
        #
        # df = TexMobject("i_k\\in \\{0,1\\}(k=1,2,\\cdots,n)", color=GREY).next_to(general_vector)
        # self.play(Write(df))
        # self.wait()

        self.add_caption("但是，这个图形在数学中指的是个啥东西呢？")
        eqv2 = VGroup(splits[0].copy(), TexMobject("\\Leftrightarrow", color=RED).scale(2),
                      TexMobject("?", color=BLUE).scale(2)).arrange(RIGHT)
        self.play(AnimationGroup(TransformFromCopy(splits[0], eqv2[0]), ShowCreation(eqv2[1:]), lag_ratio=0.5))
        self.wait()

        self.add_caption("直觉告诉我们这些图形分别指代着某个集合")
        self.add_caption("例如此处图形指的就是", "$A_1\\cap A_2\\cap A_3$", color_setting_list=[(1, BLUE)])
        set_from_cpt = TexMobject("A_1\\cap A_2\\cap A_3", color=BLUE).next_to(eqv2[1], RIGHT).shift(RIGHT*0.02)
        self.play(TransformFromCopy(self.cpt_mob[1], set_from_cpt), FadeOutAndShift(eqv2[2], UP))
        self.wait()

        self.add_caption("根据我们多年用维恩图做题的经验，这是很合理的")
        right_eq = VGroup(eqv2[1], set_from_cpt)
        right_eq.generate_target()[0].scale(0.5)
        right_eq.target[0].next_to(right_eq.target[1], LEFT)
        right_eq.target.next_to(equivalence[3], RIGHT)
        self.play(FadeOut(eqv2[0]), MoveToTarget(right_eq))

        self.add_caption("无需在意我用显然成立和经验之谈说明这两个等价关系")
        self.add_caption("毕竟图形起到的只是启发思路的作用")
        self.add_caption("抛开图形不谈，剩下两者的关系还是很明白的")
        # equivalence c=()\lra splits right_eq
        new_lra = TexMobject("\\Leftrightarrow", color=RED).move_to(equivalence[3])
        tmp = equivalence[0:2]
        tmp.generate_target().next_to(new_lra, LEFT)
        tmp2 = right_eq[1]
        tmp2.generate_target().next_to(new_lra, RIGHT)
        self.play(FadeOutAndShift(equivalence[3], UP),
                  ReplacementTransform(VGroup(equivalence[2], right_eq[0]), new_lra),
                  MoveToTarget(tmp), MoveToTarget(tmp2))
        self.wait()
        self.add_caption("对应方法也很简单，以", "(1, 1, 0, 0)", "为例", color_setting_list=[(1, BLUE)])
        eg_vec = TexMobject("(1, 1, 0, 0)", color=BLUE).scale(2).next_to(new_lra, DOWN, buff=0.8)
        lra_v = new_lra.copy().set_color(YELLOW).rotate(PI/2).next_to(eg_vec, DOWN)
        self.play(ReplacementTransform(self.cpt_mob[1].copy(), eg_vec),
                  ShowCreation(lra_v))
        lra_set = TexMobject("(", "A_1", "\\cap", "A_2", ")", "\\setminus",
                             "(", "A_3", "\\cup", "A_4", ")").next_to(lra_v, DOWN)
        lra_set[1:4].set_color(BLUE)
        lra_set[7:10].set_color(RED)
        lra_set[5].set_color(YELLOW)
        self.add_caption("分量为1的集合取交集，为0的取并集")
        self.play(ShowCreation(lra_set[1:4]), ShowCreation(lra_set[7:10]))
        self.add_caption("然后做差就好了")
        self.play(ShowCreation(VGroup(lra_set[0], lra_set[4:7], lra_set[10])))
        self.wait()
        self.play(FadeOut(VGroup(eg_vec, lra_v, lra_set)))

        self.add_caption("这样我们就把图形转化成了数学语言")
        self.add_caption("但这里还有一个问题")
        self.add_caption("我们在先前直观证明中，直接对图形进行了加减法")
        neq = VGroup(splits[3].copy(),  # 0
                     TexMobject("\\pm").scale(2),  # 1
                     splits[4].copy(),  # 2
                     TexMobject("\\nLeftrightarrow", color=YELLOW).scale(2),  # 3
                     TexMobject("A_1\\cap A_3 \\pm A_2\\cap A_3").scale(1.2),  # 4
                     ).arrange(RIGHT, buff=0.2).shift(DOWN)
        qz = TexMobject("=?").scale(2).set_color(RED)
        qz.next_to(neq[4], DOWN)
        srt = SurroundingRectangle(VGroup(neq, qz), color=YELLOW).scale(1.2)
        self.play(ShowCreation(srt), run_time=0.5)
        self.play(ShowCreation(neq[0:3]))
        self.add_caption("但对于集合，好像没有对应的计算")
        self.play(ShowCreation(neq[4]))
        self.play(ShowPassingFlashAround(neq[4]), GrowFromCenter(qz))
        self.play(ShowCreation(neq[3]), run_time=0.6)
        self.wait(2)

        self.add_caption("因此我们另寻思路，从证明内容本身出发", anim=[FadeOut(qz)])
        self.add_caption("容斥原理给出的是集合模的一个恒等关系")
        df2 = TexMobject("\\left|\\bigcup_{i=1}^{n}A_i\\right|",  # 0
                         "=",  # 1
                         "\\sum_{k=1}^{n}",  # 2
                         "(-1)^{k-1}",  # 3
                         "\\sum_{1\\le i_1 < \\cdots < i_k \\le n}",  # 4
                         "|A_{i_1}\\cap \\cdots \\cap A_{i_k}|"  # 5
                         ).scale(0.5).next_to(equivalence, DOWN, buff=0.5)
        self.play(FadeInFrom(df2, UP), run_time=0.6)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(df2, color=YELLOW)), run_time=0.4)
        self.wait()
        self.add_caption("从而我们很自然地想到用模长来代替")
        abs_neq = TexMobject("|A_1\\cap A_3| \\pm |A_2\\cap A_3|",
                             color=BLUE).scale(1.2).next_to(neq[3], RIGHT, buff=0.2)
        # abs_neq2 = TexMobject("|A_1\\cap A_2\\cap A_3|").next_to(eqv2[0:2], RIGHT)
        self.play(Transform(neq[4], abs_neq))
        revised_eq = TexMobject("\\Leftrightarrow", color=YELLOW).scale(2).move_to(neq[3])
        self.play(Transform(neq[3], revised_eq))
        self.wait()

        self.add_caption("但这样做的话，等价关系是不存在的")
        eg4neq = TexMobject("|A|=|B|", "\\nRightarrow", "A=B", color=BLUE).next_to(neq[3], DOWN, buff=0.6)
        eg4neq[1].set_color(YELLOW)
        self.play(ShowCreation(eg4neq), run_time=0.7)
        self.wait()
        self.add_caption("因此此处只有一个左推右的关系")
        self.play(Transform(neq[3], TexMobject(
            "\\Rightarrow", color=YELLOW).scale(2).next_to(neq[2], RIGHT)))
        self.wait()

        self.add_caption("这一点无伤大雅，我们来捋一下思路", anim=[FadeOutAndShift(df2, UP)])



run("P02 -pl")
