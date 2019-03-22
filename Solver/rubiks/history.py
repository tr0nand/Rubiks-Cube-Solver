import pyglet
from pyglet.gl import *

from .config import Speed


class History(object):
    def __init__(self, cube):
        self._cube = cube
        self._commands = []
        self._batch = pyglet.graphics.Batch()
        self._document = pyglet.text.document.FormattedDocument()
        self._document.text = '\n'
        self._layout = pyglet.text.layout.ScrollableTextLayout(self._document, 100, 100, multiline=True, batch=self._batch)
        self._position = (0, 0)
        self._size = (1, 1)

    def append(self, commands, speed=Speed.Medium):
        self._commands.append((commands, speed))
        self._update()

    def get(self, index):
        if len(self._commands) <= index:
            return None, None
        return self._commands[index]

    def resize(self, x, y, width, height):
        self._position = (x, y)
        self._size = (width, height)
        self._update()

    def _update(self):
        if self._document.text:
            self._layout.x = self._position[0]
            self._layout.y = self._position[1]
            self._layout.width = self._size[0]
            self._layout.height = self._size[1]

        text = ''
        for i, commands in enumerate(self._commands):
            if not commands[0]:
                continue
            command = ' '.join(['{}'.format(c) for c in commands[0]])
            text += '{}: {}\n'.format(i + 1, command)

        self._document.text = text
        self._document.set_style(0,len(self._document.text),dict(color=(255,255,255,255)))

        self._layout.view_y = -self._layout.content_height
        self._layout.end_update()


    def draw(self):
        self._batch.draw()
