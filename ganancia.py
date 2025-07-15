from manim import *

class Ganancia(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 150, 10],
            y_range=[0, 700, 50],
            axis_config={"include_numbers": True}
        )

        graph = ax.plot(lambda x: 4 * x, color=BLUE)
        label = ax.get_graph_label(graph, label="G(x) = 4x")

        title = Title("Función de Ganancia")
        self.play(Write(title))
        self.play(Create(ax), Create(graph), Write(label))
        self.wait(2)
