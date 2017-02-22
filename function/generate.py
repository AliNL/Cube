from cube import *


class Leaf(object):
    def __init__(self, cube, parent, move, depth):
        self.cube = cube
        self.parent = parent
        self.move = move
        self.depth = depth


def generate():
    c = Cube("bbbbggggoooorrrryyyywwww")
    cubes = ["bbbbggggoooorrrryyyywwww"]
    records = ['']
    move_cube(c, cubes)
    print cubes, len(cubes)


def move_cube(c, cubes):
    for i in range(6):
        c.now = c.move(i)
        if c.get() not in cubes:
            cubes.append((c.get()))
            # records.append(c.get_record())
            return move_cube(c, cubes)


generate()
