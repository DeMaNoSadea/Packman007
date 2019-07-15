class Matrix:
    def __init__(self, width, height):
        self.grid = []
        self.Tile = 0
        self.width = width
        self.height = height

    def Markup(self):
        self.x = self.width / 32
        self.y = self.height / 32
        self.width = self.width / self.x
        self.height = self.height / self.y
        for self.i in range(self.y):
            self.grid.append([])
            for self.j in range(self.x):
                self.grid[self.j].append(0)

    def Objest_Tale(self, row, column):
        self.grid[row][column] = self.Tile

    def Generator(self):
        self.grid = [[self.j in range(self.x)], self.i in range(self.y)]

        