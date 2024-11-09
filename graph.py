from manimlib.imports import *

class L1(MyScene):
    def construct(self):
        self.camera.set_frame_width(0.4*FRAME_WIDTH)
        self.camera.set_frame_height(0.6*FRAME_HEIGHT)
        dots = VGroup()
        dots.add(Dot(1 * UP))
        dots.add(Dot(1.4 * LEFT + DOWN * 0.3))
        dots.add(Dot(1.4 * RIGHT + DOWN * 0.3))
        lines = VGroup()
        for i in range(len(dots)):
            lines.add(Line(dots[i].get_center(), dots[(i + 1) % 3].get_center(), buff=SMALL_BUFF, color=RED))
        g = Graph(dots=dots, scene=self)
        g.add_lines(*lines)
        self.wait(3)
        g.add_dots(g.dot(1, 1.3*DOWN), g.dot(2, 1.3*DOWN))
        g.add_lines(g.line(1, 3, color=RED), g.line(2, 4, color=RED), g.line(3, 4, color=RED))
        self.wait(3)

        asline = Line(g.center(0), g.center(3), color=RED)
        self.play(ShowCreation(asline))
        self.wait(3)
        g.highlight([2, 1, 3, 4])
        self.wait()
        g.highlight([2, 0, 3, 4])
        self.wait(3)
        self.play(Uncreate(asline))
        self.wait(3)

        asline = Line(g.center(1), g.center(4), color=RED)
        self.play(ShowCreation(asline))
        self.wait(3)
        g.highlight([2, 1, 3, 4])
        self.wait()
        g.highlight([2, 0, 1, 4])
        self.wait(3)
        self.play(Uncreate(asline))
        self.wait(3)

        g.add_dots(g.dot(1, UL*0.8), g.dot(0, UL*0.8))
        g.add_lines(g.line(0, 6, color=RED),
                    g.line(6, 5, color=RED),
                    g.line(5, 1, color=RED))
        self.wait(3)

        g.add_dots(g.dot(0, UR*0.8), g.dot(2, UR*0.8))
        g.add_lines(g.line(0, 7, color=RED),
                    g.line(7, 8, color=RED),
                    g.line(8, 2, color=RED))
        self.wait(3)

        asline = g.line(3, 6, color=BLUE)
        self.play(ShowCreation(asline))
        self.wait(3)

        g.highlight([6, 5, 1, 3])
        self.wait()
        g.highlight([6, 5, 1, 0])
        self.wait(3)

        asline2 = g.line(3, 8, color=BLUE)
        asline3 = g.line(8, 6, color=BLUE)
        self.play(ShowCreation(VGroup(asline2, asline3)))
        self.wait(3)

        asline4 = g.line(6, 1, color=BLUE)
        asline5 = g.line(8, 1, color=BLUE)
        self.play(ShowCreation(VGroup(asline4, asline5)))
        self.wait(3)

        g.highlight([8, 6, 1])
        self.wait()
        g.highlight([8, 6, 3])
        self.wait(3)


class LL1(MyScene):
    def construct(self):
        self.camera.set_frame_width(0.5*FRAME_WIDTH)
        self.camera.set_frame_height(0.7*FRAME_HEIGHT)
        dots = VGroup()
        dots.add(Dot(1 * UP))
        dots.add(Dot(1.4 * LEFT + DOWN * 0.3))
        dots.add(Dot(1.4 * RIGHT + DOWN * 0.3))
        dots.shift(DOWN)
        lines = VGroup()
        for i in range(len(dots)):
            lines.add(Line(dots[i].get_center(), dots[(i + 1) % 3].get_center(), buff=SMALL_BUFF, color=RED))
        g = Graph(dots=dots, scene=self)
        g.add_lines(*lines)
        self.wait(3)
        g.add_dots(g.dot(0, UP*1.3))
        g.add_lines(g.line(3, 1, color=RED),
                    g.line(3, 2, color=RED))
        self.wait(3)
        g.highlight([3, 1, 0, 2])
        self.wait(3)

        g.add_dots(g.dot(1, LEFT*0.5+UP*1))
        g.add_lines(g.line(4, 1, color=RED),
                    g.line(4, 3, color=RED))
        self.wait(3)

        g.highlight([3, 1, 0, 2])
        g.highlight([3, 1, 4])
        self.wait(3)

        self.play(ShowCreationThenDestruction(g.line(1, 2, color=YELLOW)))
        self.wait(3)

        self.play(Uncreate(VGroup(g.dot_group[4], g.line_group[5:7])))
        self.wait(3)
        g.dot_group.remove(g.dot_group[4])
        g.line_group.remove(g.line_group[5], g.line_group[6])

        g.add_dots(g.dot(1, RIGHT*0.8+UP*0.4))
        g.add_lines(g.line(4, 0, color=RED),
                    g.line(4, 1, color=RED))
        self.wait(3)
        self.play(Uncreate(VGroup(g.dot_group[4], g.line_group[5:7])))
        self.wait(3)
        g.dot_group.remove(g.dot_group[4])
        g.line_group.remove(g.line_group[5], g.line_group[6])

        g.add_dots(g.dot(1, DOWN), g.dot(2, DOWN))
        g.add_lines(g.line(1, 4, color=RED),
                    g.line(4, 5, color=RED),
                    g.line(5, 2, color=RED))
        self.wait(3)

        g.highlight([0, 1, 4, 5, 2])
        self.wait(2)
        g.add_lines(g.line(0, 4, color=BLUE),
                    g.line(0, 5, color=BLUE))
        self.wait(3)

        g.highlight([3, 1, 4, 5, 2])
        self.wait(2)
        g.add_lines(g.line(3, 4, color=BLUE),
                    g.line(3, 5, color=BLUE))
        self.wait(3)

        cline = g.line(3, 0, color=BLUE)
        g.add_lines(cline)

        g.highlight([3, 4, 0])
        g.highlight([3, 5, 0])
        self.wait(3)

        self.play(cline.set_color, RED)
        self.wait(3)

        g.highlight([1, 3, 2, 0])
        g.highlight([1, 3, 0, 2])
        self.wait(3)


