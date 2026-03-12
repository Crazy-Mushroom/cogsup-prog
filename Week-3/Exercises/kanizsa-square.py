from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_WHITE, C_BLACK

exp = design.Experiment(
    name="Kanizsa Square",
    background_colour=C_GREY,
)

control.set_develop_mode()
control.initialize(exp)

width, height = exp.screen.size
square_size=int(width * 0.25)
circle_radius=int(width * 0.05)

offset = square_size/2

# the center for each circle is actually the vertex of the square
top_left = (-offset, offset)
top_right = (offset, offset)
bottom_left = (-offset, -offset)
bottom_right = (offset, -offset)

# locate the circles
c1 = stimuli.Circle(circle_radius, C_BLACK, position=top_left)
c2 = stimuli.Circle(circle_radius, C_BLACK, position=top_right)
c3 = stimuli.Circle(circle_radius, C_WHITE, position=bottom_left)
c4 = stimuli.Circle(circle_radius, C_WHITE, position=bottom_right)

# mask
m = stimuli.Rectangle((square_size,square_size), C_GREY, position=(0,0))

control.start()

# draw the circles 
c1.present(clear=True, update=False)
c2.present(clear=False, update=False)
c3.present(clear=False, update=False)
c4.present(clear=False, update=False)
# then the mask, and show all the shape at the end
m.present(clear=False, update=True)

exp.keyboard.wait()
control.end()