import random

import numpy as np

from utils.mobjects.BooleanOperationsOnPolygons import *
from manimlib.imports import *


class Text(Text):
    CONFIG = {
        "font": "Consolas"
    }


class P01(MyScene):
    def construct(self):
        self.add_caption("我们先来看看什么是容斥原理")
        title = TextMobject("容斥原理", color=YELLOW).to_edge(UP)
        cline = Line(start=LEFT_SIDE, end=RIGHT_SIDE, color=GREY).set_stroke(GREY, opacity=0.3)
        cline.next_to(title, DOWN)
        self.play(AnimationGroup(Write(title), ShowCreation(cline), lag_ratio=0.3))
        self.wait()

        df1 = TextMobject("对n个集合", "$A_1,\\cdots,A_n$", "并集与交集之间有如下关系").scale(0.8)
        df1[1].set_color(BLUE)
        df1.next_to(cline, DOWN).to_edge(LEFT)
        self.play(Write(df1))
        self.wait()

        df2 = TexMobject("\\left|\\bigcup_{i=1}^{n}A_i\\right|",  # 0
                         "=",  # 1
                         "\\sum_{k=1}^{n}",  # 2
                         "(-1)^{k-1}",  # 3
                         "\\sum_{1\\le i_1 < \\cdots < i_k \\le n}",  # 4
                         "|A_{i_1}\\cap \\cdots \\cap A_{i_k}|").scale(0.8)  # 5
        df2.next_to(df1, DOWN, aligned_edge=LEFT)
        self.play(Write(df2), run_time=3)
        self.wait(3)

        self.add_caption("看不懂不要紧，我们以n=3的情况举例说明含义")
        c1 = Circle(radius=2, color=WHITE).shift(LEFT)
        c2 = Circle(radius=2, color=WHITE).shift(RIGHT)
        c3 = Circle(radius=2, color=WHITE).shift(1.5 * UP)
        cgroup = VGroup(c1, c2, c3)
        cgroup.scale(0.75).to_corner(DR, buff=0.8)

        splits = set_split(mobs=cgroup,
                           case=[[1, 0, 0],  # 0
                                 [0, 1, 0],  # 1
                                 [0, 0, 1],  # 2
                                 [1, 1, 0],  # 3
                                 [1, 0, 1],  # 4
                                 [0, 1, 1],  # 5
                                 [1, 1, 1]],  # 6
                           color_list=[RED, GREEN, BLUE, ORANGE, PINK, LIGHT_BROWN, YELLOW])
        self.play(AnimationGroup(*map(ShowCreation, cgroup), lag_ratio=0.15), run_time=0.7)
        self.wait()

        self.add_caption("三个圆相交在一起把整个图形分成了若干块")
        self.add_caption("我们染上颜色以示区别")
        self.play(AnimationGroup(*map(GrowFromCenter, splits), lag_ratio=0.15),
                  FadeOut(cgroup), run_time=1)
        a1 = TexMobject("A_1").next_to(c1, LEFT)
        a2 = TexMobject("A_2").next_to(c2, RIGHT)
        a3 = TexMobject("A_3").next_to(c3, UP)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, UP), [a1, a2, a3]), lag_ratio=0.2))
        self.wait()

        self.add_caption("接下来我们来看等式左边")
        sr = SurroundingRectangle(df2[0], color=YELLOW)
        self.play(ShowCreation(sr))
        self.wait()
        self.add_caption("这是对所有集合求并集，也就是所有小块的面积之和")
        eq1 = self.join(splits, range(len(splits)),
                        TexMobject("+").scale(2)).scale(0.3). \
            next_to(df2, DOWN, aligned_edge=LEFT)
        self.play(ReplacementTransform(splits.copy(), eq1))
        self.wait()

        self.add_caption("再来看右边第一个求和符号")
        sr2 = SurroundingRectangle(df2[2], color=YELLOW)
        self.play(Transform(sr, sr2))
        self.wait()
        self.add_caption("这里的k代表做交集的集合个数")
        self.add_caption("当k=1时，结果就是所有单个集合相加")
        sr2 = SurroundingRectangle(df2[4:], color=YELLOW)
        self.play(Transform(sr, sr2))
        self.wait()
        pre_eq2 = TexMobject("|A_1|", "+|A_2|", "+|A_3|").scale(0.6).next_to(eq1, DOWN, aligned_edge=LEFT)
        equal_sign = TexMobject("=").scale(0.6).next_to(pre_eq2, LEFT)
        self.play(ShowCreation(VGroup(equal_sign, pre_eq2)))
        self.wait()

        self.add_caption("当k=2是就是所有两个集合的交集之和，k=3也同理")
        pre_eq3 = TexMobject("-", "(", "|A_1\\cap A_2|", "+|A_2\\cap A_3|", "+|A_3\\cap A_1|", ")").scale(0.6).next_to(
            pre_eq2, DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(pre_eq3))
        self.wait()
        pre_eq4 = TexMobject("+|A_1\\cap A_2\\cap A_3|").scale(0.6).next_to(pre_eq3, DOWN, aligned_edge=LEFT)
        self.play(ShowCreation(pre_eq4))
        self.wait()

        self.add_caption("注意k=2时结果为负")
        sr2 = SurroundingRectangle(df2[3], color=YELLOW)
        sr3 = SurroundingRectangle(pre_eq3, color=BLUE)
        self.play(AnimationGroup(Transform(sr, sr2), ShowCreationThenDestruction(sr3), lag_ratio=0.5))
        self.wait()

        self.add_caption("我们分别将他们用图形表示出来")
        # 重排正项
        pre_eq2.generate_target().arrange(DOWN, center=False, aligned_edge=LEFT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER).next_to(eq1, DOWN,
                                                                                                aligned_edge=LEFT)
        pre_eq4.generate_target().next_to(pre_eq2.target, DOWN, aligned_edge=LEFT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER)
        pre_eq3.generate_target().next_to(pre_eq2.target, RIGHT, buff=2.1)
        self.play(AnimationGroup(*map(MoveToTarget, [pre_eq2, pre_eq3, pre_eq4]), lag_ratio=0.1))

        # 重排负项
        target_coord = pre_eq3[3].get_center()
        tgt = pre_eq3[2:5].copy().arrange(DOWN, center=False, aligned_edge=RIGHT,
                                          buff=2.3 * DEFAULT_MOBJECT_TO_MOBJECT_BUFFER).move_to(target_coord)
        self.play(Transform(pre_eq3[2:5], tgt))
        pre_eq3_left = pre_eq3[0:2].copy().scale(5).next_to(pre_eq3[2:5], LEFT)
        pre_eq3_left[0].scale(0.2).next_to(pre_eq3_left[1], LEFT)
        pre_eq3_right = pre_eq3[5].copy().scale(5).next_to(pre_eq3[2:5], RIGHT)
        self.play(Transform(pre_eq3[0:2], pre_eq3_left), Transform(pre_eq3[5], pre_eq3_right))

        # 替换正项
        eq2_1 = self.join(splits, (0, 3, 4, 6), TexMobject("+").scale(2))
        eq2_2 = self.join(splits, (1, 3, 5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq2_3 = self.join(splits, (2, 4, 5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq4 = self.join(splits, (6,), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq2and4 = VGroup(eq2_1, eq2_2, eq2_3, eq4)
        eq2and4.arrange(DOWN, center=False, aligned_edge=LEFT).scale(0.3).next_to(eq1, DOWN, aligned_edge=LEFT)
        select = lambda a: map(lambda x: splits[x], a)
        self.play(ReplacementTransform(VGroup(*select([0, 3, 4, 6])).copy(), eq2_1), FadeOut(pre_eq2[0]))
        self.play(ReplacementTransform(VGroup(*select([1, 3, 5, 6])).copy(), eq2_2), FadeOut(pre_eq2[1]))
        self.play(ReplacementTransform(VGroup(*select([2, 4, 5, 6])).copy(), eq2_3), FadeOut(pre_eq2[2]))
        self.play(ReplacementTransform(splits[6].copy(), eq4), FadeOut(pre_eq4))

        # 替换负项
        eq3_1 = self.join(splits, (3, 6), TexMobject("+").scale(2))
        eq3_2 = self.join(splits, (5, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq3_3 = self.join(splits, (4, 6), TexMobject("+").scale(2), left=TexMobject("+").scale(2))
        eq3 = VGroup(eq3_1, eq3_2, eq3_3).scale(0.3).arrange(DOWN).move_to(target_coord)
        pre_eq3_right.generate_target().next_to(eq3, direction=RIGHT, coor_mask=[1, 0, 1])
        self.play(MoveToTarget(pre_eq3_right))
        self.play(ReplacementTransform(VGroup(*select([3, 6])).copy(), eq3_1), FadeOut(pre_eq3[2]))
        self.play(ReplacementTransform(VGroup(*select([5, 6])).copy(), eq3_2), FadeOut(pre_eq3[3]))
        self.play(ReplacementTransform(VGroup(*select([4, 6])).copy(), eq3_3), FadeOut(pre_eq3[4]))
        self.wait()

        self.add_caption("我们再来看看等式左边")
        # fadeout 无关物件
        fadeout_group = VGroup(title, cline, df1, df2, sr)
        self.play(FadeOutAndShift(fadeout_group, UP), eq1.to_edge, UP)
        self.wait()

        # 加框
        self.add_caption("我们对这里所有的图形分为三类")
        sr1 = SurroundingRectangle(eq1[0:5], color=RED)
        sr2 = SurroundingRectangle(eq1[6:11], color=RED)
        sr3 = SurroundingRectangle(eq1[12], color=RED)
        self.play(ShowCreation(VGroup(sr1, sr2, sr3)))
        self.wait()

        # 显示下标文字
        self.add_caption("记为$I_1,I_2,I_3$")
        i1 = TexMobject("I_1", color=YELLOW).next_to(sr1, DOWN)
        i2 = TexMobject("I_2", color=YELLOW).next_to(sr2, DOWN)
        i3 = TexMobject("I_3", color=YELLOW).next_to(sr3, DOWN)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, DOWN), [i1, i2, i3]), lag_ratio=0.15))
        self.wait()
        self.add_caption("其中$I_i$中的图形仅属于i个集合的相交部分")
        self.add_caption("例如$I_1$中的任何一个图形，都只被唯一的一个集合包含")

        # 加框eq2 I_1
        self.add_caption("分类后我们再来看右边第一项")
        sr_eq2 = SurroundingRectangle(VGroup(eq2_1, eq2_2, eq2_3), color=YELLOW)
        self.play(ShowCreation(sr_eq2))
        self.wait()
        self.add_caption("注意到，$I_1$中的元素全部来自于这一项")
        sr_eq2_1 = SurroundingRectangle(eq2_1[0], color=YELLOW)
        sr_eq2_2 = SurroundingRectangle(eq2_2[1], color=YELLOW)
        sr_eq2_3 = SurroundingRectangle(eq2_3[1], color=YELLOW)
        self.play(ReplacementTransform(sr_eq2, VGroup(sr_eq2_1, sr_eq2_2, sr_eq2_3)))
        self.wait()

        # 移动 I_1
        self.add_caption("这很好地解释了为何他们前面的系数都是1")
        eq2_1[0].generate_target().next_to(eq1[0], DOWN).shift(DOWN * 0.7)
        eq2_2[1].generate_target().next_to(eq1[2], DOWN).shift(DOWN * 0.7)
        eq2_3[1].generate_target().next_to(eq1[4], DOWN).shift(DOWN)
        self.play(Uncreate(VGroup(sr_eq2_1, sr_eq2_2, sr_eq2_3)),
                  AnimationGroup(*map(MoveToTarget, [eq2_1[0], eq2_2[1], eq2_3[1]]), lag_ratio=0.1))
        self.wait()
        self.add_caption("我们把其他项整理一下")
        eq2_1[2].generate_target().next_to(eq1[6], DOWN).shift(DOWN * 0.8)
        eq2_1[4].generate_target().next_to(eq1[8], DOWN).shift(DOWN * 0.7)
        eq2_1[6].generate_target().next_to(eq1[12], DOWN).shift(DOWN * 0.7)
        eq2_2[3].generate_target().next_to(eq2_1[2].target, DOWN)
        eq2_2[5].generate_target().next_to(eq1[10], DOWN).shift(DOWN * 0.7)
        eq2_2[7].generate_target().next_to(eq2_1[6].target, DOWN)
        eq2_3[3].generate_target().next_to(eq2_1[4].target, DOWN)
        eq2_3[5].generate_target().next_to(eq2_2[5].target, DOWN)
        eq2_3[7].generate_target().next_to(eq2_2[7].target, DOWN)

        self.play(AnimationGroup(*map(MoveToTarget,
                                      (eq2_1[2], eq2_1[4], eq2_1[6],
                                       eq2_2[3], eq2_2[5], eq2_2[7],
                                       eq2_3[3], eq2_3[5], eq2_3[7])), lag_ratio=0.05))
        self.wait()

        # 移动第二项
        self.add_caption("接下来看第二项", wait_time=1)
        self.add_caption("处理完第一项后，$I_2$中的剩下的元素就都在第二项里了")
        sr_eq3_1 = SurroundingRectangle(eq3_1[0], color=YELLOW)
        sr_eq3_2 = SurroundingRectangle(eq3_2[1], color=YELLOW)
        sr_eq3_3 = SurroundingRectangle(eq3_3[1], color=YELLOW)
        self.play(ShowCreation(VGroup(sr_eq3_1, sr_eq3_2, sr_eq3_3)))
        self.wait()

        self.add_caption("注意这里是负号，就是为了抵消第一项中$I_2$中的重复元素", anim=(ShowPassingFlash(pre_eq3[0]),))
        eq3_1[0].generate_target().next_to(eq2_2[3], DOWN)
        eq3_2[1].generate_target().next_to(eq2_3[5], DOWN)
        eq3_3[1].generate_target().next_to(eq2_3[3], DOWN)
        self.play(AnimationGroup(*map(
            MoveToTarget, [eq3_1[0], eq3_2[1], eq3_3[1]]
        ), lag_ratio=0.05))
        grp_fo = VGroup(eq3_1[0], eq3_2[1], eq3_3[1],
                        eq2_2[3], eq2_3[5], eq2_3[3])
        sr_offset1 = SurroundingRectangle(grp_fo, color=BLUE)
        self.play(ShowCreation(sr_offset1))
        self.play(FadeOut(VGroup(sr_offset1, grp_fo)))
        self.wait()
        self.add_caption("这样$I_2$中的元素也相等了")

        self.add_caption("接下来是第二部分")
        i3_of_2 = VGroup(eq3_1[2], eq3_2[3], eq3_3[3])
        i3_of_2.generate_target().arrange(DOWN).next_to(eq2_2[7], RIGHT)
        self.play(MoveToTarget(i3_of_2))
        self.wait()
        self.add_caption("同理可以消除")
        fo_g2 = VGroup(i3_of_2, eq2_1[6], eq2_2[7], eq2_3[7])
        sr_offset2 = SurroundingRectangle(fo_g2, color=BLUE)
        self.play(ShowCreation(sr_offset2))
        self.play(FadeOut(VGroup(fo_g2, sr_offset2)))
        self.wait()
        self.add_caption("剩下的就是第三项了")
        eq4[1].generate_target().next_to(eq1[12], DOWN).shift(DOWN * 0.7)
        self.play(MoveToTarget(eq4[1]))

        self.add_caption("至此，左右完全相等，验证完毕")
        self.play(ShowCreationThenDestruction(SurroundingRectangle(VGroup(eq1[0], eq4[1], eq2_1[0]), color=BLUE)))
        self.fade_all_out()
        self.wait(3)

    @staticmethod
    def join(group, idxs, j, left=None, right=None):
        idxs = list(idxs)
        r_group = VGroup()
        if left:
            r_group.add(left)
        r_group.add(group[idxs[0]].copy())
        for i in range(1, len(idxs)):
            r_group.add(j.copy(), group[idxs[i]].copy())
        if right:
            r_group.add(right)
        r_group.arrange()
        return r_group


class P02(MyScene, GraphScene):  # 证明的前置知识
    CONFIG = {"axes_color": WHITE}

    def construct(self):
        c1 = Circle(radius=2, color=WHITE).shift(LEFT)
        c2 = Circle(radius=2, color=WHITE).shift(RIGHT)
        c3 = Circle(radius=2, color=WHITE).shift(1.5 * UP)
        cgroup = VGroup(c1, c2, c3)
        splits = set_split(mobs=cgroup,
                           case=[[1, 0, 0],  # 0
                                 [0, 1, 0],  # 1
                                 [0, 0, 1],  # 2
                                 [1, 1, 0],  # 3
                                 [1, 0, 1],  # 4
                                 [0, 1, 1],  # 5
                                 [1, 1, 1]],  # 6
                           color_list=[RED, GREEN, BLUE, ORANGE, PINK, LIGHT_BROWN, YELLOW])
        splits.add(cgroup)
        self.play(AnimationGroup(*map(Write, splits), lag_ratio=0.05), run_time=0.7)
        self.add_caption("我们对之前直观理解的思路，用严谨的语言表述")
        self.add_caption("就得到了证明的思路")
        splits.generate_target().scale(0.8).to_corner(DR)
        self.play(MoveToTarget(splits))

        self.add_caption("首先我们要明确证明中的图形在数学中的含义")
        eqwt = VGroup(splits[3].copy(), TexMobject("\\Leftrightarrow", color=RED).scale(2),
                      TexMobject("?", color=BLUE).scale(2)).arrange(RIGHT).to_corner(LEFT, buff=2)
        self.play(AnimationGroup(TransformFromCopy(splits[3], eqwt[0]), ShowCreation(eqwt[1:]), lag_ratio=0.5))
        self.wait()

        self.add_caption("直觉告诉我们这些图形分别指代着某个集合")
        self.add_caption("例如此处图形指的就是", "$(A_1\\cap A_2) \\setminus A_3$", color_setting_list=[(1, BLUE)])
        set_from_cpt = TexMobject("(A_1\\cap A_2) \\setminus A_3", color=BLUE
                                  ).next_to(eqwt[1], RIGHT).shift(RIGHT * 0.03)
        self.play(TransformFromCopy(self.cpt_mob[1], set_from_cpt), FadeOutAndShift(eqwt[2], UP))
        splits.save_state()
        self.play(ShowCreationThenDestruction(c1.copy().set_color(YELLOW)),
                  ShowCreationThenDestruction(c2.copy().set_color(YELLOW)))
        splits.generate_target()
        for i in [0, 1, 2, 4, 5]:
            splits.target[i].set_fill(opacity=0.1)
        self.add_caption("我们验证一下，首先是$A_1\\cap A_2$")
        self.play(MoveToTarget(splits))
        self.wait()
        self.add_caption("再和$A_3$做差", anim=[ShowCreationThenDestruction(c3.copy().set_color(YELLOW))])
        self.play(splits[6].set_fill, None, 0.1)
        self.wait()

        self.add_caption("根据我们多年用维恩图做题的经验，这是很合理的")
        eqnw = VGroup(eqwt[:2], set_from_cpt)
        self.play(eqnw.to_corner, UP, splits.restore)
        self.wait()

        self.add_caption("接下来的问题是，二者之间是什么关系结构怎样的？")
        self.add_caption("也就是说：这些集合是按何种方式划分的？")
        set_union = PolygonUnion(PolygonUnion(c1, c2), c3).set_color(BLUE).set_fill(BLUE, opacity=0.7)
        set_minus = PolygonSubtraction(PolygonUnion(c2, c3), c1).set_color(BLUE).set_fill(BLUE, opacity=0.7)
        cutacircle = VGroup(c1.copy().set_color(GREEN).set_fill(GREEN, opacity=0.7), set_minus)
        right_arrow = TexMobject("\\Rightarrow").scale(2).set_color(YELLOW).next_to(set_union, RIGHT)
        how = Text("How?").scale(0.6).set_color(RED).next_to(right_arrow, UP, buff=0.05)
        splits.generate_target().next_to(right_arrow)
        how_trsf = VGroup(set_union, how, right_arrow, splits.target).move_to(DOWN * 0.1)
        self.play(FadeInFrom(how_trsf[0:3], LEFT), MoveToTarget(splits), FadeOutAndShift(eqnw, UP))
        srt = SurroundingRectangle(how_trsf)
        self.play(ShowCreationThenDestruction(srt), run_time=1)
        self.wait(3)

        self.add_caption("从图形来理解，我们是用三个圆进行的划分")
        self.play(AnimationGroup(
            *map(ShowCreationThenDestruction, [a.copy().set_color(YELLOW) for a in [c1, c2, c3]]), lag_ratio=0.25
        ), run_time=2)
        self.add_caption("考虑其中的一个圆", wait_time=1)
        cutacircle.move_to(set_union)
        self.play(FadeOut(set_union), FadeIn(cutacircle))
        self.wait()
        self.add_caption("整个图形被它分割为内外两个部分")
        nei = TextMobject("内").move_to(cutacircle[0])
        wai = TextMobject("外").move_to(cutacircle[1]).shift(UR * 0.5)
        self.play(ShowCreation(nei), ShowCreation(wai))
        self.wait()
        self.add_caption("用集合表示就是$A_1$以及它的补集")
        set_a = TexMobject("A_1").move_to(nei)
        set_ac = TexMobject("A_1^c").move_to(wai)
        self.play(Transform(nei, set_a), Transform(wai, set_ac))
        self.wait(2)

        self.add_caption("它们可以分别表示成：")
        wai_set = TexMobject("\\{x|x\\notin A_1\\}", color=BLUE).to_corner(UP)
        nei_set = TexMobject("\\{x|x\\in A_1\\}", color=GREEN).next_to(self.cpt_mob, UP)
        wai_arr = Arrow(start=wai.get_edge_center(UP), end=wai_set.get_edge_center(DOWN), color=BLUE)
        nei_arr = Arrow(start=nei.get_edge_center(DOWN), end=nei_set.get_edge_center(UP), color=GREEN)
        self.play(AnimationGroup(ShowCreation(wai_arr), Write(wai_set), lag_ratio=0.5))
        self.play(AnimationGroup(ShowCreation(nei_arr), Write(nei_set), lag_ratio=0.5))
        self.wait()

        self.add_caption("我们确定分割后集合的依据是：", "元素$x$是否在$A_1$中", color_setting_list=[(1, YELLOW)])
        self.play(Indicate(wai_set[0][4:6]), Indicate(nei_set[0][4]))
        self.add_caption("受此启发我们来看多个集合的情况")
        self.play(FadeOut(VGroup(cutacircle, how, right_arrow, splits, nei, wai, nei_arr, wai_arr, nei_set, wai_set)))
        self.add_caption("以三个的情况为例，我们不妨找找规律")
        equal = TexMobject("=").scale(2).shift(LEFT * 2.5)
        splits.to_corner(DR)
        self.play(FadeInFrom(splits, DOWN), ShowCreation(equal))
        self.wait()
        relation = ((0, "A_1\\setminus (A_2 \\cup A_3)", (1, 0, 0)),
                    (1, "A_2\\setminus (A_1 \\cup A_3)", (0, 1, 0)),
                    (2, "A_3\\setminus (A_1 \\cup A_2)", (0, 0, 1)),
                    (3, "(A_1\\cap A_2)\\setminus A_3", (1, 1, 0)),
                    (4, "(A_1\\cap A_3)\\setminus A_2", (1, 0, 1)),
                    (5, "(A_2\\cap A_3)\\setminus A_1", (0, 1, 1)),
                    (6, "A_1\\cap A_2\\cap A_3", (1, 1, 1)))

        pl = equal.get_center() + LEFT * 2.2
        pr = pl + RIGHT * 4.8
        odin = TexMobject("\\in", color=BLUE)
        odnotin = TexMobject("\\notin", color=YELLOW)

        for idx, tex, case in relation:
            if idx == 0:
                left_mob = splits[idx].copy().move_to(pl)
                right_mob = TexMobject(tex, color=left_mob.get_color()).move_to(pr)
                self.play(Indicate(splits[idx]), run_time=0.5)
                self.play(ShowCreation(left_mob), ShowCreation(right_mob))
                self.wait(2)
            else:
                lm = splits[idx].copy().move_to(pl)
                rm = TexMobject(tex, color=lm.get_color()).move_to(pr)
                self.play(Indicate(splits[idx]), run_time=0.5)
                anim = []
                for i in range(3):
                    if case[i] == 1:
                        od = odin.copy()
                    else:
                        od = odnotin.copy()
                    od.move_to(case_of_sets[i][1].get_center())
                    anim.append(Transform(case_of_sets[i][1], od))
                    case_of_sets[i][0].set_color(lm.get_color())
                self.play(Transform(left_mob, lm), Transform(right_mob, rm), *anim)
                self.wait(2)
            if idx == 0:
                self.add_caption("来看看这个集合(记为$S$)在$A_1\\sim A_3$里的分布情况")
                case_of_sets = VGroup(TexMobject("S", "\\in", "A_1"),
                                      TexMobject("S", "\\notin", "A_2"),
                                      TexMobject("S", "\\notin", "A_3")). \
                    arrange(RIGHT, buff=1).next_to(equal, DOWN, buff=1.6).shift(0.2 * RIGHT)
                for mob in case_of_sets:
                    mob.set_color_by_tex_to_color_map({"S": RED, "\\in": BLUE, "not": YELLOW})
                self.play(AnimationGroup(*map(Write, case_of_sets), lag_ratio=0.1), run_time=1.3)
                self.wait()
                self.add_caption("注意观察属于关系与集合表示")

        self.add_caption("我们不难发现，这其中的规律可以概括为：")
        law = TextMobject("图形代表的集合", "=", "$\\bigcap $包含该图形的集合", "$\\setminus $", "$\\bigcup $ 不包含该图形的结合")
        law[2].next_to(law[0], DOWN, aligned_edge=LEFT)
        law[4].next_to(law[2], DOWN, aligned_edge=LEFT)
        law[1].next_to(law[2], LEFT)
        law[3].next_to(law[4], LEFT)
        law.set_color_by_tex_to_color_map({"图形": RED, "包含该图形的集合": GREEN, "不包含": BLUE}).move_to(LEFT)
        self.play(FadeOutAndShift(VGroup(equal, left_mob, right_mob, case_of_sets)), AnimationGroup(
            *map(lambda a: FadeInFrom(a, DOWN), [law[0], law[1:3], law[3:]]), lag_ratio=0.8
        ), run_time=2.5)
        # self.play(ReplacementTransform(VGroup(equal, left_mob, right_mob), law))
        self.wait(3)

        self.add_caption("这样的表示似乎不是很方便")
        self.add_caption("因此我们考虑用一种简易的方式表示")
        self.play(FadeOutAndShift(law, UP))
        self.wait()
        self.add_caption("我们类比平面上点的坐标表示")
        self.setup_axes(animate=False)
        self.axes.scale(0.7).move_to(DOWN * 0.9 + LEFT * 2)
        self.play(ShowCreation(self.axes))
        point = Dot(self.coords_to_point(5, 6), color=YELLOW)
        self.play(ShowCreation(point))

        self.add_caption("我们取了x坐标与y坐标，组成一个向量")
        vline = Line(self.coords_to_point(5, 0), point.get_center(), color=BLUE, buff=0.1)
        cline = Line(self.coords_to_point(0, 6), point.get_center(), color=BLUE, buff=0.1)
        self.play(ShowCreation(VGroup(vline, cline)))
        coord = TexMobject("(5, 6)", color=RED).next_to(point, UR)
        self.play(ShowCreation(coord))
        self.wait()
        self.add_caption("这个点就这样由两个分量组成的坐标完全决定")
        self.add_caption("于是我们就可以通过研究坐标来研究平面上的点")
        lra = TexMobject("\\Leftrightarrow").next_to(point, RIGHT)
        coord.generate_target().next_to(lra, RIGHT)
        self.play(ShowCreation(lra), MoveToTarget(coord))
        self.play(ShowCreationThenDestruction(
            SurroundingRectangle(VGroup(point, lra, coord), color=YELLOW).scale(1.2)), run_time=0.6)
        self.wait()
        self.add_caption("所以我们也来类似地定义一个坐标")
        self.play(FadeOut(VGroup(cline, vline, coord, point, self.axes, lra)))
        self.wait()

        general_vector = ListTex("i_1", "i_2", "\\cdots", "i_n",
                                 sep=",", brace="()", color_list=[(2, YELLOW)]).to_corner(UP)
        df = TexMobject("i_k\\in \\{0,1\\}(k=1,2,\\cdots,n)", color=GREY).next_to(general_vector)
        general_df = VGroup(general_vector, df).move_to(ORIGIN, coor_mask=[1, 0, 0])
        self.play(ShowCreation(general_vector))
        self.play(Write(df))
        self.wait()

        self.add_caption("第i个分量值为1代表这个集合被$A_i$包含", anim=[Indicate(df[0][6])])
        self.add_caption("为0则表示不包含", anim=[Indicate(df[0][4])])
        udarr = TexMobject("\\Leftrightarrow", color=YELLOW).rotate(PI / 2).next_to(general_vector, DOWN)
        general_set = TexMobject("\\bigcap_{i_k=1}A_{i_k}", "\\setminus", "\\bigcup_{i_k=0}A_{i_k}"
                                 ).next_to(udarr, DOWN).align_to(general_df, LEFT)
        general_set[0].set_color(BLUE)
        general_set[2].set_color(RED)
        self.add_caption("我们就用这个坐标来代表对应的集合")
        self.play(ShowCreation(general_set), ShowCreation(udarr))
        self.wait()

        self.add_caption("在此定义下，我们容易验证以下成立")
        prpt = VGroup(*map(TextMobject, ["1.这样的集合一共有$2^n-1$个",
                                         "2.不同的集合互不相交",
                                         "3.全集中的任何一个元素都包含在某个集合中",
                                         "4.以n=3为例，我们的分割方法完美符合先前的演示"]
                           )).arrange(DOWN, aligned_edge=LEFT).next_to(general_set, DOWN).to_edge(LEFT)

        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, LEFT), [prpt[i] for i in range(4)]), lag_ratio=1),
                  FadeOutAndShift(splits, RIGHT), run_time=4)
        self.wait(4)
        allmob = VGroup(general_vector, df, udarr, general_set, prpt)
        allmob.save_state()
        self.play(ShrinkToCenter(allmob))
        allmob.restore()
        self.remove(allmob)

        self.add_caption("终于,我们将之前的图像转化成了严谨的集合表示", wait_time=0.5)
        eg = splits[3].copy().move_to(ORIGIN).to_edge(UP)
        udarr.next_to(eg, DOWN)
        eg_set = TexMobject("(A_1\\cap A_2)\\setminus A_3", color=BLUE).next_to(udarr, DOWN)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, UP), [eg, udarr, eg_set]), lag_ratio=0.2), run_time=1.6)

        self.add_caption("让我们可以通过数学语言证明这个等式")
        darr = TexMobject("\\Leftarrow", color=RED).rotate(PI / 2).next_to(eg_set, DOWN)
        len_eg_set = TexMobject("|", "(A_1\\cap A_2)\\setminus A_3", "|",
                                color=YELLOW).move_to(ORIGIN).next_to(darr, DOWN)
        len_eg_set[1].set_color(BLUE)
        darr2 = darr.copy().next_to(len_eg_set, DOWN)
        res = TexMobject("\\left|\\bigcup_{i=1}^{n}A_i\\right|",  # 0
                         "=",  # 1
                         "\\sum_{k=1}^{n}",  # 2
                         "(-1)^{k-1}",  # 3
                         "\\sum_{1\\le i_1 < \\cdots < i_k \\le n}",  # 4
                         "|A_{i_1}\\cap \\cdots \\cap A_{i_k}|").scale(0.8).next_to(darr2, DOWN)  # 5
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, UP), [darr, len_eg_set]), lag_ratio=0.15), run_time=1.3)
        self.play(AnimationGroup(*map(lambda a: FadeInFrom(a, UP), [darr2, res]), lag_ratio=0.15), run_time=1.3)
        self.play(ShowCreationThenDestruction(SurroundingRectangle(res, color=YELLOW)), run_time=1)
        self.wait()

        self.add_caption("同时，为了方便证明，我们合理地引入了坐标")
        coord_of3 = TexMobject("(1, 1, 0)")
        left_coord = VGroup(coord_of3, TexMobject("\\Leftrightarrow", color=RED)
                            ).arrange(RIGHT).next_to(eg_set, LEFT)
        self.play(FadeInFrom(left_coord, LEFT))
        self.wait()
        self.add_caption("放弃冗长的集合表示，这会使得后续证明更加方便")
        self.play(VGroup(left_coord, eg_set).shift, eg_set.get_center() - coord_of3.get_center())
        self.play(Uncreate(VGroup(left_coord[1], eg_set)))
        self.wait()

        self.add_caption("至此，思路理清了，可以开始证明了")
        self.play(FadeOut(VGroup(eg, eg_set, len_eg_set, udarr, darr, darr2, coord_of3)), res.to_edge, UP)
        self.wait(1)


