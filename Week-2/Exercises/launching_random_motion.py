from expyriment import design, control, stimuli
import random 
import math

exp = design.Experiment(name = "Launching Random Motion")

control.set_develop_mode()
control.initialize(exp)
 
square_size = (50, 50) 
square_length = square_size[0]

def launching_random_motion():
    # create random anglei, and computational methods (direction vectors)
    theta = random.uniform(0, 2*math.pi)
    x = math.cos(theta)
    y = math.sin(theta)
     
    # create squares
    green_square = stimuli.Rectangle( 
        size=square_size, 
        colour=(0, 255, 0), 
        position=(0, 0) 
        ) 
    red_square = stimuli.Rectangle( 
        size=square_size, 
        colour=(255, 0, 0), 
        position=(300*x, 300*y) 
        ) 

    # initial settings
    red_square.present(clear=True, update=False) 
    green_square.present(clear=False, update=True)

    # speed control
    step_size=10
    step_count = 0 # to ensure same time and same speed, count step of left square

    # Move the green square towards the red square 
    # (2) spatial gap (by default = 0)
    while True: 
        green_square.move((step_size*x, step_size*y)) # (move-x, move-y) 
        step_count += 1
    # Don’t forget to update the screen! 
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)

    # if two squares meet, stop moving (avoid overlapping)
    # overlapping: True/False; overlap_area: number
        overlapping, overlap_area = green_square.overlapping_with_stimulus(red_square)
        if overlapping:
            break

    # Move the red square at the same time and same speed 
    moved=0 
    while moved < step_count: # ensure the right and the left squares move the same nb of steps
        red_square.move((step_size*x, step_size*y)) 
        moved +=1
        red_square.present(clear=True, update=False)
        green_square.present(clear=False, update=True)
    
    # A short pause between experiments
    exp.clock.wait(1000)

control.start(subject_id=1)

# Display three conseccutive launching events
for i in range(3):
    launching_random_motion()

exp.keyboard.wait()
control.end()
