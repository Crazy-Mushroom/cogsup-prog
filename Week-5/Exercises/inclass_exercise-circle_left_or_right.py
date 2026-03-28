""" 
In this experiment:
First, a question appears on the screen "Find the circle left or right?"
Then, two shapes, a circle on the left and a square on the right, are shown simultaneously on the screen.\
The participant press a key to indicate the location of the circle.
If the response is correct, feedback is given "Correct!"; otherwise, feedback is "False!"
"""

from expyriment import design, control, stimuli
from expyriment.misc.constants import K_RIGHT, K_LEFT

exp = design.Experiment(name="right-correct, left-incorrect")
control.set_develop_mode()
control.initialize(exp)

control.start()

# (1) Prepare the question and the shapes (a circle and a square)
question = stimuli.TextLine("Find the circle left or right?")
circle = stimuli.Circle(radius=50, position=(-200, 0))
square = stimuli.Rectangle(size=(100, 100), position=(200,0))

# Use preload() to load the stimuli into memory before presenting them, so they appear at the same time without delay
# here it works because there is a small interval between preloading and the presentation,
# that the participant first sees question and presses a key, giving the computer time to load the shapes into memory.
question.preload()  
circle.preload()
square.preload()

# (2) Present the question, and then the shapes 
question.present()
exp.keyboard.wait()

circle.present(clear=True, update=False)
square.present(clear=False, update=True)

# (3) Wait for the response
# since keyboard.wait returns two values, I unpack both to ensure "key" get the correct intefer for comparison.
key, reaction_time=exp.keyboard.wait([K_LEFT, K_RIGHT]) 

# (4) Give feedback according to the response
if key == K_LEFT:
    feedback = stimuli.TextLine("Correct!")
else:
    feedback = stimuli.TextLine("False!")

feedback.present()
exp.clock.wait(1000)

control.end()
