from manim import Scene, Circle, LIGHT_PINK, Create

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        
        circle.set_fill(color=LIGHT_PINK, opacity=0.5)

        self.play(Create(mobject=circle))
