from manimlib.imports import *


class Calisson:
    def __init__(self):
        self.mob = Polygon(np.array([np.sqrt(3), 0, 0]),
                           np.array([0, 1, 0]),
                           np.array([-np.sqrt(3), 0, 0]),
                           np.array([0, -1, 0]))


class Eg(Scene):
    def construct(self):
        # rt = Polygon(*get_circle_coords(3), color=BLACK, fill_color=GREY, fill_opacity=1)
        # lt = Polygon(*get_circle_coords(3, start=PI), color=BLACK)

        # lt.next_to(rt, UP, buff=LARGE_BUFF)
        # self.add(lt, rt)

        # lt.next_to(rt, LEFT, buff=0)
        # ar = Arrow(rt.get_center_of_mass(), lt.get_center_of_mass(), color=BLACK, stroke_width=3, buff=0)
        # r1 = VGroup(lt, rt, ar)
        r2 = r1.copy().shift(UP * 2.5).rotate(2 * PI / 3)
        r3 = r1.copy().shift(DOWN * 2.5).rotate(-2 * PI / 3)
        self.add(r1, r2, r3)
        # V = np.array([np.sqrt(3)/2, 0.5, 0])
        # for i in range(7):
        #     c = np.array([0, -3+i, 0])
        #     l1 = Line(c-i*V, c+3*V, color=BLACK)
        #     l2 = l1.copy().ro

        self.wait()


run("Eg -s -c WHITE")
