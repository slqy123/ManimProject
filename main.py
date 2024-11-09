from manimlib.imports import *

class Test(Scene):
    def construct(self):
        theta0 = 5 * DEGREES
        sin = math.sin(theta0)
        wid = 0.8
        coord = FRAME_X_RADIUS*LEFT + FRAME_Y_RADIUS*UP
        count = 9
        n = 1.35

        all_mob = VGroup()
        for i in range(count):
            coord2 = coord + wid*DOWN + math.tan(math.asin(sin))*RIGHT
            line = Line(coord, coord2)
            edge = Line(FRAME_X_RADIUS*LEFT, FRAME_X_RADIUS*RIGHT).move_to(coord2, coor_mask=[0, 1, 1])
            all_mob.add(line, edge)

            coord = coord2
            sin = sin*n

        all_mob.flip(UP).rotate(PI/2).shift(DOWN*4.5)
        self.add(all_mob)
        self.wait(3)


class A(Scene):
    def construct(self):
        self.add(Dot())
        self.wait(142857)
run("A -pl")

