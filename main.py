import VecSample
import numpy as np

num_samples = 10
init_pos_guess = np.array([0, 0, 0])
pos_stdev = 0.25
velocity_guess = np.array([4, 4, 4])
vel_stdev = 0.1

pos = VecSample.VecSample(init_pos_guess, pos_stdev)
vel = VecSample.VecSample(velocity_guess, vel_stdev)

def sample_pos(t):
    v = vel.pick()
    dp = v*t
    p = pos.pick()
    return p + dp

for i in range(3):
    print(sample_pos(2))
