from expyriment import design, control, stimuli

exp = design.Experiment(name = "Lauching Function")

control.set_develop_mode()
control.initialize(exp)
 
square_size = (50, 50) 
square_length = square_size[0]

def launching_function(temporal_gap=0, spatial_gap=0, faster_target=1.0):

    left_square = stimuli.Rectangle( 
        size=square_size, 
        colour=(255, 0, 0), 
        position=(-400, 0) 
        ) 
    right_square = stimuli.Rectangle( 
        size=square_size, 
        colour=(0, 255, 0), 
        position=(0, 0) 
        ) 

    # initial settings
    left_square.present(clear=True, update=False) 
    right_square.present(clear=False, update=True)

    # (1) speed control
    left_step_size=10
    right_step_size=int(left_step_size * faster_target) 

    step_count = 0 # to ensure same time and same speed, count step of left square

    # Move left square until collision 
    # (2) spatial gap (by default = 0)
    while left_square.distance(right_square) > square_length + spatial_gap: 
        left_square.move((left_step_size, 0)) # (move-x, move-y) 
        step_count += 1
    # Don’t forget to update the screen! 
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)

    # (3) Temporal gap
    if temporal_gap > 0:
        exp.clock.wait(temporal_gap) # the temporal delay required if truning on temporal_gap

    # Move right square the same amount 
    moved=0 
    while moved < step_count: # ensure the right and the left squares move the same nb of steps
        right_square.move((right_step_size, 0)) 
        moved +=1
        left_square.present(clear=True, update=False)
        right_square.present(clear=False, update=True)
    
    # A short pause between experiments
    exp.clock.wait(1000)

control.start(subject_id=1)

# (1) Michottean Launching 
launching_function()

# (2) Launching with temporal gap
launching_function(temporal_gap=2000)

# (3) Launching with spatial gap
launching_function(spatial_gap=60) 
exp.clock.wait(1000)

# (4) Triggering
launching_function(faster_target=3.0)

exp.keyboard.wait()
control.end()
