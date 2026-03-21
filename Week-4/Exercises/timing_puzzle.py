"""
After running the original code, it reported that the fixation was present on the screen for 1.006 seconds.
When the function present() is called, the stimulus will only appear at the nest refresh.
This introduces a delay of up to one refresh cycle. 
Therefore, the fixation cross stas on the screen slightly longer than one second.
"""

from expyriment import design, control, stimuli

exp = design.Experiment(name="timing puzzle")

control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
text = stimuli.TextLine("Fixation removed")

# use preload to reduce timing delays
fixation.preload()
text.preload()

# measure the presentation time, and subtract this time from the waiting time
t0 = exp.clock.time
fixation.present()
t1 = exp.clock.time
dt =  t1 - t0  # dt = the time for executing present()

# wait remaining time
exp.clock.wait(1000 - dt)

text.present()
t2 = exp.clock.time

fix_duration = (t2 - t1)/1000

exp.clock.wait(1000)

units = "second" if fix_duration == 1.0 else "seconds"
duration_text = f"Fixation was present on the screen for {fix_duration} {units}"

text2 = stimuli.TextLine(duration_text)
text2.present()
exp.clock.wait(2000)

control.end()