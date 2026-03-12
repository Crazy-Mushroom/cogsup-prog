from expyriment import control, stimuli

control.set_develop_mode(True) # test, the display works fine with or withour control.set_develop_mode()--independent of screen resolution
exp = control.initialize()

# get the size of the screen
width, height = exp.screen.size

# the expected square length = about 5% of the screen width
square_size = int(width * 0.05)

# compute the locations of the four contours, Expyriment'o is (0,0)
half_w = width // 2 
half_h = height // 2 
offset = square_size // 2

top_left = (-half_w + offset, half_h - offset)
top_right = (half_w - offset, half_h - offset)
bottom_left = (-half_w + offset, -half_h + offset)
bottom_right = (half_w - offset, -half_h + offset)

# create the four contours, use line_width parameter to create empty shape
""" 
For each, it's like:
suqare = stimuli.Rectangle(
    size=(square_size, square_size),
    colour=(2255,0,0),
    line_width=1,
)
"""
sq1 = stimuli.Rectangle(size=(square_size, square_size), colour=(255,0,0), line_width=1, position=top_left)
sq2 = stimuli.Rectangle(size=(square_size, square_size), colour=(255,0,0), line_width=1, position=top_right)
sq3 = stimuli.Rectangle(size=(square_size, square_size), colour=(255,0,0), line_width=1, position=bottom_left)
sq4 = stimuli.Rectangle(size=(square_size, square_size), colour=(255,0,0), line_width=1, position=bottom_right)

# show the contours until a key is pressed
sq1.present(clear=True, update=False)
sq2.present(clear=False, update=False)
sq3.present(clear=False, update=False)
sq4.present(clear=False, update=True)

exp.keyboard.wait()
control.end()