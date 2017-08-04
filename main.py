import VecSample
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

num_samples = 10
init_pos_guess = np.array([0, 0, 0])
pos_stdev = 0.25
velocity_guess = np.array([4, 4, 4])
vel_stdev = 1.2

pos = VecSample.VecSample(init_pos_guess, pos_stdev)
vel = VecSample.VecSample(velocity_guess, vel_stdev)

def sample_pos(t):
    v = vel.pick()
    dp = v*t
    p = pos.pick()
    return p + dp

def make_data(sample_size):
    t_domain = np.arange(0,5,0.25)
    s = []
    for t in t_domain:
        for i in range(sample_size):
            s.append(sample_pos(t))
    return s

data = make_data(500)
xs = [r[0] for r in data]
ys = [r[1] for r in data]
zs = [r[2] for r in data]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs, c='b', marker='.')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
