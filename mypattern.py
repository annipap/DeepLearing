Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Checker():
    resolation = 0
    tile_size = 0
    output = 0

    def __init__(self, r, t):  # body of the constructor
        self.resolation = r
        self.tile_size = t
        self.output = None

    def draw(self):
        white = np.zeros((self.tile_size, self.tile_size), dtype=int)
        black = np.ones((self.resolation, self.resolation), dtype=int)

        black[0:self.tile_size, 0:self.tile_size] = white
        black[self.tile_size:(2 * self.tile_size), self.tile_size:(2 * self.tile_size)] = white
        square = black[0:(2 * self.tile_size), 0:(2 * self.tile_size)]

        x = self.resolation // (2 * self.tile_size)
        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        self.output = np.tile(square, (x, x))
        return np.copy(self.output)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        #plt.show()


class Circle():
    resolution = 0
    radius = 0
    position = (0, 0)
    output = 0

    def __init__(self, r, rd, p):  # body of the constructor
        self.resolution = r
        self.radius = rd
        self.position = p
        self.output = None

    def draw(self):
        black = np.zeros((self.resolution, self.resolution), dtype=int)
        xv = range(self.resolution) #;
        yv = range(self.resolution)
        x, y = np.meshgrid(xv, yv, sparse=False)
        xc = self.position[0]
        yc = self.position[1]
        black[(x - xc) ** 2 + (y - yc) ** 2 < self.radius ** 2] = 1

        ax = plt.gca()
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        self.output = black

        return np.copy(self.output)

    def show(self):
        plt.imshow(self.output, cmap='gray')
        #plt.show()
