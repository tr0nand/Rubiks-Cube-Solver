from pyglet.gl import *
from pyglet.window import key

from rubiks import Cube2D, Cube3D
from rubiks.config import Background, CubeSize
from utils.wavefront import Vector


class CubeView(object):
    def __init__(self, controller, window):
        controller.on_command_changed.append(self._on_command_changed)
        self._cube = controller.cube
        self._cube2d = Cube2D(self._cube)
        self._cube3d = Cube3D(self._cube)
        self._history = controller.history
        self._command = pyglet.text.Label('')
        self._view_x = 30
        self._view_y = -30
        self._window = window
        self._window.push_handlers(
            self.on_draw,
            self.on_key_press,
            self.on_resize)

    def on_draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # self._draw_history()
        self._draw_2d()
        self._draw_3d()
        glFlush()

    def on_resize(self, width, height):
        glClearColor(*Background)
        glShadeModel(GL_SMOOTH)
        glViewport(0, 0, width, height)
        self._cube2d.resize(0, height - CubeSize, width // 2, CubeSize)
        self._cube3d.resize(0, 0, width, height)
        self._history.resize(30, 30, width, height - CubeSize * 3 - 30)
        self._command.x = 30
        self._command.y = 10
        glFlush()

    def on_key_press(self, symbol, modifiers):
        if symbol in [key.UP, key.DOWN, key.LEFT, key.RIGHT]:
            self._view_x += -15 if symbol == key.UP else 15 if symbol == key.DOWN else 0
            self._view_y += -15 if symbol == key.LEFT else 15 if symbol == key.RIGHT else 0

        elif symbol == key.HOME:
            self._view_x = 30
            self._view_y = -30

    def _on_command_changed(self, controller, command):
        self._command.text = command

    def _draw_2d(self):
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self._window.width, 0, self._window.height, 0, 8192)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glPushMatrix()
        glTranslatef(10, self._window.height - 10, 0)
        self._cube2d.draw()
        glPopMatrix()

    def _draw_3d(self):
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(35, self._window.width / self._window.height, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        #draw light
        glLightfv(GL_LIGHT0, GL_POSITION, Vector(10, 30, 50))
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glPushMatrix()
        glTranslatef(50, -20, -400)
        glRotatef(self._view_x, 1, 0, 0)
        glRotatef(self._view_y, 0, 1, 0)
        self._cube3d.draw()
        glPopMatrix()

        glDisable(GL_LIGHTING)

    def _draw_history(self):
        glDisable(GL_DEPTH_TEST)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, self._window.width, 0, self._window.height, 0, 8192)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        glPushMatrix()
        self._history.draw()
        glPopMatrix()

        self._command.draw()
