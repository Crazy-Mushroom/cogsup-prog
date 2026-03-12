from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY, C_WHITE, C_BLACK

exp = design.Experiment(
    name="Kanizsa Rectangle",
    background_colour=C_GREY,
)

control.set_develop_mode()
control.initialize(exp)

# deine the function as kanizsa_rectangle
def kanizsa_rectangle(aspect_ratio, rect_scaling_factor, circle_scaling_factor):
    width, height = exp.screen.size

    ## for the rectangle
    rect_w = width // rect_scaling_factor
    rect_h = width // aspect_ratio
    rectangle = stimuli.Rectangle(size=(rect_w, rect_h), colour=C_GREY, position=(0,0))

    ## for the circles
    radius = width // circle_scaling_factor
    """ The centers (x, y) of the circles are the vertices of the rectangle: 
        (-half_rect_w,half_rect_h), (half_rect_w,half_rect_h),(-half_rect_w,-half_rect_h),(half_rect_w,-half_rect_h),
        But! Instead of setting the centers manually, we want the system to find the them automatically.
        Basically, we can do a search, the x ranging from -half_rect_w to half_rect_w, and y from -half_rect_h to half_rect_h
    """
    half_rect_w = rect_w // 2 # we need integers, not floats 
    half_rect_h = rect_h // 2

    points = []
    colors = [] # the upper two circles are black, and the two below are white
    for x in (-half_rect_w, half_rect_w):       # x is either -half_rect_w or half_rect_w
        for y in (-half_rect_h, half_rect_h):   # y is either -half_rect_h or half_rect_h
            points.append((x, y)) # Important! It's (x, y), a point as a pair, not the value of x and the value of y separately
            colors.append(C_BLACK if y>0 else C_WHITE)
    
    circles = []
    for point, color in zip(points, colors):
        circle = stimuli.Circle(radius=radius, colour=color, position=point) 
        circles.append(circle)

    return circles + [rectangle]

# set the values of the parameters
stim_list = kanizsa_rectangle(aspect_ratio=2.5, rect_scaling_factor=2, circle_scaling_factor=16)

# let's present the shapes
exp.screen.clear()

for stim in stim_list:
    stim.present(False, False)
exp.screen.update()

exp.keyboard.wait()

control.end()