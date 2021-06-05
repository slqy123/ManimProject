from manimlib.imports import *
import matplotlib.pyplot as plt


def generate(width=2, height=2, dense=100, min_angle=np.pi/18, coord=np.array([1, 1]),
             speed=np.array([1, 0]), iter_count=10):
    cos_min_angle = -np.cos(min_angle)
    x = []
    y = []
    
    def cos_vec(vec1, vec2):
        return np.dot(vec1, vec2) / np.linalg.norm(vec1) / np.linalg.norm(vec2)

    def in_rect(coord):
        if (-width / 2 < coord[0] < width / 2 and
                -height / 2 < coord[1] < height / 2):
            print(coord/(width, height)*2)
            return True
        else:
            return False
    for _ in range(iter_count):
        # 生成贝塞尔曲线的参考点
        c1 = coord * 1
        c2 = coord + speed
        c3 = (np.random.random(2)-0.5) * (width, height)
        while cos_vec(c2-c1, c3-c2) < cos_min_angle or not in_rect(2*c3-c2):
            c3 = (np.random.random(2)-0.5) * (width, height)
    
        # 绘制曲线
        for i in range(dense):
            t = i / dense
            dot = (1-t)**2*c1 + 2*t*(1-t)*c2 + t**2*c3
            x.append(dot[0])
            y.append(dot[1])
    
        # 更新点的属性
        coord = c3
        speed = c3 - c2
    return x, y


class Show(Scene):
    def construct(self):
        x, y = generate(width=FRAME_WIDTH, height=FRAME_HEIGHT, dense=100, min_angle=-np.pi/18,
                        coord=np.zeros(2), speed=(np.random.random(2)-0.5)*2, iter_count=50)
        crds = [np.array([i, j, 0]) for i, j in zip(x, y)]
        crds.reverse()

        def update(mob, dt):
            crd = crds.pop()
            mob.move_to(crd)

        dot = Dot(crds[-1])
        path = TracedPath(dot.get_center, stroke_color=BLUE)
        dot.add_updater(update)
        self.add(dot, path)
        self.wait(len(crds)/61)


run("-p")