class P03(MyScene):  # 正式的证明
    def construct(self):
        res = TexMobject("\\left|\\bigcup_{i=1}^{n}A_i\\right|",  # 0
                         "=",  # 1
                         "\\sum_{k=1}^{n}",  # 2
                         "(-1)^{k-1}",  # 3
                         "\\sum_{1\\le i_1 < \\cdots < i_k \\le n}",  # 4
                         "|A_{i_1}\\cap \\cdots \\cap A_{i_k}|").scale(0.8).to_edge(UP)  # 5
        self.add(res)
        self.wait()

        self.add_caption("此前先明确几个表示方法：")
        general_vector = ListTex("i_1", "i_2", "\\cdots", "i_n",
                                 sep=",", brace="()", color_list=[(2, YELLOW)]).next_to(res, DOWN)
        rarr = TexMobject("\\Rightarrow", color=YELLOW)
        p = TexMobject("P", color=BLUE)
        rarr2 = rarr.copy()
        aset = TexMobject("S", color=BLUE)
        rarr3 = rarr.copy()
        len_aset = TexMobject("|", "S", "|", color=RED)
        len_aset[1].set_color(BLUE)
        process = VGroup(p, rarr, general_vector, rarr2, aset, rarr3, len_aset).scale(1.2).arrange(RIGHT)
        cpts = ["我们用P来指代某个坐标", "从坐标出发得到集合", "进而得到集合的模长用于证明"]
        for i in range(1, 4):
            self.add_caption(cpts[i - 1])
            if i == 1:
                self.play(AnimationGroup(
                    GrowFromCenter(p), ShowCreation(process[2 * i - 1]), Write(process[2 * i]), lag_ratio=0.1),
                    run_tim=1.3)
            else:
                self.play(AnimationGroup(
                    ShowCreation(process[2 * i - 1]), Write(process[2 * i]), lag_ratio=0.1
                ), run_time=1.2)
        proof_vec = rarr.copy().rotate(PI / 2).scale(2).move_to(np.array([
            len_aset.get_x(), 0.5 * (len_aset.get_y() + res.get_y()), 0]))
        self.play(ShowCreation(proof_vec))
        self.wait(3)
        self.add_caption("因此我们在证明过程中用的坐标P，本质上表示的是模长", wait_time=3)
        left_process = VGroup(p, rarr2, len_aset)
        left_process.generate_target().arrange(RIGHT).move_to(ORIGIN)
        fade_process = VGroup(rarr, general_vector, aset, rarr3)
        self.play(FadeOutAndShift(fade_process, DOWN), MoveToTarget(left_process), FadeOut(proof_vec))
        self.play(left_process.next_to, res, DOWN, 1)
        self.wait()

        self.add_caption("另外我们引入几个符号用于简记")
        index_symbol = TexMobject("P", "[", "k", "]").set_color_by_tex_to_color_map({
            "P": BLUE, "[": YELLOW, "]": YELLOW, "k": RED}).next_to(left_process, DOWN, buff=0.5).to_edge(LEFT)
        sum_symbol = TexMobject("\\mathrm{Sum}", "(", "P", ")").next_to(index_symbol, DOWN, buff=0.5).to_edge(LEFT) \
            .set_color_by_tex_to_color_map({"sum": RED, "P": BLUE, "(": YELLOW, ")": YELLOW})
        index_description = TextMobject("表示坐标$P$的第$k$个分量$i_k$的值").next_to(index_symbol, RIGHT, buff=1.5)
        sum_description = TextMobject("表示坐标中1的个数，也就是$\\sum_{k=1}^{n}P[k]$"
                                      ).next_to(index_description, DOWN, buff=0.5).align_to(index_description, LEFT)
        self.play(ShowCreation(index_symbol))
        self.play(Write(index_description))
        self.play(ShowCreation(sum_symbol))
        self.play(Write(sum_description))
        self.wait(3)

        srd_res = SurroundingRectangle(res, color=YELLOW)
        self.add_caption("由此，我们正式开始证明")
        self.play(*map(FadeOut, (left_process, index_description, index_symbol, sum_symbol, sum_description)),
                  ShowCreation(srd_res))
        self.wait()

        left_srd = SurroundingRectangle(res[0], color=YELLOW)
        self.add_caption("先看等式左边", anim=(Transform(srd_res, left_srd),))
        self.add_caption("左边就是全集的模长，全体$P$的模长之和")
        udarr = TexMobject("\\Leftrightarrow", color=RED).rotate(PI / 2).next_to(res[0], DOWN)
        all_sub = TexMobject("\\sum", "P").set_color_by_tex_to_color_map({
            "sum": RED, "P": BLUE
        }).scale(0.8).next_to(udarr, DOWN)
        self.play(FadeInFrom(udarr, UP), FadeInFrom(all_sub, UP))
        self.wait()

        self.add_caption("我们按照$\\mathrm{Sum(P)}$的不同值进行分类")
        number_axis = VGroup(*[TexMobject(i) for i in ("1", "2", "\\vdots", "k", "\\vdots", "n")]
                             ).arrange(DOWN, buff=0.4).next_to(all_sub, DOWN, buff=0.5). \
            next_to(res, DOWN, buff=0.5).next_to(all_sub, RIGHT, coor_mask=np.array([1, 0, 0])).shift(RIGHT)
        lefteq = VGroup(sum_symbol, TexMobject("=")).arrange(RIGHT).next_to(number_axis, LEFT).shift(0.25 * LEFT)
        lbrace = TexMobject("\\{\\}")[0][0].set_height(number_axis.get_height(), stretch=True).next_to(lefteq, RIGHT)
        self.play(FadeInFrom(number_axis, LEFT), ShowCreation(lefteq), ShowCreation(lbrace))
        udarr2 = udarr.copy().move_to_mid(all_sub, lefteq[0]).move_to(udarr, coor_mask=[1, 0, 0])
        self.play(ShowCreation(udarr2))
        self.wait()

        self.add_caption("从每一类中取出一个代表")
        representative = ["(1, 0, \\cdots, 0)", "(1, 1, 0, \\cdots, 0)",
                          "(1, \\cdots, 1, 0, \\cdots, 0)", "(1, 1, \\cdots, 1)"]
        rep_tex = VGroup()
        to_list = VGroup()
        to = TexMobject("\\to", color=RED)
        for i in [0, 1, 3, 5]:
            tex = TexMobject(representative.pop(0), color=BLUE).next_to(number_axis[i], RIGHT, buff=1.5)
            rep_tex.add(tex)
            t = to.copy().move_to_mid(number_axis[i], tex[0][0])
            to_list.add(t)
            self.play(Write(tex), ShowCreation(t), run_time=0.5)
        dsp = TextMobject("此处为第$k$个$1$", color=RED).scale(0.6).next_to(
            rep_tex[2][0][7], DOWN, buff=0.3).shift(0.5 * RIGHT)
        self.play(rep_tex[2][0][7].set_color, YELLOW, ShowCreation(dsp))
        self.wait()

        self.add_caption("我们再来分析右边的集合")
        self.play(Uncreate(VGroup(number_axis, udarr, all_sub, lefteq, lbrace, udarr2, to_list, dsp)))
        self.play(rep_tex.to_edge, LEFT, 1)
        self.wait()

        self.add_caption("首先面临的问题就是，这些交集是什么东西？")
        right_srd = SurroundingRectangle(res[2:], color=YELLOW)
        qst = TexMobject("?", color=RED).scale(2).next_to(right_srd)
        self.play(AnimationGroup(
            Transform(srd_res, right_srd), FadeInFrom(qst, DOWN), lag_ratio=0.2), run_time=1.2)
        self.wait()

        self.add_caption("我们拿几个简单的来看看到底是什么情况")
        apart_line = Line(rep_tex.get_edge_center(UR), rep_tex.get_edge_center(DR), color=GREY).shift(0.2 * RIGHT)
        eg_of_right1 = TexMobject("A_1")
        eg_of_right2 = TexMobject("A_1\\cap A_2")
        eg_of_right3 = TexMobject("A_1\\cap A_2\\cap A_3")
        eor = VGroup(eg_of_right1, eg_of_right2, eg_of_right3).arrange(
            DOWN, buff=1, aligned_edge=LEFT).next_to(apart_line, RIGHT)

        self.play(ShowCreation(eor), ShowCreation(apart_line))
        self.wait(2)

        self.add_caption("第一个很简单，就是所有包含于$A_1$的集合", anim=[Indicate(eg_of_right1)])
        self.add_caption("也就是$P[1]=1$，其他位置无任何要求")
        aswof1 = TexMobject("\\Leftrightarrow", "\\{P|P[1]=1\\}", color=BLUE
                            ).next_to(eg_of_right1, RIGHT)
        aswof2 = TexMobject("\\Leftrightarrow", "\\{P|P[1\\sim 2]=1\\}", color=BLUE
                            ).next_to(eg_of_right2, RIGHT)
        aswof3 = TexMobject("\\Leftrightarrow", "\\{P|P[1\\sim 3]=1\\}", color=BLUE
                            ).next_to(eg_of_right3, RIGHT)
        asws = VGroup(aswof1, aswof2, aswof3)
        for i in range(3):
            asws[i][0].set_color(YELLOW)
            if i == 0:
                asws[i][1][-5:-4].set_color(RED)
            else:
                asws[i][1][-7:-4].set_color(RED)
        self.play(Write(aswof1))
        self.wait()
        self.add_caption("第二个涉及两个集合的交集，也是类似", anim=[Indicate(eg_of_right2)], wait_time=1)
        self.add_caption("只要前两位是1，即可保证")
        self.play(Write(aswof2))
        self.wait()
        self.add_caption("第三个也是同理", anim=[Indicate(eg_of_right3)])
        self.play(Write(aswof3))
        self.wait()

        self.add_caption("由此我们不难得出以下性质：", anim=[FadeOut(qst)])
        self.play(AnimationGroup(*map(lambda a: FadeOutAndShift(a, RIGHT), (*eor, *asws)), lag_ratio=0.1), run_time=1.6)
        cap_poperty = TexMobject("\\forall P\\in", "S", ":", "\\bigcap_{i=1}^{k}", "A_i").set_color_by_tex_to_color_map(
            {"P": BLUE, "S": RED, "A_i": YELLOW}
        ).next_to(res, DOWN).next_to(apart_line, RIGHT, coor_mask=[1, 0, 0], buff=1)
        self.add_caption("对$k$个集合的交集而言", anim=[ShowCreation(cap_poperty)])
        self.wait()

        self.add_caption("由于至少有k个位置为1，因此：")
        pt1 = TexMobject("(1):\\mathrm{Sum}(", "P", ")\\ge", "k").set_color_by_tex_to_color_map(
            {"P": BLUE, "k": YELLOW}).next_to(cap_poperty, DOWN).next_to(apart_line, RIGHT, coor_mask=[1, 0, 0])
        self.play(Write(pt1))
        self.wait()

        self.add_caption("另外，关于集合$S$的组成：")
        pt2 = TextMobject("(2):这样的", "$P$", "一共有", "$2^{n-k}$", "个").set_color_by_tex_to_color_map(
            {"P": BLUE, "2^": YELLOW}).next_to(pt1, DOWN).next_to(apart_line, RIGHT, coor_mask=[1, 0, 0])
        self.play(Write(pt2))
        self.wait()

        self.add_caption("又由于这些$P$互不相交，于是有：")
        pt3 = TexMobject("(3):", "S", "=\\sum_{i=1}^{2^{n-k}}", "P_i").set_color_by_tex_to_color_map(
            {"S": RED, "P": BLUE}).next_to(pt2, DOWN).next_to(apart_line, RIGHT, coor_mask=[1, 0, 0])
        self.play(Write(pt3))
        self.wait()

        self.add_caption("理解这些后就可以开始正式分析了")
        self.play(*map(Uncreate, (pt1, pt2, pt3, apart_line, cap_poperty)))

        self.add_caption("我们拿出左边第一个代表，它在左边仅出现一次")
        rpt1 = rep_tex[0]
        p1 = TexMobject("P_1", "=").set_color_by_tex_to_color_map({"P": BLUE, "=": YELLOW})
        ptex1 = VGroup(p1, rpt1.copy()).arrange(RIGHT)
        self.play(FadeOutAndShift(rep_tex[1:], LEFT), ReplacementTransform(rpt1, ptex1[1]), ShowCreation(ptex1[0]))
        self.wait()

        self.add_caption("于是我们统计右边出现的次数")
        count = TexMobject("\\mathrm{Count}", "=", "0").set_color_by_tex_to_color_map(
            {"Count": BLUE, "0": YELLOW}).next_to(res[-1], DOWN, buff=1)
        count_bak = count.copy()
        self.play(Write(count), ptex1.to_edge, LEFT)

        self.crosses = VGroup()

        def cross_anim(mob):
            cr1 = Line(mob.get_edge_center(UL), mob.get_edge_center(DR), color=RED)
            cr2 = Line(mob.get_edge_center(UR), mob.get_edge_center(DL), color=RED)
            self.crosses.add(VGroup(cr1, cr2))
            return AnimationGroup(ShowCreation(cr1), ShowCreation(cr2), lag_ratio=0.2)

        self.add_caption("由于$k$个集合的交集中的元素$Sum(P)$至少为k")
        self.add_caption("因此我们就按相交的集合个数进行分类")

        cps1 = VGroup(*map(TexMobject, ("|A_1|", "|A_2|", "\\vdots", "|A_n|"))).arrange(DOWN, buff=0.5)
        br1 = Brace(cps1, LEFT, color=YELLOW)
        cap1 = TexMobject("\\sum", "|A_i|").set_color_by_tex_to_color_map(
            {"sum": RED, "A": BLUE}).next_to(br1, LEFT)
        all1 = VGroup(cap1, br1, cps1).to_edge(RIGHT, buff=2.5).shift(DOWN * 1.5)

        self.add_caption("先看一个集合的交集", wait_time=1)
        self.play(Write(cap1))
        self.wait()
        self.add_caption("它包含$n$个集合，分别为：")
        self.play(GrowFromCenter(br1), *map(Write, cps1))
        self.wait()

        self.add_caption("我们根据坐标的含义就可以判断")
        self.play(AnimationGroup(
            *map(Indicate, (ptex1[1][0][1], ptex1[1][0][3], ptex1[1][0][9])), lag_ratio=0.1), run_time=1.3)
        self.wait()

        srdset = SurroundingRectangle(cps1[0], color=YELLOW).scale(1.1)
        self.add_caption("这些集合只有一个包含了$P$", anim=[ShowCreation(srdset), ptex1[1][0][1].set_color, YELLOW])
        self.play(*map(cross_anim, (cps1[1], cps1[3])))
        self.add_caption("因此这部分中只含有左边集合的一项")
        num0 = count[2]
        num1 = TexMobject("1", color=YELLOW).move_to(num0)
        self.play(FadeOutAndShift(num0, UP), FadeInFrom(num1, DOWN))
        count = VGroup(count[:2], num1)
        self.wait()

        second_set = TexMobject("\\sum", "|A_{i_1}\\cap A_{i_2}|").set_color_by_tex_to_color_map(
            {"sum": YELLOW, "A_": BLUE}).move_to(all1).shift(UP * 0.5).scale(1.5)
        self.add_caption("再来看右边的集合的下一项", wait_time=1)
        self.play(ShrinkToCenter(VGroup(all1, srdset, self.crosses)), GrowFromCenter(second_set))
        self.wait()

        self.add_caption("注意到这是两个集合的交集，根据性质我们有：")
        poperty_of_two_sets = TexMobject("\\mathrm{Sum}(", "P", ")\\ge", "2").set_color_by_tex_to_color_map(
            {"P": BLUE, "2": YELLOW}).next_to(second_set, DOWN)
        self.play(Write(poperty_of_two_sets))
        self.wait()
        self.add_caption("而左边的集合$\\mathrm{Sum}(P)=1$")
        poperty_of_left_set = TexMobject("\\mathrm{Sum}(", "P", ")=", "1", "\\neq 2").set_color_by_tex_to_color_map(
            {"P": BLUE, "1": RED, "2": YELLOW}).next_to(ptex1, DOWN)
        self.play(TransformFromCopy(self.cpt_mob, poperty_of_left_set))
        self.wait()

        self.crosses = VGroup()
        self.add_caption("因此，这些集合中绝不可能含有左边的代表", wait_time=1)
        self.play(cross_anim(VGroup(poperty_of_two_sets, second_set)))
        self.wait()
        self.add_caption("两个集合交集不行，后面的就更不用说了")
        self.add_caption("因此我们得到了左边代表在右侧的个数")
        count.generate_target().move_to(self.crosses).move_to(ptex1, coor_mask=[0, 1, 0])
        self.play(ShowCreationThenDestruction(SurroundingRectangle(count, color=YELLOW)))
        self.play(FadeOut(VGroup(
            poperty_of_two_sets, self.crosses, second_set, poperty_of_left_set)), MoveToTarget(count))
        self.add_caption("左右相等，我们成功地验证了一部分")
        first_part_end = VGroup(ptex1, TexMobject("\\Leftrightarrow").scale(2), count)
        first_part_end[1].move_to(FRAME_HEIGHT / 2 * DOWN + DOWN)
        first_part_end.generate_target()[1].scale(0.66)
        first_part_end.target.arrange(RIGHT, buff=0.5).move_to(ORIGIN)
        self.play(MoveToTarget(first_part_end))

        self.add_caption("另外，虽然我们只验证了左边的一个代表")
        self.add_caption("但实际上由于对称性，对所有$Sum(P)=1$的集合都是成立的")
        sump1_sets = ("(0, 1, \\cdots, 0)", "\\cdots", "(0, 0, \\cdots, 1)")
        first = True
        for sump1_str in sump1_sets:
            if first:
                fadein_tex = TexMobject(sump1_str, color=BLUE).move_to(ptex1[1])
                self.play(FadeInFrom(fadein_tex, DOWN), FadeOutAndShift(ptex1[1], UP))
                first = False
            else:
                to_fadein_tex = TexMobject(sump1_str, color=BLUE).move_to(ptex1[1])
                self.play(FadeInFrom(to_fadein_tex, DOWN), FadeOutAndShift(fadein_tex, UP))
                fadein_tex = to_fadein_tex
        self.wait()

        self.add_caption("验证了第一类后，接下来看第二类")
        self.play(FadeOut(first_part_end[1]), FadeOut(count), VGroup(ptex1[0], fadein_tex).shift, LEFT * 2)
        p2_and_coord = VGroup(TexMobject("P_2", color=BLUE), TexMobject("="), rep_tex[1]
                              ).arrange(RIGHT).move_to(ptex1, aligned_edge=LEFT)
        self.play(FadeOutAndShift(ptex1[0], UP), FadeOutAndShift(fadein_tex, UP), FadeInFrom(p2_and_coord, DOWN))
        self.wait()

        self.add_caption("它的$Sum(P)=2$")
        sump2 = TexMobject("\\mathrm{Sum}(", "P", ")=", "2").set_color_by_tex_to_color_map(
            {"p": BLUE, "2": RED}).next_to(p2_and_coord, DOWN)
        self.play(Write(sump2))
        self.add_caption("因此，我们只需考虑右边的两项")
        # self.play(VGroup(sump2, p2_and_coord).shift, LEFT * 2)
        apart_line = Line(rep_tex.get_edge_center(UR) + UP, rep_tex.get_edge_center(DR), color=GREY
                          ).next_to(p2_and_coord, RIGHT, buff=0.8, coor_mask=[1, 0, 0])
        count = count_bak.copy()
        self.play(ShowCreation(apart_line), Write(count))
        self.wait()

        first_part = VGroup(*map(TexMobject, ("|A_1|", "|A_2|", "\\cdots", "|A_n|"))).arrange(RIGHT, buff=0.7)
        second_part = VGroup(*map(TexMobject, ("|A_1\\cap A_2|", "\\cdots", "|A_{n-1}\\cap A_n|"
                                               ))).arrange(RIGHT, buff=0.5).next_to(first_part, DOWN, buff=1)
        whole_two_parts = VGroup(first_part, second_part).next_to(apart_line)
        self.play(*map(ShowCreation, first_part))
        self.wait()
        sr_group = VGroup(SurroundingRectangle(first_part[0]), SurroundingRectangle(first_part[1]))
        self.add_caption("第一项中显然只有前两项是符合要求的", anim=(
            ShowCreation(sr_group[0]), ShowCreation(sr_group[1])))
        num2 = TexMobject("2", color=YELLOW).next_to(count[1], RIGHT)
        self.play(FadeOutAndShift(count[2], UP), FadeInFrom(num2, DOWN))
        self.wait()

        self.play(*map(ShowCreation, second_part))
        sr_group.add(SurroundingRectangle(second_part[0]))
        self.add_caption("第二项也很明显只有一个", anim=(ShowCreation(sr_group[2]),))
        neg_hint_srd = SurroundingRectangle(res[3], color=YELLOW)
        self.add_caption("注意此处有一个负号", anim=(ReplacementTransform(srd_res, neg_hint_srd),))
        self.add_caption("因此$\\mathrm{Count}$应该减去1")
        count_minus1 = TexMobject("-1", color=RED).next_to(count, RIGHT).shift(DOWN * 0.05)
        self.play(Write(count_minus1))
        minus_result = num1.next_to(count[1], RIGHT)
        self.play(ReplacementTransform(VGroup(num2, count_minus1), minus_result))
        self.wait()

        count = VGroup(count[0:2], minus_result)
        self.add_caption("接下来看看一般情况")
        everythiing = VGroup(whole_two_parts, sr_group, neg_hint_srd, apart_line)
        self.play(FadeOut(everythiing), FadeOutAndShift(count[1], UP), count[0].shift, 8 * LEFT)

        pk = VGroup(TexMobject("P_k", "=", "(1, \\cdots, 1, 0, \\cdots, 0)").set_color_by_tex_to_color_map(
            {"P": BLUE, "cdots": BLUE}),
            TexMobject("\\mathrm{Sum}(", "P_k", ")", "=", "k").set_color_by_tex_to_color_map(
                {"k": YELLOW, "P": BLUE})).arrange(RIGHT, buff=1).shift(0.5 * UP)
        self.play(ReplacementTransform(VGroup(p2_and_coord, sump2), pk))
        self.wait()

        self.add_caption("对此我们考虑右边的k项")
        self.add_caption("实际上，对于若干个(l个)集合的交集：")
        cap_of_many = TexMobject("\\bigcap_lA_i:", "P", "[i_1,\\cdots, i_l]=", "1").set_color_by_tex_to_color_map(
            {"big": RED, "P": BLUE, "1": YELLOW, "i_l": WHITE}).next_to(pk, DOWN)
        self.play(Write(cap_of_many))
        self.wait()
        self.add_caption("我们只需保证这些下标都在前k个位置里")
        all_in_k = TexMobject("1", "\\le", "i_1,\\cdots, i_l", "\\le", "k").set_color_by_tex_to_color_map(
            {"le": YELLOW, "cdots": BLUE}).next_to(cap_of_many, DOWN).shift(UP * 0.3)
        self.play(Write(all_in_k))
        self.wait()
        self.add_caption("就一定能在其中找到$P_k$")
        res_k = TexMobject("P_k", "\\in", "\\bigcap_lA_i").set_color_by_tex_to_color_map({
            "P": BLUE, "big": RED}).next_to(all_in_k, DOWN)
        self.play(Write(res_k))
        self.wait()

        self.add_caption("因此对l个集合的交集，不难得出包含$P_k$的集合个数")
        srd = SurroundingRectangle(all_in_k, color=YELLOW)
        self.play(ShowCreation(srd))
        self.play(FadeOut(VGroup(cap_of_many, res_k)), Uncreate(srd))
        self.play(all_in_k.move_to, cap_of_many.get_center())
        self.wait()
        self.add_caption("任何从前$k$项中选择$l$项的交集都会包含$P$")
        self.add_caption("因此总的个数就是$\\mathrm{C}_k^l$")
        choose_answer = TexMobject("\\mathrm{C}_k^l").scale(2).next_to(all_in_k, DOWN)
        choose_answer[0][1].set_color(BLUE)
        choose_answer[0][2].set_color(YELLOW)
        srd = SurroundingRectangle(choose_answer, color=YELLOW)
        self.play(Write(choose_answer), ShowCreationThenDestruction(srd))
        self.wait()

        self.add_caption("这样我们就可以轻易地写出结果来了")
        to_transform = VGroup(choose_answer, all_in_k)
        final_eq = TexMobject("C_k^1", "-", "C_k^2",
                              "+", "C_k^3", "+", "\\cdots", "+", "(-1)^{k-1}", "C_k^k").shift(DOWN)
        idx = (0, 2, 4, 9)
        for i in idx:
            final_eq[i][1].set_color(BLUE)
            final_eq[i][2].set_color(YELLOW)
        self.play(ReplacementTransform(to_transform, final_eq))
        self.wait()

        self.play(final_eq.next_to, count[0], RIGHT)
        self.wait()

        self.add_caption("而这串式子的结果可以通过二项式定理轻易得出")
        binomial = TexMobject("(1-1)^k", "=", "C_k^0", "-", "C_k^1", "+", "C_k^2",
                              "-", "C_k^3", "+", "\\cdots", "+", "(-1)^k", "C_k^k").shift(DOWN)
        idx = (2, 4, 6, 8, 13)
        for i in idx:
            binomial[i][1].set_color(BLUE)
            binomial[i][2].set_color(YELLOW)
        binomial[0].set_color(RED)
        self.play(Write(binomial))
        self.wait()

        self.add_caption("由于$C_k^0=1$，因此结果就是1")
        one = TexMobject("1", color=YELLOW).next_to(count[0])
        self.play(ReplacementTransform(final_eq, one))
        self.wait()

        to_fade_out = VGroup(pk, binomial)
        count = VGroup(count[0], one)
        count.generate_target().scale(2).move_to(ORIGIN)
        self.play(FadeOut(to_fade_out), MoveToTarget(count))

        self.add_caption("所有的$P$在左右的个数都是相等的")
        self.add_caption("这样我们就完成了证明")
        final_srd = SurroundingRectangle(res, color=YELLOW)
        self.play(Transform(neg_hint_srd, final_srd))
        self.play(FadeOutAndShiftDown(count), VGroup(neg_hint_srd, res).move_to, ORIGIN)
        self.wait()
        self.play(Uncreate(neg_hint_srd), FadeOut(res))
        self.wait()


