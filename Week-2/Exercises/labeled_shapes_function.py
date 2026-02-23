from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

line_length = 50
line_width = 3
label_offset = line_length + 20
white=(255,255,255)
black=(0,0,0)
# create a dictionary to map nb of sides to shape names, it'll be used to generate(retrieve) label names
shapes={3: 'triangle', 4: 'square', 5: 'pentagon', 6: 'hexagon'}

# define a function to create labelled regular polygon with a vertical line
# n       : nb of sides of the polygon
# length  : size that will be used to generate vertices of polygon
# position:(x,y) points the center of polygon
# colour  : the colour of polygon
def create_labelled_polygon(n, length, position, colour):
    vertices=geometry.vertices_regular_polygon(n, length) # the function to generate vertices of the n-side polygon
    
    # use generated vertices to create the polygon
    polygon = stimuli.Shape(
        vertex_list=vertices,
        position=position,
        colour=colour
    )
     
    # generate/ retrieve the name of the polygon based on number of its sides from the dictionary
    name =  shapes.get(n, "polygon")
    x, y = position

    # put the label above the polygon 
    label = stimuli.TextLine(
        text=name,
        position=(x,y+label_offset),
        text_colour=white,
        background_colour=black
    )
    # create the vertical line connecting the polygon and the label
    line = stimuli.Line(
        start_point=polygon.position,
        end_point=label.position,
        line_width=line_width,
        colour=white
)
    return line, polygon, label

# This function draw all stimuli in a  stimulus bundle, 
# so that the function can present each stimulius without repeated clearing and updating
def draw(labeled_polygon):
    for stim in labeled_polygon:
        stim.present(clear=False, update=False)

exp = design.Experiment(name = "labeled shapes function")

control.set_develop_mode()
control.initialize(exp)
 
labeled_triangle = create_labelled_polygon(n = 3, length = 50, position = (-100, 0), colour = (128, 0, 128))
labeled_hexagon = create_labelled_polygon(n = 6, length = 25, position = (100, 0), colour = (255, 255, 0))

control.start(subject_id=1)

exp.screen.clear()
for bundle in (labeled_triangle, labeled_hexagon):
    draw(bundle)
exp.screen.update()

exp.keyboard.wait()

control.end()
