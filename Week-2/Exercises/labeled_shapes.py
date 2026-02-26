from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

exp = design.Experiment(name = "labeled shapes")

control.set_develop_mode()
control.initialize(exp)
 
line_length=50
line_width=3

triangle_height = line_length*(math.sqrt(3)/2)
triangle_radius = line_length / (math.sqrt(3))
hexagon_radius = triangle_height/(math.sqrt(3))

# (1)the left triangle
triangle_vertices = geometry.vertices_regular_polygon(3, triangle_radius) 
"""
for geometry.vertices_regular_polygon, the first parameter is side number of the polygon
                                       and the second parameter is the radius of circumcircle.
Side length of the  equilateral triangle is 50, so:
                                       the triangle_radius is 50/√3;
                                       both heights are 25*√3;
                                       the hexogon_radius is 25.
"""


triangle = stimuli.Shape(
    vertex_list=triangle_vertices,
    colour=(128,0,128),
    position=(-100,0)
)
# Add shape labels on top of the line segments
triangle_label = stimuli.TextLine(
    text="triangle",
    text_colour=(255,255,255),
    position=(
        triangle.position[0],
        triangle.position[1] + line_length + 20
    )
)
# Add 50px-long and 3px-wide white vertical lines
triangle_top_y = triangle.position[1] + triangle_radius
triangle_line = stimuli.Line(
    start_point=(triangle.position[0],triangle_top_y), 
    end_point=triangle_label.position, 
    line_width=line_width, 
    colour=(255,255,255))


# (2)the right hexagon
hexagon_vertices = geometry.vertices_regular_polygon(6, hexagon_radius)

hexagon = stimuli.Shape(
    vertex_list=hexagon_vertices,
    colour=(255,255,0),
    position=(100,0)
)

# Add shape labels on top of the line segments
hexagon_label = stimuli.TextLine(
    text="hexagon",
    text_colour=(255,255,255),
    position=(
        hexagon.position[0],
        hexagon.position[1] + line_length + 20
    )
)

# Add 50px-long and 3px-wide white vertical lines
hexagon_top_y = hexagon.position[1] + hexagon_radius
hexagon_line = stimuli.Line(
    start_point=(hexagon.position[0], hexagon_top_y), 
    end_point=hexagon_label.position, 
    line_width=line_width, 
    colour=(255,255,255))

control.start(subject_id=1)

# show all stimuli at once
triangle.present(clear=True, update=False) 
hexagon.present(clear=False, update=False)

triangle_line.present(clear=False, update=False)
hexagon_line.present(clear=False, update=False)

triangle_label.present(clear=False, update=False)
hexagon_label.present(clear=False, update=True)

exp.keyboard.wait()

control.end()

