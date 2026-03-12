from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK


def build_grid(nb_rows, nb_cols, size, color, space, background_color):
    
    # Since background_colour should be set by parameter, 
    # we create the experiment also inside the function.
    exp = design.Experiment(
        name="Hermann Grid", 
        background_colour = background_color,
    )
    control.set_develop_mode()
    control.initialize(exp)

    # we need to compute the size of grid and 
    # the length of the row(column) cannot excess the width and length of the screen
    grid_w = size * nb_cols + space * (nb_cols - 1)
    grid_h = size * nb_rows + space * (nb_rows - 1)

    # (Just in case if the size of the grid does not fit the screen size) 
    # We check if the grid size fits the screen size under current parameter values; if not, raise an error.
    width, height = exp.screen.size
    if grid_w > width or grid_h > height:
        raise ValueError("The target grid does not on fit the screen")

    # start from the top left square, let's locate all the little squares
    start_x = - grid_w // 2 + size // 2
    start_y = grid_h // 2 - size // 2

    squares = [] # to store all the little squares

    # use the nested loops to draw each square
    # basically, it is to locate each square based on the location of the top left square
    for i in range(nb_rows):
        for j in range(nb_cols):
            x = start_x + (size + space)*j
            y = start_y - (size + space)*i

            square = stimuli.Rectangle(size=(size,size), colour=color, position=(x,y))
            squares.append(square)
    return exp, squares

# set the parameters to build the grid and start the experiment!
exp, stim_list = build_grid(
    nb_rows = 10,
    nb_cols = 10,
    size = 50,
    color = C_BLACK,
    space = 10,
    background_color = C_WHITE,
)

exp.screen.clear()
for stim in stim_list:
    stim.present(clear=False, update=False)

exp.screen.update()
exp.keyboard.wait()
control.end()

    

