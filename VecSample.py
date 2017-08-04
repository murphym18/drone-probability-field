import math
import random
import numpy as np

# this is like a 3d version of pick a random number that is normally distributed
class VecSample:
   def __init__(self, mean_vector, stdev):
      self.stdev = stdev
      self.mean_vec = mean_vector
   def pick(self):
      # do magic to pick a number
      d = np.random.normal(scale=self.stdev)
      return self.mean_vec + (self.mk_n_vec() * d)
   def mk_n_vec(self):
      z = random.uniform(0,1)
      theta = random.uniform(0, 2*math.pi)
      x = math.sqrt(1 - z**2)*math.cos(theta)
      y = math.sqrt(1 - z**2)*math.sin(theta)
      return np.array([x, y, z])
