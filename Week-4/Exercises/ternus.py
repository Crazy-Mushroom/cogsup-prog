from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE,C_WHITE, C_BLACK,C_RED,C_BLUE,C_YELLOW
from drawing_functions import load, present_for


### GLOBAL SETTINGS
# constants 
circle_radius = 60
distance_ratio = 3 # distance = space between the centers of the two adjacent circles
spread_ratio = 9   # This is because it equals three circle spacing,
                   # so that it allows the left circle to move to the far right position in the next frame
tag_colours=[C_RED, C_BLUE, C_YELLOW]
circle_frames = 10  # Here I just randomly chose a suitable duration for the participant to clearly see the stimulus, it's about 170 ms.
     

### STIMULI GENERATION
# create the three circles for the ternus display
def make_circles(radius):
    distance = radius * distance_ratio 
    spread = radius * spread_ratio   
    x_positions = range(-spread // 2, spread // 2, distance)

    circles=[]
    for x in x_positions:
        circle = stimuli.Circle(radius=radius, position=(x,0))
        circles.append(circle)
    return circles


# add the colour tag to each circle
                     # a tag is a little concentric circle of the circle
def add_tags(circles, tag_radius):
    for circle, colour in zip(circles, tag_colours):
        tag = stimuli.Circle(radius=tag_radius, colour=colour)
        tag.plot(circle)


def run_trial(circle_radius=60, ISI=0, tags=False): # By default, there is no tag in the circle!
    circles = make_circles(circle_radius)
    if tags:
        add_tags(circles, circle_radius//3) # tag radius is 1/3 of the circle radius, so the tag is much smaller than the circle but not too small to see
    load(circles) # use the load function imported from drawing_functions.py

    spread = circle_radius*spread_ratio
    
    """ 
    Important! 
    create an infinite loop that only stops when a break statement is executed (that is when SPACE is pressed)
    """
    while True: 
        # move the right circle first, then move back left
        for shift in (spread, -spread):
            # after movement, present the circles
            present_for(exp, circles, circle_frames)
            # show the blank screen for ISI frames
            if ISI>0:
                present_for(exp, [], ISI)
            circles[0].move((shift,0))
        if exp.keyboard.check(K_SPACE):
            break


### TRIAL RUN
exp = design.Experiment(
    name="Ternus Illusion",
    background_colour = C_WHITE, 
    foreground_colour = C_BLACK,
)
control.set_develop_mode()
control.initialize(exp)
control.start()

# three required conditions
""" 
When the inter-stimulus interval (ISI) is short, we tend to perceive element motion.
When ISI is long, we tend to perceive group motion.
"""
trials = [
    {"ISI":0, "tags":False},   # 1. Element motion without color tags (low ISI)
    {"ISI":20, "tags":False},  # 2. Group motion without color tags (high ISI)
    {"ISI":30, "tags":True}    # 3. Element motion with color tags (high ISI)
]

for params in trials:
    run_trial(**params) # use **params to unpack the dictionary into function parameters, then automatically pass the parameters

control.end()