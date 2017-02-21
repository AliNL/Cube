from function.cube import *
import unittest


class TestCube(unittest.TestCase):
    def test_output_should_be_same_as_input(self):
        cube = Cube("bbbbggggoooorrrryyyywwww")
        self.assertEqual("bbbbggggoooorrrryyyywwww", cube.get())
        cube = Cube("rrbbyyggbbooggrryyyywwww")
        self.assertEqual("rrbbyyggbbooggrryyyywwww", cube.get())

    def test_move_right_up_and_down(self):
        cube = Cube("bbbbggggoooorrrryyyywwww")
        cube.move(RIGHT_UP)
        cube.move(RIGHT_DOWN)
        self.assertEqual("bbbbggggoooorrrryyyywwww", cube.get())

    def test_move_left_up_and_down(self):
        cube = Cube("bbbbggggoooorrrryyyywwww")
        cube.move(LEFT_UP)
        cube.move(LEFT_DOWN)
        self.assertEqual("bbbbggggoooorrrryyyywwww", cube.get())

    def test_move_up_left_and_right(self):
        cube = Cube("bbbbggggoooorrrryyyywwww")
        cube.move(UP_LEFT)
        cube.move(UP_RIGHT)
        self.assertEqual("bbbbggggoooorrrryyyywwww", cube.get())


if __name__ == '__main__':
    unittest.main()
