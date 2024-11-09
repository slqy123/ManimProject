from manimlib.imports import *
from itertools import chain


class Test(Scene):
    def construct(self):
        NUM = 16
        points_list = VGroup()
        txt_list = VGroup()
        txt_str_list = []
        for i in range(NUM):
            txt_str = bin(i)[2:].zfill(4)
            txt_str_list.append(txt_str)
            txt = TextMobject(txt_str)
            txt.scale(0.5)
            if txt_str[0] == "0":
                # outside
                LEN = 2.3
                CTR = DOWN * 0.5
            else:
                # inside
                LEN = 1.15
                CTR = LEFT * 0.1 + DOWN * 0.35
            if txt_str[1] == "0":
                # front
                ADD = ORIGIN * 1
            else:
                ADD = UR * LEN * math.sqrt(2) / 2
            DIR = ORIGIN * 1
            if txt_str[2] == "0":
                DIR += UP
            else:
                DIR += DOWN
            if txt_str[3] == "0":
                DIR += LEFT
            else:
                DIR += RIGHT
            print(txt_str, CTR, DIR, LEN, ADD)
            point = Dot(CTR + DIR * LEN + ADD, radius=0.1, color=BLUE)

            txt.next_to(point, DR)
            points_list.add(point)
            txt_list.add(txt)

        self.play(FadeIn(points_list))
        self.wait(0.5)
        self.play(Write(txt_list))
        self.wait(1)

        def correspond(src, dst):
            count = 0
            for i in range(4):
                if src[i] == dst[i]:
                    count += 1
            if count == 3:
                count = int(src[0]) + int(dst[0])
                if count == 0:
                    COLOR = WHITE
                elif count == 1:
                    COLOR = YELLOW
                else:
                    COLOR = GREEN
                return COLOR
            else:
                return None

        all_lines = VGroup()
        for i in range(NUM):
            lines = VGroup()
            for j in range(NUM):
                COLOR = correspond(txt_str_list[i], txt_str_list[j])
                if COLOR:
                    line = Line(points_list[i].get_center(), points_list[j].get_center(), buff=0.1, color=COLOR)
                    lines.add(line)
            all_lines.add(lines)
            self.play(ShowCreation(lines))

        alls = VGroup(points_list, all_lines, txt_list)
        self.play(ApplyMethod(alls.to_edge, LEFT))

        path = ["0001", "0011", "0010", "0110", "0100", "0101", "0111", "1111", "1110", "1100", "1101", "1001", "1011",
                "1010", "1000", "0000"]
        path_txt = TexMobject("0000\\\\", *[("\\to " + i + "\\\\") for i in path])
        path_txt.to_edge(UR)
        path_txt[10:].shift(UP * 7.75 + LEFT * 2.2)
        self.play(Write(path_txt[0]), ApplyMethod(points_list[0].set_color, RED))
        former_point = "0000"
        self.wait(0.1)
        path_count = 1

        vec_list = VGroup()
        for pt in path:
            vec = Arrow(points_list[int(former_point, 2)].get_center(), points_list[int(pt, 2)].get_center(), buff=0.1,
                        color=RED, tip_length=0.2)
            vec_list.add(vec)
            self.play(ApplyMethod(points_list[int(pt, 2)].set_color, RED), Write(path_txt[path_count]))
            self.wait(0.2)
            self.play(ShowCreation(vec))
            former_point = pt
            path_count += 1
            self.wait(0.1)
        the_path = VGroup(vec_list, txt_list)
        self.play(FadeOut(path_txt), ApplyMethod(the_path.shift, RIGHT * 6.4))
        self.wait(2)
        self.play(FadeOut(the_path), ApplyMethod(alls[0:2].move_to, ORIGIN))
        self.wait(1)


class Test2(Scene):
    def construct(self):
        NUM = 16
        in_points_list = VGroup()
        out_points_list = VGroup()
        points_list = VGroup()
        txt_list = VGroup()
        txt_str_list = []
        for i in range(NUM):
            txt_str = bin(i)[2:].zfill(4)
            txt_str_list.append(txt_str)
            txt = TextMobject(txt_str)
            txt.scale(0.5)
            if txt_str[0] == "0":
                # outside
                LEN = 2.3
                CTR = DOWN * 0.5
                out = True
            else:
                # inside
                LEN = 1.15
                CTR = LEFT * 0.1 + DOWN * 0.35
                out = False
            if txt_str[1] == "0":
                # front
                ADD = ORIGIN * 1
            else:
                ADD = UR * LEN * math.sqrt(2) / 2
            DIR = ORIGIN * 1
            if txt_str[2] == "0":
                DIR += UP
            else:
                DIR += DOWN
            if txt_str[3] == "0":
                DIR += LEFT
            else:
                DIR += RIGHT
            print(txt_str, CTR, DIR, LEN, ADD)
            point = Dot(CTR + DIR * LEN + ADD, radius=0.1, color=BLUE)
            if out:
                out_points_list.add(point)
            else:
                in_points_list.add(point)
            points_list.add(point)
            txt.aim = point
            txt.add_updater(lambda a: a.next_to(a.aim, DR))
            txt_list.add(txt)

        self.play(FadeIn(VGroup(in_points_list, out_points_list)))
        self.wait(0.5)
        self.play(Write(txt_list))
        self.wait(1)

        def correspond(src, dst):
            count = 0
            for k in range(4):
                if src[k] == dst[k]:
                    count += 1
            if count == 3:
                count = int(src[0]) + int(dst[0])
                if count == 0:
                    COLOR = WHITE
                elif count == 1:
                    COLOR = YELLOW
                else:
                    COLOR = GREEN
                return COLOR
            else:
                return None

        all_lines = VGroup()
        for i in range(NUM):
            lines = VGroup()
            for j in range(NUM):
                COLOR = correspond(txt_str_list[i], txt_str_list[j])
                if COLOR:
                    line = Line(points_list[i].get_center(), points_list[j].get_center(), buff=0.1, color=COLOR)
                    line.aim1 = points_list[i]
                    line.aim2 = points_list[j]
                    line.add_updater(lambda a: a.put_start_and_end_on(a.aim1.get_center(), a.aim2.get_center()))
                    lines.add(line)
            all_lines.add(lines)
            self.play(ShowCreation(lines), run_time=0.5, rate_func=linear)

        self.play(in_points_list.shift, UP)
        self.play(out_points_list.shift, LEFT)



def main():
    os.system("python -m manim super_four.py Test2 -pl")


if __name__ == "__main__":
    main()
