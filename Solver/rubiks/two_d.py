from pyglet.gl import *

from .config import *
from .cube import Cube as TextCube


class Face(object):
    def __init__(self, index, cube):
        self._cube = cube
        self._index = index
        self._face = self._index // 9

    def draw(self):
        glPushMatrix()

        glScalef(CubeSize // 4, CubeSize // 4, 1)
        if self._face == 0:
            x_offset = 3.5 + self._index % 3
            y_offset = (self._index - self._face * 9) // 3
        elif self._face == 4:
            x_offset = 10.5 + 2 - (self._index % 3)
            y_offset = 3.5 + (self._index - self._face * 9) // 3
        elif self._face == 5:
            x_offset = 3.5 + self._index % 3
            y_offset = 7 + (self._index - self._face * 9) // 3
        else:
            x_offset = (self._face - 1) * 3.5 + self._index % 3
            y_offset = 3.5 + (self._index - self._face * 9) // 3
        glTranslatef(1 + x_offset, -2 - y_offset, 0)

        glColor3ub(*Colors[self._cube.faces[self._index]])
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(0, .9)
        glVertex2f(.9, .9)
        glVertex2f(.9, 0)
        glEnd()

        glPopMatrix()


class Cube(object):
    def __init__(self, cube=None):
        self._cube = cube or TextCube()
        self._faces = [Face(i, self._cube) for i in range(54)]

    def create_commands(self, commands):
        """ Create :class:Command: instances for all given cube notation commands """
        return self._cube.create_commands(commands)

    def draw(self):
        for face in self._faces:
            face.draw()

    def resize(self, x, y, width, height):
        pass
