import math

from utils.mobjects.BooleanOperationsOnPolygons import *
from manimlib.imports import *
import random


class Text(Text):
    CONFIG = {
        "font": "YaHei"
    }


class Test(GraphScene):
    def construct(self):
        # tex = TexMobject(r"\sup", r"\sin\cos", r"(n)")
        # tex.get_parts_by_tex(r"\si").set_color(YELLOW)
        # self.add(tex)
        # self.wait()
        # info = TextMobject("在正片开始前，你需要了解关于全错位排列的知识\\\\"
        #                    "如果你已经了解，请跳转到**-**\\\\"
        #                    "接下来是定义与推导")
        # self.play(Write(info), run_time=3)
        # self.wait(5)
        #
        # self.play(FadeOutAndShift(info, UP), run_time=1.5)
        #
        # t1 = TexMobject(*["%d" % i for i in range(10)]).shift(UP)
        # t2 = TexMobject(*["%d" % (9-i) for i in range(8)]).shift(DOWN+RIGHT)
        # t1.align_submobjects(t2)
        # self.add(t1, t2)
        #
        # c = Circle()
        # v = VGroup(c, c.copy(), c.copy())
        # v2 = v.deepcopy()
        # m = Mapping(left_elements=v, right_elements=v2, sep=0.5, distance=3)
        # m.show_anim(self)
        # cnn = m.connect(0, 2, color=BLUE)
        # self.play(ShowCreation(cnn))
        # self.wait()
        # c1 = Circle(radius=2, color=WHITE).shift(LEFT)
        # c2 = Circle(radius=2, color=WHITE).shift(RIGHT)
        # c3 = Circle(radius=2, color=WHITE).shift(1.5 * UP)
        #
        # splits = set_split(mobs=[c1, c2, c3],
        #                    case=[[1, 0, 0],
        #                          [0, 1, 0],
        #                          [0, 0, 1],
        #                          [1, 1, 0],
        #                          [1, 0, 1],
        #                          [0, 1, 1],
        #                          [1, 1, 1]],
        #                    color_list=[RED, GREEN, BLUE, ORANGE, PINK, LIGHT_BROWN, YELLOW])
        # self.play(AnimationGroup(*map(ShowCreation, [c1, c2, c3]), lag_ratio=0.15), run_time=0.7)
        # self.play(AnimationGroup(*map(GrowFromCenter, splits), lag_ratio=0.15), FadeOut(VGroup(c1, c2, c3)), run_time=1)
        # self.play(*map(lambda a: ApplyMethod(a.shift, np.array([2 * (random.random() - 0.5),
        #                                                         2 * (random.random() - 0.5), 0])), splits))
        # self.wait()
        # tx = TexMobject("1", "2", "3")
        # self.add(tx)
        # tx[1].generate_target().next_to(tx[0], DOWN)
        # tx[2].generate_target().next_to(tx[1].target, DOWN)
        # self.play(MoveToTarget(tx[1]), MoveToTarget(tx[2]))
        # lb = TexMobject("(")
        # self.play(ShowCreation(lb))
        # a = Square(color=BLUE).set_fill(color=RED, opacity=0.5)
        # self.add(a)
        # self.play(FocusOn(a))
        # self.play(Indicate(a))
        # self.wait()
        # a = Square()
        # self.add(a)
        # a.save_state()
        # self.play(Uncreate(a))
        # a.restore()
        # self.play(ShowCreation(a))

        # b = VGroup(*[Circle() for i in range(3)]).arrange()
        # b[0:2].generate_target().shift(RIGHT)
        # self.play(MoveToTarget(b[0:2]))
        # c = b[0:2]
        # c.generate_target().shift(RIGHT)
        # self.play(MoveToTarget(c))
        # self.play(Transform(b[0:2], b[0:2].copy().shift(RIGHT)))
        # a = TexMobject("\\neq")
        # self.play(a[0][1].shift, UP, a[0][0].shift, DOWN)
        # self.setup_axes(animate=True)
        # print(self.coords_to_point(5, 6))
        # def func(mob, alpha):
        #     mob.shift(0.05*RIGHT)
        #     mob.rotate(PI/25)
        # a = Square().shift(LEFT*3)
        # b = a.copy().scale(math.sqrt(2)).set_color(YELLOW)
        # b.add_updater(lambda c: c.move_to(a))
        # d = Line(LEFT_SIDE, RIGHT_SIDE, color=BLUE)
        # d.next_to(a, DOWN, buff=0)
        # e = Line(a.get_center(), a.get_center()+DOWN, color=RED)
        # e.add_updater(lambda i: i.put_start_and_end_on(a.get_center(), a.get_center()+DOWN))
        # self.add(b, d, e)
        # self.play(UpdateFromAlphaFunc(a, func), run_time=5)
        # line = Line(LEFT, RIGHT)
        # line = line.append_points([UP, UR, DOWN, LEFT_SIDE])
        # self.play(ShowCreation(line))
        # self.wait()
        # a = Circle()
        # self.play(ShowCreation(a))
        # self.remove(a)
        # self.play(ShowCreation(a))
        # self.wait()
        # txt = TextMobject("abc", "$\\bigcap$", "$\\bigcup$").set_color_by_tex_to_color_map({"\\": BLUE, "a": RED})
        # self.play(ShowCreation(txt))
        # law = TextMobject("图形代表的集合", "=", "$\\bigcap $ 包含该图形的集合", "$\\setmius $", "$\\bigcup $ 不包含该图形的结合")
        # self.add(law)
        # self.wait()
        # c1 = Circle()
        # c2 = c1.copy().shift(RIGHT)
        # c1.save_state()
        # self.play(ShrinkToCenter(c1))
        # c1.scale(100)
        # self.play(c1.to_corner, DR)
        # c = TextMobject("\\{\\}").set_height(FRAME_HEIGHT/3, stretch=True)
        # self.play(Write(c[0][0]))
        # self.wait()
        # t = TexMobject("\\{P|P[1]=1\\}")
        # self.play(ShowCreation(t))
        # d = c.copy()
        # p = Dot(c.get_center()).set_stroke(width=0).set_fill(opacity=0)
        # c.add_updater(lambda a, dt: a.rotate(PI*dt))

        # c.add_updater(lambda a, dt: a.rotate(PI*dt))
        # turn_animation_into_updater(ScaleInPlace(c, 0))
        # self.add(c)
        # self.wait()
        # self.remove(c)
        # self.wait()
        # self.play(Transform(c, p), UpdateFromAlphaFunc(c, lambda a, alpha: a.rotate(PI*alpha**1.5).fade(alpha)), GrowFromCenter(d), rate_func=linear)
        # self.play(GrowingAndRotatingFromCenter(c))
        a = Circle().shift(LEFT)
        b = Square().shift(RIGHT)
        self.add(a)
        self.play(CyclicReplace(a, b), run_time=2)
        self.wait()
