from manim import *


class Bit(VMobject):
    def __init__(self, value: float = 0):
        super().__init__()

        zero = Square(side_length=1).set_stroke(width=6).set_color(WHITE).set_fill(opacity=0)
        text_zero = Text("0", font="Digital Numbers").move_to(zero)

        one = Square(side_length=1).set_stroke(width=6).set_color(WHITE).set_fill(opacity=0)
        text_one = Text("1", font="Digital Numbers").move_to(one)

        frame = VGroup(
            VGroup(zero, text_zero),
            VGroup(one, text_one),
        ).arrange_submobjects()
        self.add(frame)

        fill = Square(side_length=1).set_color(RED).set_fill(opacity=1).move_to(zero)
        self.add_to_back(fill)

        self.value = ValueTracker(value=value)
        fill.add_updater(lambda mobj: mobj.move_to(one if self.value.get_value() > 0.5 else zero))


class Pbit(VMobject):
    def __init__(self, value: float = 0.0):
        super().__init__()

        frame = Rectangle(height=0.5, width=4).set_stroke(width=6)
        self.add(frame)

        fill = Rectangle(height=frame.height, width=value * frame.width).set_fill(GREEN, opacity=1).set_stroke(width=0).align_to(frame, LEFT)
        self.add_to_back(fill)

        label = DecimalNumber(value, num_decimal_places=1).next_to(frame, UP)
        self.add(label)

        self.value = ValueTracker(value=value)
        fill.add_updater(lambda mobj: mobj.stretch_to_fit_width(self.value.get_value() * frame.width).align_to(frame, LEFT))
        label.add_updater(lambda mobj: mobj.set_value(self.value.get_value()))


def Rx(theta: float) -> np.ndarray:
    return np.ndarray([[np.cos(theta), 1j * np.sin(theta)], [1j * np.sin(theta), np.cos(theta)]])


def Ry(theta: float) -> np.ndarray:
    return np.ndarray([[np.cos(theta), -1j * np.sin(theta)], [1j * np.sin(theta), np.cos(theta)]])


def Rz(theta: float) -> np.ndarray:
    return np.ndarray([1, 0], [0, np.exp(1j * theta)])


def qubit_to_bloch(ket: np.ndarray) -> np.ndarray:
    phi = np.subtract.reduce(np.angle(ket))
    theta = 2 * np.arctan(np.divide.reduce(np.abs(ket)))
    return np.array([np.cos(phi) * np.sin(theta), np.sin(phi) * np.sin(theta), np.cos(theta)])


def bloch_to_qubit(bloch: np.ndarray) -> np.ndarray:
    raise NotImplementedError()


class Qubit(VMobject):
    def __init__(self, value: np.ndarray):
        assert len(value) == 2

        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, 2, 1))
        # xlabel = axes.get_x_axis_label(Text("X"), direction=RIGHT)
        # ylabel = axes.get_y_axis_label(Text("Y"), direction=UP)
        # zlabel = axes.get_z_axis_label(Text("Z"), direction=OUT)

        # self.add(axes, xlabel, ylabel, zlabel)
        self.add(axes)

        sphere = Sphere(center=ORIGIN, radius=1, resolution=(15, 20), color=PURPLE)
        pointer = Dot3D(OUT, radius=0.1)
        self.add(sphere, pointer)

        self.value = ValueTracker(value=value)
        self.value.interpolate()

        pointer.add_updater(lambda mobj: mobj.move_to(qubit_to_bloch()))
