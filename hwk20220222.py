from utils.mobjects.BooleanOperationsOnPolygons import *
from manimlib.imports import *


class Hwk(Scene):
    def construct(self):
        c1 = Circle(radius=3).shift(LEFT * 2)
        c2 = Circle(radius=3).shift(RIGHT * 2)
        rect = Rectangle(width=12, height=7)
        res = set_split([c1, c2, rect],
                        [[1, 0, 1],
                         [1, 1, 1],
                         [0, 1, 1],
                         [0, 0, 1]],
                        color_list=[RED, GREEN, YELLOW, BLUE])
        self.add(res.set_width(FRAME_WIDTH).set_height(FRAME_HEIGHT))
        self.wait()

run('-pl')