class RoundDot(Scene):

    def construct(self):
        r = 3.5
        n = 16
        start_angle = 0
        center = ORIGIN
        dgroup = VGroup()
        lgroup = VGroup()
        dot = Dot(color=BLUE).scale(1.5)
        omega = 2
        t = ValueTracker(0)

        def move_func(mob):
            dst = math.cos(omega*t.get_value() + mob.theta)
            alpha = (dst + 1)/2
            mob.move_to(mob.start * alpha + mob.end * (1-alpha))

        for i in range(n // 2):
            dotcp = dot.copy().move_to(np.array([math.cos(start_angle + i * 2 * PI / n),
                                                 math.sin(start_angle + i * 2 * PI / n), 0]) * r + center)
            dotcp.theta = i * 2 * PI / n
            dotcp.start = dotcp.get_center()
            dotcp.end = -dotcp.start
            line = Line(dotcp.start, dotcp.end, color=GREY)
            lgroup.add(line)
            dotcp.add_updater(move_func)
            dgroup.add(dotcp)
        mainc = Circle(radius=r)
        self.add(mainc)
        sep = 2 * PI / omega
        for i in range(n//2):
            self.add(lgroup[i], dgroup[i])
            self.play(t.increment_value, sep, run_time=sep, rate_func=linear)
        self.play(t.increment_value, 2*PI, run_time=2*PI, rate_func=linear)


class DrawRect(Scene):
    def construct(self):
        dotgroup = VGroup(*[Dot(5*LEFT + i/3*10*RIGHT) for i in range(4)])
        line = Line(5*LEFT, 5*RIGHT, buff=0, color=BLACK)
        vline = Line(0.1*UP, 0.1*DOWN, color=BLACK, buff=0)
        db = Brace(line, DOWN, color=BLACK, buff=1)
        dbl = TexMobject("2").next_to(db, DOWN).set_color(BLUE)
        ubgroup = VGroup(*[Brace(Line(dotgroup[i], dotgroup[i+1]), UP, color=BLACK, buff=1) for i in range(3)])
        ubgroup[0].set_color(RED)
        ubl = TexMobject("{2\\over 3}", color=RED).next_to(ubgroup[0], UP)
        self.add(line, vline, db, dbl, ubgroup, ubl)
        self.wait()

class Another(Scene):
    def construct(self):
        sq = Square(color=BLACK).scale(2.5)
        line = Line(sq.get_edge_center(UL), sq.get_edge_center(DR), color=BLUE, buff=0)
        n1 = TexMobject("1", color=BLACK).scale(0.7).next_to(sq, UP)
        n1p = n1.copy().next_to(sq, LEFT)
        qst = TexMobject("?", color=RED).shift(UR*0.2)
        self.add(sq, line, n1, n1p, qst)
        self.wait()


class TestSound(MyScene):
    def construct(self):
        q = Square()
        p = Rectangle()
        # self.play(AnimationGroup(ShowCreation(p), run_time=2), run_time=4)
        self.add_caption("啊这", anim=[ShowCreationThenDestruction(VGroup(p, q))],  sound="isuzu.ogg")

class SubString(Scene):
    def construct(self):
        a = TexMobject("P(\\mathrm{score}=0)=0", substrings_to_isolate=["score", "P", "0"]).set_color_by_tex_to_color_map(
            {"P": BLUE, "score": YELLOW, "0": RED}
        )
        self.play(ShowCreation(a))
        self.wait()
run("SubString -pl")
