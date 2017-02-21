# move
RIGHT_UP = 0
RIGHT_DOWN = 1
LEFT_UP = 2
LEFT_DOWN = 3
UP_RIGHT = 4
UP_LEFT = 5

# direction
FRONT = 0
BACK = 1
RIGHT = 2
LEFT = 3
UP = 4
DOWN = 5

# color
BLUE = 0
GREEN = 1
ORANGE = 2
RED = 3
YELLOW = 4
WHITE = 5


class Cube(object):
    def __init__(self, color):
        self.start = [c for c in color]
        self.record = []
        self.now = self.start

    def get(self):
        return ''.join(self.now)

    def move(self, move):
        color = self.now[:]
        if move == RIGHT_UP:
            m = [2, 0, 3, 1,
                 4, 5, 6, 7,
                 20, 9, 21, 11,
                 16, 13, 17, 15,
                 10, 8, 18, 19,
                 14, 12, 22, 23]
        elif move == RIGHT_DOWN:
            m = [1, 3, 0, 2,
                 4, 5, 6, 7,
                 17, 9, 16, 11,
                 21, 13, 20, 15,
                 12, 14, 18, 19,
                 8, 10, 22, 23]
        elif move == LEFT_UP:
            m = [20, 1, 22, 3,
                 16, 5, 18, 7,
                 10, 8, 11, 9,
                 12, 13, 14, 15,
                 2, 17, 0, 19,
                 6, 21, 4, 23]
        elif move == LEFT_DOWN:
            m = [18, 1, 16, 3,
                 22, 5, 20, 7,
                 9, 11, 8, 10,
                 12, 13, 14, 15,
                 4, 17, 6, 19,
                 0, 21, 2, 23]
        elif move == UP_RIGHT:
            m = [9, 8, 2, 3,
                 13, 12, 6, 7,
                 4, 5, 10, 11,
                 0, 1, 14, 15,
                 18, 16, 19, 17,
                 20, 21, 22, 23]
        elif move == UP_LEFT:
            m = [12, 13, 2, 3,
                 8, 9, 6, 7,
                 1, 0, 10, 11,
                 5, 4, 14, 15,
                 17, 19, 16, 18,
                 20, 21, 22, 23]
        else:
            m = range(24)
        for i in range(24):
            self.now[i] = color[m[i]]
        self.record.append(move)
        return self.now

    def equals(self, another):
        if cmp(self.get(), another.get()) == 0:
            return True
        return False

        # def turn(self, move):
        #     color = self.now
        #     if move == RIGHT_UP:
        #         self.now = color[20:23] + color[16:19] + color[8:15] + color[:7]
        #     elif move == RIGHT_DOWN:
        #         self.now = color[16:23] + color[8:15] + color[4:7] + color[:3]
        #     elif move == LEFT_UP:
        #         self.now = color[:7] + color[20:23] + color[16:19] + color[8:15]
        #     elif move == LEFT_DOWN:
        #         self.now = color[:7] + color[16:23] + color[12:15] + color[8:11]
        #     elif move == UP_RIGHT:
        #         self.now = color[8:15] + color[4:7] + color[:4] + color[16:23]
        #     elif move == UP_LEFT:
        #         self.now = color[12:15] + color[8:11] + color[:7] + color[16:23]
