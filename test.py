import numpy as np
import matplotlib.pyplot as plt

class Spectrum():
    resolution = 0
    output = 0

    def __init__(self, r):  # body of the constructor
        self.resolution = r
        self.output = None

    def draw(self):
        colour = np.zeros((self.resolution, self.resolution, 3), dtype=float)
        r = np.linspace(0, 1, self.resolution)
        b = np.linspace(1, 0, self.resolution)
        g = np.linspace(0, 1, self.resolution)

        colour[:, :, 0] = r
        colour[:, :, 1] = g.reshape(self.resolution, -1)
        colour[:, :, 2] = b

        self.output = colour
        return np.copy(self.output)

    plt.show()
