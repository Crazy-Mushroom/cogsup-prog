from expyriment import design, control, stimuli

exp = design.Experiment(name = "Two square")

control.set_develop_mode()
control.initialize(exp)
 
square_size = (50, 50) 
left_square = stimuli.Rectangle( 
    size=square_size, 
    colour=(0, 0, 255), 
    position=(-100, 0) 
    ) 
right_square = stimuli.Rectangle( 
    size=square_size, 
    colour=(0, 255, 0), 
    position=(100, 0) 
    ) 

control.start(subject_id=1)

left_square.present(clear=True, update=False) 
right_square.present(clear=False, update=True)

exp.keyboard.wait()

control.end()