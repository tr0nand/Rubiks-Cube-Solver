import threading

from pyglet import clock
from pyglet.gl import *

from utils.wavefront import Vector
from .config import *
from .cube import Cube as TextCube


class Piece(object):
    def __init__(self, x, y, z, cube):
        self._cube = cube
        self._position = (x, y, z)
        self._colors = []
        self._position_scale = CubeSize / 3
        self._piece_size = (CubeSize / 6) * PieceScale
        self.apply_colors()

    @property
    def position(self):
        return self._position

    def apply_colors(self):
        self._colors = self._cube.get_colors(*self._position)

    def draw(self):
        glPushMatrix()
        glTranslatef(
            self._position[0] * self._position_scale,
            self._position[1] * self._position_scale,
            self._position[2] * self._position_scale)

        glPushMatrix()
        glScalef(
            self._piece_size,
            self._piece_size,
            self._piece_size)

        color = Colors[0]
        glColor3ub(*Colors[0])
        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, Vector(*[c / 256 * 0.1 for c in color]))
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, Vector(*[c / 256 * 5 for c in color]))
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 0.8)
        RoundedCube.draw()
        glPopMatrix()

        glScalef(
            self._piece_size,
            self._piece_size,
            self._piece_size)

        glEnable(GL_BLEND)
        glEnable(TextureMask.target)
        glBindTexture(TextureMask.target, TextureMask.id)

        for index, face in enumerate(Faces):
            if self._colors[index] == 0:
                continue

            glBegin(GL_QUADS)
            for vertex_index, vertex in enumerate(face):
                color = Colors[self._colors[index]]
                glMaterialfv(GL_FRONT, GL_AMBIENT, Vector(*[c / 256 / 0.2 for c in color]))
                glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, Vector(*[c / 256 / 5 for c in color]))
                glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
                glColor3ub(*Colors[self._colors[index]])
                glTexCoord2f(*TextureUV[vertex_index])
                glVertex3f(
                    Vertices[vertex * 3:vertex * 3 + 3][0] * FacesScale[index][0],
                    Vertices[vertex * 3:vertex * 3 + 3][1] * FacesScale[index][1],
                    Vertices[vertex * 3:vertex * 3 + 3][2] * FacesScale[index][2])
            glEnd()

        glDisable(TextureMask.target)
        glDisable(GL_BLEND)
        glPopMatrix()


class Cube(object):
    """
    Extends the text based cube with OpenGL based 3D rendering and animations.
    """
    def __init__(self, cube=None):
        """ Initializes a new instance of the :class:`Cube` class. """
        self._cube = cube or TextCube()
        self._cube.on_command_created.append(self._on_command_created)
        self._pieces = [Piece(x, y, z, self._cube)
                        for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)
                        if x or y or z]
        self._rotate = [0, 0, 0]
        self._animated = []
        self._speed = None
        self._stable = self._pieces[:]
        self._idle = threading.Event()
        self._idle.set()

    def draw(self):
        """ Performs the 3D drawing and rotation of the currently moving pieces (if any) """
        glPushMatrix()
        [piece.draw() for piece in self._stable]
        glRotatef(self._rotate[0], 1, 0, 0)
        glRotatef(self._rotate[1], 0, 1, 0)
        glRotatef(self._rotate[2], 0, 0, 1)
        [piece.draw() for piece in self._animated]
        glPopMatrix()

    def resize(self, x, y, width, height):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glTexParameteri(TextureMask.target, GL_TEXTURE_WRAP_R, GL_CLAMP_TO_EDGE)
        glTexParameteri(TextureMask.target, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(TextureMask.target, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

    def update(self, command, front, inverse, speed):
        """ Starts the 3D animation for the moved pieces. """
        self._idle.clear()
        if speed == Speed.Immediate:
            self._finish_update()
            return

        axis = Animation[command]['axis']
        direction = speed.value * Animation[command]['dir']
        if not inverse:
            direction = -direction
        self._speed = [0, 0, 0]
        self._speed[axis] = direction

        face = Animation[command]['face']
        for piece in self._pieces:
            if face is None or piece.position[axis] == face:
                self._stable.remove(piece)
                self._animated.append(piece)

        clock.schedule_interval(self._tick, interval=AnimationTick)
        self._idle.wait()

    def _finish_update(self):
        """ Reset the rotation and re-apply the new face colors of the pieces """
        for piece in self._pieces:
            piece.apply_colors()

        self._speed = None
        self._rotate = [0, 0, 0]
        self._animated = []
        self._stable = list(self._pieces)
        self._idle.set()

    def _on_command_created(self, cube, command):
        command.on_updated.append(self.update)

    # noinspection PyUnusedLocal
    def _tick(self, *args, **kwargs):
        """ Scheduler callback used to animate the cube pieces for a move. """
        if self._speed:
            self._rotate[0] = self._rotate[0] + self._speed[0]
            self._rotate[1] = self._rotate[1] + self._speed[1]
            self._rotate[2] = self._rotate[2] + self._speed[2]

        if all(r % 90 == 0 for r in self._rotate):
            clock.unschedule(self._tick)
            self._finish_update()