class P04(MyScene):  # 论容斥原理的应用----七选五
    def construct(self):
        self.add_caption("容斥原理的一个很重要的应用就是", "错位排列", color_setting_list=[(1, YELLOW)])
        copyed_title = self.cpt_mob[1].copy().move_to(ORIGIN).to_edge(UP)
        hline = HorizonLine(color=GREY).next_to(copyed_title, DOWN)
        self.play(TransformFromCopy(self.cpt_mob[1], copyed_title))
        self.play(ShowCreation(hline))
        self.wait()
        self.add_caption("其中一个很有趣的案例就是英语的七选五了")
        sfimg = ImageMobject("seven_five.png").scale(2.6).next_to(hline, DOWN).to_edge(LEFT)
        self.play(GrowFromCenter(sfimg))
        self.wait()

        self.add_caption("从七个选项$A-G$中选出$5$个组成一个排列")
        choices = TexMobject(*[chr(i) for i in range(ord("A"), ord("G") + 1)], color=BLUE
                             ).arrange(RIGHT).next_to(hline, DOWN, buff=1.8).to_edge(RIGHT)
        down_arrow = TexMobject("\\Leftarrow", color=RED).rotate(PI / 2).next_to(choices, DOWN, buff=0.8)
        underlines = VGroup(*[Line(start=ORIGIN, end=0.5 * RIGHT, color=YELLOW).set_stroke(width=1) for _ in range(5)]
                            ).arrange(RIGHT, buff=0.25).next_to(down_arrow, DOWN, buff=1.5)
        self.play(AnimationGroup(ShowCreation(choices), Write(down_arrow),
                                 AnimationGroup(*map(ShowCreation, underlines)), lag_ratio=0.5))
        self.wait()
        # print(choices[0].get_width(), choices[0].get_edge_center(RIGHT), choices[1].get_edge_center(LEFT))
        chosen_answer = [5, 2, 6, 4, 3]
        chosen_group = VGroup()
        anims = VGroup()
        for i in range(5):
            anims.add(ApplyMethod(choices[chosen_answer[i]].next_to, underlines[i], UP, buff=0.1))
            chosen_group.add(choices[chosen_answer[i]])
        self.play(AnimationGroup(*anims, lag_ratio=0.25))
        self.wait()

        self.add_caption("将它与正确答案一一比较")
        self.play(FadeOut(VGroup(underlines, choices[0:2], down_arrow)), chosen_group.shift, UP * 3)
        correct_answer = [1, 5, 3, 2, 0]
        correct_choices = VGroup(*[choices[correct_answer[i]].copy().set_color(GREEN_E).next_to(
            chosen_group[i], DOWN, buff=0.8) for i in range(5)])
        self.play(*map(Write, correct_choices))

        anims = VGroup()
        srds = VGroup()
        for i in range(5):
            srds.add(SurroundingRectangle(VGroup(chosen_group[i], correct_choices[i])))
            anims.add(ShowCreation(srds[i], color=YELLOW))
        self.play(AnimationGroup(*anims, lag_ratio=0.25))
        self.wait()

        self.add_caption("看看选对了几个？")
        crs_group = VGroup()
        for i in range(5):
            crs_group.add(VGroup(
                Line(start=chosen_group[i].get_edge_center(UL) + UL * 0.1,
                     end=chosen_group[i].get_edge_center(DR) + DR * 0.1, buff=0),
                Line(start=chosen_group[i].get_edge_center(UR) + UR * 0.1,
                     end=chosen_group[i].get_edge_center(DL) + DL * 0.1, buff=0)
            ).set_color(RED))
            self.play(ShowCreation(crs_group[i]), Uncreate(srds[i]))
        self.wait()
        self.add_caption("很遗憾，一个都没选对，像极了当年高考的我(OTZ)")
        self.add_caption("于是，我们很自然的会有这样的疑问:", anim=[AnimationGroup(*map(Uncreate, crs_group), lag_ratio=0.1)])
        self.add_caption("七选五随机选，全错的概率是多少？")
        possibility = TexMobject("P", "(\\mathrm{score=0})", "=", "?").set_color_by_tex_to_color_map(
            {"P": BLUE, "=": WHITE, "?": RED}
        ).next_to(correct_choices, DOWN, buff=1.5)
        possibility[1][1:6].set_color(BLUE)
        possibility[1][0].set_color(WHITE)
        possibility[1][-1].set_color(WHITE)
        possibility[1][-2].set_color(YELLOW)
        self.play(Write(possibility))
        self.wait()

        self.play(FadeOut(VGroup(possibility, chosen_group, correct_choices, hline, copyed_title)),
                  ShrinkToCenter(sfimg))
        self.remove(sfimg)
        self.wait()


class P05(MyScene):  # 问题的解决
    def construct(self):
        self.add_caption("我们将题目条件进行抽象化")


run("P04 -pl")
