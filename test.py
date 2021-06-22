import math

from manimlib.imports import *


class Test(Scene):
    def construct(self):
        # tex = TexMobject(r"\sup", r"\sin\cos", r"(n)")
        # tex.get_parts_by_tex(r"\si").set_color(YELLOW)
        # self.add(tex)
        # self.wait()
        info = TextMobject("在正片开始前，你需要了解关于全错位排列的知识\\\\",
                           "如果你已经了解，请跳转到**-**\\\\",
                           "接下来是定义与推导")
        self.play(Write(info), run_time=3)
        self.wait(5)

        self.play(FadeOutAndShift(info, UP), run_time=1.5)

run("-pl")