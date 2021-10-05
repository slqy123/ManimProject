from manimlib.imports import *

class Text(Text):
    CONFIG = {"font": "consolas"}

class State:
    def __init__(self, *args, **kwargs):
        self.txt = Text(*args, **kwargs)
        self.sr = SurroundingRectangle(self.txt, color=YELLOW).scale(1.2).stretch(2, 0)
        self.mobs = VGroup(self.txt, self.sr)

class P(Scene):
    def construct(self):
        halt = Text("halt-end", color=BLUE).scale(2).to_edge(UP, buff=0.6)
        eps = Ellipse(height=halt.get_height()*1.5, width=halt.get_width()*1.5).move_to(halt.get_center())
        state05 = VGroup()
        for i in range(5):
            s = State(str(i))
            state05.add(s.mobs)
        state05.arrange(RIGHT, buff=2).move_to(ORIGIN)

        ar = Arrow(start=state05[0].get_edge_center(RIGHT),
                   end=state05[1].get_edge_center(LEFT),
                   color=BLUE, buff=0.1)
        indication = Text("1 1 r").next_to(ar, UP, buff=0.05)
        ar_idc = VGroup(ar, indication)
        for i in range(3):
            self.add(ar_idc.copy().next_to(state05[i+1], RIGHT, buff=0.1).move_to(ar_idc, coor_mask=np.array([0, 1, 1])))
        for i in range(5):
            er_arr = Arrow(start=state05[i].get_edge_center(UP),
                           end=eps.get_edge_center(DOWN),
                           color=RED, buff=0.2)
            idc = Text("_ _ l").scale(0.8).move_to(er_arr.get_center())
            self.add(er_arr, idc)
        s5 = State("5").mobs
        s6 = State("6").mobs
        s56 = VGroup(s6, s5).arrange(RIGHT, buff=3).next_to(state05, DOWN, buff=1)
        arrc = Arrow(start=state05[4].get_edge_center(DOWN),
                     end=s5.get_edge_center(RIGHT),
                     color=GREY, buff=0.2)
        idcc = Text("1 f *").move_to(arrc.get_center()).shift(DOWN*0.3+RIGHT*0.2)
        arc = Arc(start_angle=3*PI/4, angle=3*PI/2).stretch(0.7, dim=1).next_to(s5, DOWN, buff=0.03).add_tip().set_color(GREY)
        self.add(arc)
        caltxt = Text("* * l").move_to(arc.get_center())

        arrcc = Arrow(start=s5.get_edge_center(LEFT),
                      end=s6.get_edge_center(RIGHT),
                      color=GREY, buff=0.1)
        idccc = Text("_ _ r").next_to(arrcc, UP, buff=0.05)
        arcc = arc.copy().next_to(s6, DOWN, buff=0.03)
        arcctxt = Text("1 _ r").move_to(arcc)

        arrf = Arrow(start=s6.get_edge_center(LEFT),
                     end=state05[0].get_edge_center(DOWN),
                     buff=0.2, color=LIGHT_GREY)
        ftxt = Text("f _ r").move_to(arrf.get_center()+DOWN*0.4+LEFT*0.2)
        self.add(arrc, idcc, caltxt, arrcc, idccc, arcc, arcctxt, arrf, ftxt)
        self.add(s56)
        self.add(halt, eps, state05, ar, indication)
        self.wait()



run("-p -s")