class L2(MyScene):
    def construct(self):
        self.camera.set_frame_width(0.5*FRAME_WIDTH)
        self.camera.set_frame_height(0.7*FRAME_HEIGHT)
        dots = VGroup(Dot(UP+1.5*RIGHT),
                      Dot(UP+1.5*LEFT),
                      Dot(DOWN+1.5*RIGHT),
                      Dot(DOWN+1.5*LEFT),)
        dots.shift(LEFT*0.5+DOWN*0.7)
        g = Graph(dots, self)
        g.add_lines(g.line(0, 1, color=BLUE),
                    g.line(1, 3, color=BLUE),
                    g.line(3, 2, color=BLUE),
                    g.line(2, 0, color=BLUE))
        self.wait(3)

        sline = g.line(1, 2, color=BLUE)
        self.play(ShowCreation(sline))
        self.wait(3)

        g.highlight([1, 2, 3])
        g.highlight([1, 2, 0])
        self.wait(2)
        self.play(Uncreate(sline))
        self.wait(3)

        g.add_dots(g.dot(1, RIGHT*1.5+2*UP))
        g.add_lines(g.line(4, 1, color=BLUE),
                    g.line(4, 0, color=BLUE))
        self.wait(3)

        cline = g.line(4, 2, color=BLUE)
        self.play(ShowCreation(cline))
        self.wait(3)

        g.highlight([4, 0, 1])
        g.highlight([4, 0, 2])
        self.wait(2)
        self.play(Uncreate(cline))
        self.wait(3)

        g.add_dots(g.dot(0, DOWN+RIGHT*2))
        g.add_lines(g.line(5, 0, color=BLUE),
                    g.line(5, 2, color=BLUE))
        self.wait(3)

        # g.add_dots(g.dot(1, DOWN+LEFT*2),
        #            g.dot(3, RIGHT*1.5+DOWN*2))
        # g.add_lines(g.line(6, 1, color=BLUE),
        #             g.line(6, 3, color=BLUE),
        #             g.line(7, 3, color=BLUE),
        #             g.line(7, 2, color=BLUE))
        # self.wait(3)

        g.add_lines(g.line(3, 4, color=RED),
                    g.line(3, 5, color=RED))
        self.wait(3)

        bline = g.line(4, 5, color=BLUE)
        self.play(ShowCreation(bline))
        self.wait(2)
        g.highlight([4, 0, 1])
        g.highlight([4, 0, 5])
        self.wait(3)

        self.play(bline.set_color, RED)
        self.wait(3)


class Show(Scene):
    def construct(self):
        dots = VGroup(Dot(LEFT*1.5, color=BLACK),
                      Dot(RIGHT*1.5, color=BLACK))
        g = Graph(dots, self)
        g.add_dots(g.dot(0, LEFT*4, color=BLACK),
                   g.dot(1, RIGHT*4, color=BLACK))
        g.add_lines(g.line(0, 2, color=BLUE))

        g.add_dots(g.dot(2, RIGHT*2+UP*2, color=BLACK),
                   g.dot(1, RIGHT*2+UP*2, color=BLACK),
                   g.dot(1, RIGHT*2+DOWN*2, color=BLACK))
        g.add_lines(g.line(4, 2, color=BLUE),
                    g.line(4, 0, color=BLUE),
                    g.line(5, 1, color=RED),
                    g.line(5, 3, color=RED),
                    g.line(6, 1, color=RED),
                    g.line(6, 3, color=RED))
        self.wait()


class Test(Scene):
    def construct(self):
        a = Square().shift(RIGHT)
        b = Square()
        c = Square().shift(UP)
        self.play(Transform(VGroup(*self.mobjects), b))
run("Test -pl")
