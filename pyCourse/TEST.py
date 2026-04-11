from manim import *
import numpy as np

class Heart(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-2, 2, 0.1],
            y_range=[-1, 2, 0.1],
            axis_config={"color": WHITE},
            x_length=7,
            y_length=6,
            x_axis_config={"tick_size": 0.05},
            y_axis_config={"tick_size": 0.05},
        )

        axes.shift(UP * 1)

        k_tracker = ValueTracker(0.0)

        title = Text(
            "Te amo Lidi ❤️",
            font_size=48,
            color=RED
        )

        title.next_to(axes, DOWN)

        # equation = MathTex(
        #     r"(x^2)^{1/3} + 0.7 \sin(kx)\sqrt{3 - x^2}",
        #     font_size=38,
        #     color=WHITE
        # )

        equation.next_to(title, DOWN)

        k_label = MathTex(
            r"k = ",
            font_size=38,
            color=WHITE
        )

        k_label.next_to(equation, DOWN)

        k_value = always_redraw(
            lambda: DecimalNumber(
                k_tracker.get_value(),
                num_decimal_places=2,
                font_size=38,
                color=WHITE
            ).next_to(k_label, RIGHT)
        )

        graph = always_redraw(
            lambda: axes.plot(
                lambda x: (x**2)**(1/3)
                + 0.7 * np.sin(k_tracker.get_value() * x)
                * np.sqrt(3 - x**2),
                x_range=[-np.sqrt(3), np.sqrt(3)],
                color=RED,
            )
        )

        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Write(title))
        self.play(Write(equation))
        self.play(Write(k_label))
        self.play(Write(k_value))

        self.play(
            k_tracker.animate.set_value(100),
            run_time=10,
            rate_func=linear
        )

        self.wait(2)