from manim import *
from bloch.bit import Bit, Pbit, Qubit, qubit_to_bloch


class BlochSphereXRotation(ThreeDScene):
    def construct(self):
        self.renderer.camera.light_source.move_to(3 * IN + 2 * DOWN + RIGHT)
        phi = 75 * DEGREES
        theta = 30 * DEGREES
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, zoom=1.5)
        direction = np.array([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)])

        axes = ThreeDAxes(x_length=4, y_length=4, z_length=4, x_range=(None), y_range=None, z_range=None)
        xlabel = axes.get_x_axis_label(Text("X"), direction=direction)
        ylabel = axes.get_y_axis_label(Text("Y"), edge=UP)
        zlabel = axes.get_z_axis_label(Text("Z"), rotation=0, rotation_axis=OUT)

        self.add(axes, xlabel, ylabel, zlabel)

        sphere = Sphere(radius=1, resolution=(100, 100), color=PURPLE)
        Surface

        n = 8
        offset = PI / n
        pointers = VGroup(*[Dot3D(np.array([np.cos(angle), 0, np.sin(angle)]), radius=0.05, color=WHITE, resolution=(10, 10)) for angle in np.linspace(offset, 2 * PI + offset, n, endpoint=False)])

        self.add(pointers, sphere)

        self.play(Rotate(pointers, angle=PI, axis=RIGHT, about_point=ORIGIN))
        self.wait()


class BlochSphereYRotation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, 2, 1))
        xlabel = axes.get_x_axis_label(Text("X"), direction=RIGHT)
        ylabel = axes.get_y_axis_label(Text("Y"), direction=UP)
        zlabel = axes.get_z_axis_label(Text("Z"), direction=OUT)

        self.renderer.camera.light_source.move_to(3 * IN)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes, xlabel, ylabel, zlabel)

        # sphere = Sphere(center=ORIGIN, radius=1, resolution=(15, 20), color=PURPLE)
        sphere = Dot3D(radius=1, color=PURPLE, resolution=(15, 20))
        ket = Dot3D(OUT, radius=0.1)

        self.add(ket, sphere)

        self.play(Rotate(ket, angle=PI, axis=UP, about_point=ORIGIN))


class BlochSphereYRotationStream(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, 2, 1))
        xlabel = axes.get_x_axis_label(Text("X"), direction=RIGHT)
        ylabel = axes.get_y_axis_label(Text("Y"), direction=UP)
        zlabel = axes.get_z_axis_label(Text("Z"), direction=OUT)

        # func = lambda pos:
        stream = StreamLines()

        # self.renderer.camera.light_source.move_to(3 * IN)
        # self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # self.add(axes, xlabel, ylabel, zlabel)

        # # sphere = Sphere(center=ORIGIN, radius=1, resolution=(15, 20), color=PURPLE)
        # sphere = Dot3D(radius=1, color=PURPLE, resolution=(15, 20))
        # ket = Dot3D(OUT, radius=0.1)

        # self.add(ket, sphere)

        # self.play(Rotate(ket, angle=PI, axis=UP, about_point=ORIGIN))


class BitDistribution(Scene):
    def construct(self):
        bit = Bit()
        chart = BarChart(
            values=[1.0, 0.0001],
            bar_names=["0", "1"],
            x_length=4,
            y_range=[0, 1],
        )

        chart.add_updater(
            lambda mobj: mobj.change_bar_values(
                [
                    1.0 if bit.value.get_value() == 0.0 else 0.0,
                    1.0 if bit.value.get_value() == 1.0 else 0.0,
                ]
            )
        )

        group = VGroup(bit, chart)
        group.arrange_in_grid(rows=2, col_alignments="c")
        bit.next_to(chart.bars, direction=UP, buff=0.8)

        self.add(group)
        self.wait(2)

        bit.value.set_value(1.0 - bit.value.get_value())
        bit.update()
        chart.update()
        self.wait(2)


class PbitDistribution(Scene):
    def construct(self):
        bit = Pbit(0.8)
        chart = BarChart(
            values=[0.2, 0.8],
            bar_names=["0", "1"],
            x_length=4,
            y_range=[0, 1],
        )

        chart.add_updater(
            lambda mobj: mobj.change_bar_values(
                [
                    1 - bit.value.get_value(),
                    bit.value.get_value(),
                ]
            )
        )

        group = VGroup(bit, chart)
        group.arrange_in_grid(rows=2, col_alignments="c")
        bit.next_to(chart.bars, direction=UP, buff=1.2)

        self.add(group)

        self.play(bit.value.animate.set_value(0.2))
        self.wait()

        self.play(bit.value.animate.set_value(0.8))
        self.wait()


# class QubitX(Scene):
#     def construct(self):
#         ket = ValueTracker(np.array([1, 0]))

#         qubit = Qubit(ket.get_value())
#         qubit.add_updater(lambda mobj: mobj.move_to(qubit_to_bloch(ket.get_value())))
#         self.add(qubit)

#         self.play(ket.animate.set(np.array[0, 1]))


class QubitDistribution(Scene):
    def construct(self):
        ket = ValueTracker(np.array([1.0, 0.0], dtype=np.complex64))
        qubit = Qubit(ket.get_value())
        qubit.add_updater(lambda mobj: mobj.move_to(qubit_to_bloch(ket.get_value())))
        self.add(qubit)

        # X-rotation
        self.add(ket.animate.set(np.array([])))
