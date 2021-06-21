import math

from manimlib.imports import *


class Test(Scene):
    def construct(self):
        tex = TexMobject(r"\sup", r"\sin\cos", r"(n)")
        tex.get_parts_by_tex(r"\si").set_color(YELLOW)
        self.add(tex)
        self.wait()

run("-pl")