""" 
The problem: 
The original script calls present() separately for the fixation and the square.
The first call present the fixation cross and swaps the buffers, so the fixation appears on the screen. 
However, the fixation is only stored in the front buffer, while the back buffer remains empty.
When square.present(clear=False, update=True) is called, the square is drawn on the back buffer without the fixation cross. 
After the buffers are swapped, only the square appears on the screen and the fixation disappears.
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)

control.start(subject_id=1)

fixation.present(clear=True, update=False)  # switch update to False, the fixation is drawn to the back buffer before updating the screen
exp.clock.wait(500)

square.present(clear=False, update=True)
exp.keyboard.wait()

control.end()

""" 
My solution
(1):
    fixation.present(clear=True, update=False) 
    square.present(clear=False, update=True)
This ensures that both stimuli are drawn to the back buffer before updating the screen.

(2): Or, separate the steps in a way that perfectly folows the GPU logic: 1. clear back buffer, 2. draw timuli, 3. swap buffers
    
    exp.screen.clear()
    fixation.present(clear=False, update=False) 
    square.present(clear=False, update=False)
    exp.screen.update()
"""