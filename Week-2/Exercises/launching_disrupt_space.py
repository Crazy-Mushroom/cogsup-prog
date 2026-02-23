from expyriment import design, control, stimuli

exp = design.Experiment(name = "Michottean Lauching Disrupt Space")

control.set_develop_mode()
control.initialize(exp)
 
square_size = (50, 50) 
square_length = square_size[0]

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

control.start(subject_id=1)

left_square.present(clear=True, update=False) 
right_square.present(clear=False, update=True)

# Distance to travel = Initial distance between objects 
# Set speed 
step_size = 10 # pixels per update 
step_count = 0 # to ensure same time and same speed, count step of left square
gap = 60 # try different values: 5, 10, 20, 30, 40, 60, 80 ,100...

# Move left square until collision 
while left_square.distance(right_square) > square_length + gap: 
    left_square.move((step_size, 0)) # (move-x, move-y) 
    step_count += 1
# Don’t forget to update the screen! 
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)


# Move right square the same amount 
moved=0 
while moved < step_count: # ensure the right and the left squares move the same nb of steps
    right_square.move((step_size, 0)) 
    moved +=1
    left_square.present(clear=True, update=False)
    right_square.present(clear=False, update=True)

exp.keyboard.wait()
control.end()
