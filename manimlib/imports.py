"""
I won't pretend like this is best practice, by in creating animations for a video,
it can be very nice to simply have all of the Mobjects, Animations, Scenes, etc.
of manim available without having to worry about what namespace they come from.

Rather than having a large pile of "from <module> import *" at the top of every such
script, the intent of this file is to make it so that one can just include
"from manimlib.imports import *".  The effects of adding more modules
or refactoring the library on current or older scene scripts should be entirely
addressible by changing this file.

Note: One should NOT import from this file for main library code, it is meant only
as a convenience for scripts creating scenes for videos.
"""

from manimlib.constants import *

from manimlib.animation.animation import *
from manimlib.animation.composition import *
from manimlib.animation.creation import *
from manimlib.animation.fading import *
from manimlib.animation.growing import *
from manimlib.animation.indication import *
from manimlib.animation.movement import *
from manimlib.animation.numbers import *
from manimlib.animation.rotation import *
from manimlib.animation.specialized import *
from manimlib.animation.transform import *
from manimlib.animation.update import *

from manimlib.camera.camera import *
from manimlib.camera.mapping_camera import *
from manimlib.camera.moving_camera import *
from manimlib.camera.three_d_camera import *

from manimlib.mobject.coordinate_systems import *
from manimlib.mobject.changing import *
from manimlib.mobject.frame import *
from manimlib.mobject.functions import *
from manimlib.mobject.geometry import *
from manimlib.mobject.matrix import *
from manimlib.mobject.mobject import *
from manimlib.mobject.number_line import *
from manimlib.mobject.numbers import *
from manimlib.mobject.probability import *
from manimlib.mobject.shape_matchers import *
from manimlib.mobject.svg.brace import *
from manimlib.mobject.svg.drawings import *
from manimlib.mobject.svg.svg_mobject import *
from manimlib.mobject.svg.tex_mobject import *
from manimlib.mobject.svg.text_mobject import *
from manimlib.mobject.svg.code_mobject import *
from manimlib.mobject.three_d_utils import *
from manimlib.mobject.three_dimensions import *
from manimlib.mobject.types.image_mobject import *
from manimlib.mobject.types.point_cloud_mobject import *
from manimlib.mobject.types.vectorized_mobject import *
from manimlib.mobject.mobject_update_utils import *
from manimlib.mobject.value_tracker import *
from manimlib.mobject.vector_field import *

from manimlib.for_3b1b_videos.common_scenes import *
from manimlib.for_3b1b_videos.pi_creature import *
from manimlib.for_3b1b_videos.pi_creature_animations import *
from manimlib.for_3b1b_videos.pi_creature_scene import *

from manimlib.once_useful_constructs.arithmetic import *
from manimlib.once_useful_constructs.combinatorics import *
from manimlib.once_useful_constructs.complex_transformation_scene import *
from manimlib.once_useful_constructs.counting import *
from manimlib.once_useful_constructs.fractals import *
from manimlib.once_useful_constructs.graph_theory import *
from manimlib.once_useful_constructs.light import *

from manimlib.scene.graph_scene import *
from manimlib.scene.moving_camera_scene import *
from manimlib.scene.reconfigurable_scene import *
from manimlib.scene.scene import *
from manimlib.scene.sample_space_scene import *
from manimlib.scene.graph_scene import *
from manimlib.scene.scene_from_video import *
from manimlib.scene.three_d_scene import *
from manimlib.scene.vector_space_scene import *
from manimlib.scene.zoomed_scene import *

from manimlib.utils.bezier import *
from manimlib.utils.color import *
from manimlib.utils.config_ops import *
from manimlib.utils.debug import *
from manimlib.utils.images import *
from manimlib.utils.iterables import *
from manimlib.utils.file_ops import *
from manimlib.utils.paths import *
from manimlib.utils.rate_functions import *
from manimlib.utils.simple_functions import *
from manimlib.utils.sounds import *
from manimlib.utils.space_ops import *
from manimlib.utils.strings import *

# Non manim libraries that are also nice to have without thinking

import inspect
import itertools as it
import numpy as np
import operator as op
import os
import random
import re
import string
import sys
import math

from PIL import Image
from colour import Color


def run(ctr):
    f = open("manim.py", "w")
    f.write("""#!/usr/bin/env python
import manimlib

if __name__ == "__main__":
    manimlib.main()""")
    f.close()
    cmd = "python -m manim " + sys.argv[0] + " " + ctr
    os.system(cmd)


class MyScene(Scene):

    def add_caption(self, cpt, wait_time=2, anim_run_time=1, *args, **kwargs):
        cpt = TextMobject(cpt, *args, **kwargs).to_edge(DOWN)
        # if color_setting_list:
        #     for color_setting in color_setting_list:
        #         idx, color = color_setting
        #         cpt[idx].set_color(color)
        if hasattr(self, "cpt_mob"):
            self.play(Transform(self.cpt_mob, cpt), run_time=anim_run_time)
        else:
            self.cpt_mob = cpt
            self.play(Write(self.cpt_mob))
        self.wait(wait_time)

    def fade_all_out(self):
        self.play(*map(FadeOut, self.mobjects))


def get_circle_coords(n, start=0, radius=1):
    return [radius*np.array([np.cos(start+i*2*PI/n),
                             np.sin(start+i*2*PI/n), 0])
            for i in range(n)]


class MobCircleGenerater(object):
    def __init__(self, Mob, *args, **kwargs):
        self.mob = Mob(*args, **kwargs)
        self.all_group = VGroup()

    def generate_circle(self, amount, center=ORIGIN, start_angle=0, rotate_axis=IN):
        mob_group = VGroup()
        for i in range(amount):
            mobcp = self.mob.copy().move_to(np.array([math.cos(start_angle + i * 2 * PI / amount),
                                                      math.sin(start_angle + i * 2 * PI / amount, 0)]) + center)
            mob_group.add(mobcp)

        self.all_group.add(mob_group)
        return mob_group


class Graph(object):
    def __init__(self, dots, scene=None, animate=True):
        self.scene = scene
        self.dot_group = dots
        self.line_group = VGroup()
        if scene and animate:
            scene.play(ShowCreation(dots))

    def highlight(self, dots):
        poly = Polygon(*map(lambda i: self.dot_group[i].get_center(), dots), color=YELLOW)
        self.scene.play(ShowCreationThenDestruction(poly), run_time=len(dots)*0.5)


    def add_dots(self, *dots):
        for dot in dots:
            self.dot_group.add(dot)
        self.scene.play(*map(ShowCreation, dots), run_time=0.5)

    def add_lines(self, *lines):
        for line in lines:
            self.line_group.add(line)
        self.scene.play(*map(ShowCreation, lines))

    def center(self, idx):
        return self.dot_group[idx].get_center()

    def dot(self, idx, direction, **kwargs):
        return Dot(self.center(idx)+direction, **kwargs)

    def line(self, idx1, idx2, **kwargs):
        return Line(self.center(idx1), self.center(idx2), buff=SMALL_BUFF, **kwargs)

