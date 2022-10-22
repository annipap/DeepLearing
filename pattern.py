import numpy as np
import matplotlib.pyplot as plt


class Checkers:
    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = None

    def draw(self):
        black = np.zeros((2*self.tile_size, 2*self.tile_size), dtype=int)
        print('-------------\n', 'Black is:\n', black)
        white = np.ones((self.tile_size, self.tile_size), dtype=int)
        print('White is:\n', white)
        black[self.tile_size:2*self.tile_size, 0:self.tile_size] = white
        black[0:self.tile_size, self.tile_size:2*self.tile_size] = white
        print('2nd Black is:\n', black)
        self.output = np.tile(black, (self.resolution//(2*self.tile_size), self.resolution//(2*self.tile_size)))
        print('Output is:\n', self.output)
        return np.copy(self.output)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()


class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None

    def draw(self):
        a = np.linspace(0, self.resolution, self.resolution, dtype=int)
        b = np.linspace(0, self.resolution, self.resolution, dtype=int)
        x_grid, y_grid = np.meshgrid(a, b)
        black = np.zeros((self.resolution, self.resolution), dtype=int)
        # print('Black is:\n', black)
        black[(x_grid - self.position[0]) ** 2 + (y_grid - self.position[1]) ** 2 < self.radius ** 2] = 1
        self.output = black

    def show(self):
        plt.imshow(self.output, cmap='gray')
        plt.show()

# class Spectrum:
#     def __init__(self, resolution, ):
#         self.resolution = resolution
#         self.output = None
#
#
#     def draw(self):
#         a = 1
#
#
#     def show(self):
#         plt.imshow(self.output)
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

    def show(self):
        plt.imshow(self.output)

        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
# jabra = Checkers(18, 3)
# jabra.draw()
# jabra.show()
#
# jabra = Circle(256, 40, (100, 100))
# jabra.draw()
# jabra.show()

# jabra = Spectrum(1000)
# jabra.draw()
# jabra.show()

###Checkerboard###
# resolution = 24
# tile_size = 2
# black = np.zeros((2*tile_size, 2*tile_size), dtype=int)
# print('-------------\n', 'Black is:\n', black)
# white = np.ones((tile_size, tile_size), dtype=int)
# print('White is:\n', white)
# black[tile_size:2*tile_size, 0:tile_size] = white
# black[0:tile_size, tile_size:2*tile_size] = white
# print('2nd Black is:\n', black)
# black = np.tile(black, (resolution//(2*tile_size), resolution//(2*tile_size)))
# print('Output is:\n', black)
# plt.imshow(black, cmap='gray')
# plt.show()

###Circle###
# resolution = 256
# radius = 40
# start, end, step = 0, resolution, resolution
# position = np.array([150, 150])
# a = np.linspace(start, end, step, dtype=int)
# b = np.linspace(start, end, step, dtype=int)
# x_grid, y_grid = np.meshgrid(a, b)
# print('y=\n', y_grid)
# print('x=\n', x_grid)
# print('look here=\n',(x_grid-position[0])**2+(y_grid-position[1])**2)
# black = np.zeros((resolution, resolution), dtype=int)
# print('Black is:\n', black)
# black[(x_grid-position[0])**2+(y_grid-position[1])**2 < radius**2] = 1
# print(black)
# plt.imshow(black, cmap='gray')
# plt.show()


# ###Color Spectrum###
# resolution = 4
# colour = np.zeros((resolution, resolution, 3), dtype=float)
# red = np.linspace(0, 1, resolution)
# blue = np.linspace(1, 0, resolution)
# green = np.linspace(0, 1, resolution)
# # print('Red is:\n', red)
# # print('colour is:\n',colour)
# colour[:, :, 0] = red
# #colour[:, :, 2] = blue
#
#
#
# print('output is:\n',colour)
# plt.imshow(colour)
# plt.show()