""" 
In this experiment, we have two blocks, one is deterministic, another one is stochastic.
Each block has several trials. In each trial, the stimuli consists of a circle and a square (one on the left, another on the right).
The participant is required to determine whether the circle is one the left or right.
The results will be stored in a datafile.
"""
from expyriment import control, design, stimuli
from expyriment.misc.constants import K_LEFT, K_RIGHT, C_BLUE, C_YELLOW, C_GREY
import random

exp = design.Experiment(name="Experiment")
exp.add_data_variable_names(
    ["block_id", "trial_id", "condition", "response", "rt"]
)

STIMSIZE=100
LATERAL_OFFSET=200

# Avoid the full screen and use a small window for the development
control.set_develop_mode()

# Initialize the experiment (this creates the window and prepares everything)
control.initialize(exp)

# Instruction of the experiment (help the participant to understand what to do in this experiemnt)
instruction = stimuli.TextScreen(
    "INSTRUCTION:",
    "TASK: Please find where the circle is.\n\n"
    "      Press LEFT if the circle is on the left.\n"
    "      Press RIGHT if the circle is on the right. \n\n"
)

# Prepare the stimuli
circle = stimuli.Circle(radius=STIMSIZE//2)
square = stimuli.Rectangle(size=(STIMSIZE, STIMSIZE))

circle.preload()
square.preload()

LEFT_POS = ((-LATERAL_OFFSET, 0))
RIGHT_POS = ((LATERAL_OFFSET, 0))

# Start the experiment
control.start(subject_id=1)

instruction.present()
exp.keyboard.wait()

N_TRIALS = 20 # Number of trials in each block

# Block loop, each block contains 20 trials since I set N_TRIALS = 20
for block_id, condition in enumerate(["deterministic", "stochastic"], start=1):
    block_text = stimuli.TextLine(f"Block {block_id}: {condition}")  # Display the current block condition
    block_text.present()
    exp.clock.wait(1500)

    for trial_id in range(1, N_TRIALS + 1):
        if condition == "deterministic":
            circle_loc = "left"
        else:
            circle_loc = random.choice(["left", "right"])
        if circle_loc == "left":
            circle.position = LEFT_POS
            square.position = RIGHT_POS
        else:
            circle.position = RIGHT_POS
            square.position = LEFT_POS

        circle.present(clear=True, update=False)
        square.present(clear=False, update=True)

        # K_LEFT = left, K_RIGHT = right
        key, rt = exp.keyboard.wait([K_LEFT, K_RIGHT])
        
        if key == K_LEFT:
            answer = "left"
        else:
            answer = "right"

        # Judge whether the response is right or wrong    
        if answer == circle_loc:
            response = "correct"
        else:
            response = "incorrect"

        # Record data
        exp.data.add([
            block_id,
            trial_id,
            condition,
            response,
            rt,
        ])

control.end()


        