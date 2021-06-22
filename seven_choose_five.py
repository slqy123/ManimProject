from manimlib.imports import *


class P01(MyScene):
    """引入全错位排列"""

    def construct(self):
        info = TextMobject("在正片开始前，你需要了解关于全错位排列的知识\\\\",
                           "如果你已经了解，请跳转到**-**\\\\",
                           "接下来是定义与推导")
        info.arrange()
        self.play(ShowCreation(info), run_time=3)
        self.wait(4)
        self.play(FadeOutAndShift(info, UP), run_time=1.5)

        self.add_caption(r"现有$1\sim n$的自然数")
        one2n = ListTex("1", "2", "3", "\\cdots", "n-1", "n").scale(1.5).shift(UP)
        self.play(ShowCreation(one2n))
        self.wait()
        self.add_caption("重新排列这组数，得到一个排列", r"$i_i,i_2\sim i_n$", color_setting_list=[(1, BLUE)])
        t_one2n = ListTex("i_i", "i_2", "i_3", "\\cdots", "i_{n-1}", "i_n",
                          color=BLUE).scale(1.5).next_to(one2n, DOWN)
        self.play(ReplacementTransform(self.cpt_mob[1].copy(), t_one2n))
        self.wait()
        self.add_caption("要求对应位置的数字两两不相等，即:")

        tex_list = [("2", "i_2"), ("3", "i_3"), ("\\cdots", "\\cdots"),
                    ("n-1", "i_{n-1}"), ("n", "i_n")]
        r1 = SurroundingRectangle(one2n.idx(0), color=YELLOW)
        r2 = SurroundingRectangle(t_one2n.idx(0), color=YELLOW)
        neq = TexMobject("1 \\neq i_1", color=YELLOW).scale(1.5).next_to(t_one2n, DOWN).shift(DOWN*0.1)
        self.play(ShowCreation(r1), ShowCreation(r2))
        self.play(Write(neq))
        self.wait()
        for tex in tex_list:
            i, j = tex
            sr1 = SurroundingRectangle(one2n.get_parts_by_tex(i, substring=False))
            sr2 = SurroundingRectangle(t_one2n.get_parts_by_tex(j, substring=False))
            neqq = TexMobject(i+"\\neq "+j, color=YELLOW).scale(1.5).next_to(t_one2n, DOWN).shift(DOWN*0.1)
            self.play(Transform(r1, sr1), Transform(r2, sr2), Transform(neq, neqq))
            self.wait()

        self.wait(2)
        self.add_caption("定义已然明了，我们想知道的问题是：")
        self.add_caption("n个数的全错位排列一共有多少种呢？")
        self.wait(2)
        self.play(*map(FadeOut, self.mobjects), ApplyMethod(self.cpt_mob.move_to, ORIGIN))
        sr = SurroundingRectangle(self.cpt_mob, color=YELLOW)
        self.add(self.cpt_mob)
        self.play(ShowCreation(sr))
        self.play(FadeOut(VGroup(sr, self.cpt_mob)))

run("-pl")
