from re import T
from venv import create
from cloup import Color
from manim import *

class LimitDef(Scene):
    def construct(self):
   
    # Scene 1: Introduce Formal Limit Definition
        #Part A: Write Limit Def
        # Objects
        limDefG = Tex(r'For any number $\epsilon>0$, there exists a number $\delta>0$ such that: \\ $|x-a|<\delta$ implies $|f(x)-L|<\epsilon$.', color=BLUE,).move_to([0,0,0])
        limNotationG = Tex(r'Formal Limit Definition: \\ $\lim_{x\rightarrow a}f(x)=L$').next_to(limDefG, UP, buff=.15)
        text = Tex(r'Consider the following example.', color=YELLOW).next_to(limNotationG, UP, buff=.25)


        # Animations
        self.play(Write(limNotationG))
        self.wait(2)
        self.play(Write(limDefG))
        self.wait(4)
        self.play(Write(text))
        self.wait(2)

        #Part B: Update Limit Def to Specfic 
        #Objects
        limNotationS = Tex(r'Formal Limit Definition: \\ $\lim_{x\rightarrow 3}\frac{x^2-2x-3}{x^2-4x+3}=2$').move_to([0,1,0])
        limDefS = Tex(r'For any number $\epsilon>0$, there exists a number $\delta>0$ such that: \\ ' , r'$|x-3|<\delta$ ' , r'implies ', r'$|\frac{x^2-2x-3}{x^2-4x+3}-2|<\epsilon$.', arg_separator=" ", color=BLUE,).move_to([0,-.5,0])

        #Animations
        self.play(ReplacementTransform(limNotationG,limNotationS), ReplacementTransform(limDefG, limDefS))
        self.wait(6)
        self.play(FadeOut(text, limNotationS), limDefS.animate.move_to(UP*2.75))

    #Scene 2: Graphing
        #Part A: Creating the Graph
        #Objects
        ax = Axes(
            x_range=[-5, 5],
            y_range=[-4, 4],
            x_axis_config={"numbers_to_include": [3]},
            y_axis_config={"numbers_to_include":[2]},
            tips=False,).move_to([0,-2,0])
        func = lambda x: (x+1)/(x-1)
        curve1 = ax.plot(func, x_range=[1.6,5],color=BLUE)
        curve2 = ax.plot(func, x_range=[-5,.6],color=BLUE)
        xValue=ax.get_vertical_line(ax.input_to_graph_point(3, curve1))
        LValue=ax.get_horizontal_line(ax.input_to_graph_point(3, curve1))

        #Animations
        self.play(FadeIn(ax, curve1, curve2,xValue, LValue))
        self.wait(.5)

        #Part B: Connecting the Def to the Graph
        #Objects
        E=ValueTracker(1)
        D=ValueTracker(1)
        LValueE = always_redraw(lambda: ax.get_horizontal_line(ax.coords_to_point(5,2+E.get_value(),0)))
        LValuee = always_redraw(lambda: ax.get_horizontal_line(ax.coords_to_point(5,2-E.get_value(),0)))
        text1 = Tex(r"For any range aroung $y=2$ \\ Let's say $\epsilon = 1$", color=YELLOW).move_to(ax.coords_to_point(-3,3))
        AreaE = always_redraw(lambda: ax.get_area(ax.plot(lambda x: 2+E.get_value()) ,[0,5], bounded_graph= ax.plot(lambda x: 2-E.get_value()),color=YELLOW, opacity=0.2))
        framebox1 = SurroundingRectangle(limDefS[3], buff = .1)
        text2 = Tex(r"There is a domain around $x=3$ \\ Let's say $\delta = 1$", color=YELLOW).move_to(ax.coords_to_point(-3,3))
        AreaD =  always_redraw(lambda: ax.get_area(ax.plot(lambda x: 4) ,[3-D.get_value(),3+D.get_value()], color=YELLOW, opacity=0.2))
        framebox2 = SurroundingRectangle(limDefS[1], buff = .1)
        text3 = Tex(r' That when we restrict the domain, \\ the function is bounded by the range', color=YELLOW, font_size=40).move_to(ax.coords_to_point(-3,3))
        curve1Faded = always_redraw(lambda: ax.plot(func, x_range=[1.6,5],color=BLUE, stroke_width=1))
        curve1Restricted = always_redraw(lambda: ax.plot(func, x_range=[3-D.get_value(),3+D.get_value()],color=BLUE))
        curve2Faded = ax.plot(func, x_range=[-5,.6],color=BLUE, stroke_width=1)

        #Animations
        self.play(FadeIn(LValuee, LValueE, text1, AreaE, framebox1))
        self.wait(4)
        self.play(FadeOut(AreaE, framebox1), FadeIn(AreaD, framebox2), ReplacementTransform(text1, text2))
        self.wait(4)
        self.play(FadeIn(curve1Restricted), FadeOut(framebox2), ReplacementTransform(text2, text3), ReplacementTransform(curve1, curve1Faded), ReplacementTransform(curve2, curve2Faded))
        self.wait(6)

    # Scene 3: Restricts Epsilon and Delta
        # Part A: Eplion Shrinks
        #Objects
        text4 = Tex(r'For smaller $\epsilon$ values, \\ let $\epsilon = 0.5$', color=YELLOW).move_to(ax.coords_to_point(-3,3))
        curve1Red = always_redraw(lambda: ax.plot(func, x_range=[3-D.get_value(),(3+E.get_value())/(1+E.get_value())],color=RED))
        # always_redraw(lambda: if 3+D.get_value()<(3-E.get_value())/(1-E.get_value()):
        #     domain = [0,0]
        # else:
        #     domain = [(3-E.get_value())/(1-E.get_value()), 3+D.get_value()])
        # curve1Red2 =always_redraw(lambda: ax.plot(func, x_range = domain, color = RED) )

        #Animations
        self.play(FadeIn(curve1Red), ReplacementTransform(text3, text4))
        self.play(E.animate.set_value(0.5), run_time=4)
        self.wait(2)

        #Part B: Delta Shrinks
        #Objects
        text5 = Tex(r'We need to lower the $\delta$ value, \\ let $\delta = 0.6$', color=YELLOW).move_to(ax.coords_to_point(-3,3))

        #Animation
        self.play(ReplacementTransform(text4, text5))
        self.play(D.animate.set_value(0.6), run_time=4)
        self.wait(2)

        #Part C: Epsilon and Delta Shrinks
        #Objects
        text6 = Tex(r'Let $\epsilon =$', color=YELLOW).move_to(ax.coords_to_point(-3,3))
        text7= Tex(r'Let $\delta =$', color=YELLOW).next_to(text6, DOWN, buff=.1)
        e = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3)
            .set_value(E.get_value())
            .next_to(text6, RIGHT, buff=.3)
            .set_color(YELLOW)
        ).add_background_rectangle()
        d = always_redraw(
            lambda: DecimalNumber(num_decimal_places=3)
            .set_value(D.get_value())
            .next_to(text7, RIGHT, buff=.3)
            .set_color(YELLOW)
        ).add_background_rectangle()

        #Animations
        self.play(ReplacementTransform(text5,text6), FadeIn(text7, e, d))
        self.play(E.animate.set_value(0.25), run_time=4)
        self.wait(1)
        self.play(D.animate.set_value(0.4), run_time=4)
        self.wait(1)
        self.play(E.animate.set_value(0.1), run_time=4)
        self.wait(1)
        self.play(D.animate.set_value(0.15), run_time=4)
        self.wait(1)
        self.play(E.animate.set_value(0.05), run_time=4)
        self.wait(1)
        self.play(D.animate.set_value(0.09), run_time=4)
        self.wait(2)

        #Part D: General Epsilon and Delta
        #Objects
        text8 = Tex(r'If $\epsilon = E$, \\ Then $\delta < \frac{2E}{1+E}$.', color=YELLOW).move_to(ax.coords_to_point(-3,3))
        text9 = Tex(r'Can you prove that if $\delta<\frac{2\epsilon}{1+\epsilon}$ and $|x-3|<\delta$, \\then $|\frac{x^2-2x-3}{x^2-4x+3}-2|<\epsilon$?', color=PURPLE_A)

        #Animations
        self.play(ReplacementTransform(text6, text8), FadeOut(text7, e, d))
        self.wait(5)
        self.play(FadeOut(text8, ax, curve1Faded, curve1Red, curve1Restricted, curve2Faded, AreaD, xValue, LValue, LValueE, LValuee))
        self.play(FadeIn(text9))
        self.wait(2)