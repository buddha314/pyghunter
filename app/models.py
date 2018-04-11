import numpy as np
import math, random

class Agent:
    def __init__(self, name):
        self.name = name

class Tiler(object):
    def __init__(self, min, max, slices):
        self.min=min
        self.max=max
        self.slices=slices
        self.bins=[]
        self.build_bins()

    def build_bins(self):
        intv = (self.max-self.min)/(self.slices-1.0)
        overlap = intv - 1.0*(self.max - self.min)/self.slices
        self.bins = [
          [self.min + i*(intv-overlap), self.min + (i+1)*(intv - overlap)+overlap] for i in range(self.slices)
        ]

    def state(self, x):
        state = [0]*self.slices
        for i in range(self.slices):
            if x >= self.bins[i][0] and x <= self.bins[i][1]:
                state[i] = 1
        return np.array(state)


"""
> flask shell

import app.models
x = app.models.RadiusTiler(min=0, max=75, slices=9)
x.state(59)
"""
class RadiusTiler(Tiler):
    def __init__(self, max, min=0, slices=7):
        super(RadiusTiler,self).__init__(min=min,max=max,slices=slices)

class AngleTiler(Tiler):
    def __init__(self, min=-math.pi, max=math.pi, slices=7):
        super(RadiusTiler,self).__init__(min=min,max=max,slices=slices)

class DM:
    def __init__(self, name):
        self.name = name
        self.tiles = []

    def add_tiler(self, tiler):
        self.tiles.append(tiler)
