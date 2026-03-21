from expyriment import design, control, stimuli
import random
import math

""" 
In expyriment, use frames can avoid unnecessary errors.
Most of the refresh rate by default is 60Hz, 
so duration of one frame = 1000ms/60 = 16.67ms.
Thus, we need to do frame-based timing, then compute timing of (draw + present + wait)
"""
frame_rate = 60
frame_duration = 1000/frame_rate

def frams_to_ms(frames):
    return frames*frame_duration

def ms_to_frames(ms):
    return math.ceil(ms/frame_duration)

def load(stims):
    # preload the stimuli
    for stim in stims:
        stim.preload()

def timed_draw(exp, stims):
    start = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    duration = exp.clock.time - start
    return duration
    # return the time it took to draw

def present_for(exp, stims, frames):
    if frames <= 0: # to prevent unnecessary errors
        return
    draw_time = timed_draw(exp, stims)
    target_time = frams_to_ms(frames) # compute the remaining time to wait so that total on-screen duration equals the target on-screen duration
    # remaining time to wait
    remain = target_time - draw_time
    if remain > 0:
        exp.clock.wait(remain)


""" Test functions """
if __name__=="__main__":
    exp = design.Experiment()

    control.set_develop_mode()
    control.initialize(exp)

    fixation = stimuli.FixCross()
    load([fixation])

    n = 20
    positions = [(random.randint(-300, 300), random.randint(-300, 300)) for _ in range(n)]
    squares = [stimuli.Rectangle(size=(50, 50), position = pos) for pos in positions]
    load(squares)

    durations = []

    t0 = exp.clock.time
    for square in squares:
        if not square.is_preloaded:
            print("Preloading function not implemented correctly.")
        stims = [fixation, square] 
        present_for(exp, stims, frames=30) # originally, here was 500 ms, so the frames = 500/16.67=30
        t1 = exp.clock.time
        durations.append(t1-t0)
        t0 = t1

    # As the exercise instruction required: "the program will print "Well done!". Otherwise, it will show you the measured durations."
    if all(abs(d-500) <= 1 for d in durations):
        print("Well done!")
    else:
        ("Measured durations:", durations)

    control.end()