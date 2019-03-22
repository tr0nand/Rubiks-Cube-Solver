import sys
from enum import Enum

from pyglet.gl import *
from pyglet.window import key
from pyglet.window.key import symbol_string

from rubiks import Cube, Moves, Speed, History

Macros = {
    key.F1: "U R U' R' U' F' U F",  # solve middle layer (to right)
    key.F2: "U' L' U L U F U' F'",  # solve middle layer (to left)
    key.F3: "R U R' U R U U R'",  # solve top layer
    key.F4: "R B' R F F R' B R F F R R",  # position the yellow corners
    key.F5: "R U' R U R U R U' R' U' R R",
    key.F6: "R U R' U'",
    key.F7: "L' U' L U",
}


class InputMode(Enum):
    Direct = 1
    Command = 2
    CommandDirect = 3


class CubeController(object):
    def __init__(self, cube=None,conf=''):
        self.cube = cube or Cube(conf)
        self.history = History(self.cube)
        self.on_command_changed = []
        self._input_mode = InputMode.Direct
        self._command = ''

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            self._set_command('')
            return pyglet.event.EVENT_HANDLED

        if self._input_mode == InputMode.Direct:
            self._direct_mode(symbol, modifiers)
        if self._input_mode == InputMode.Command:
            self._command_mode(symbol, modifiers)
        if self._input_mode == InputMode.CommandDirect:
            self._command_direct(symbol, modifiers)

    def _set_command(self, command):
        if command == '':
            self._input_mode = InputMode.Direct
        elif command == ':':
            self._input_mode = InputMode.Command

        self._command = command
        for hook in self.on_command_changed:
            hook(self, self._command)

    def _get_command(self):
        command = self._command[1:]  # strip colon
        invert = command and command[0] == '!'
        if invert:
            command = command[1:]  # strip invert
        return command.replace('  ', ' ').strip(), invert

    def _direct_mode(self, symbol, modifiers):
        if symbol == key.COLON:
            self._set_command(':')

        elif symbol_string(symbol) in Moves.keys():
            command = symbol_string(symbol)
            commands = self.cube.create_commands(command)
            self._execute(commands, invert=modifiers & key.MOD_SHIFT)
            self._set_command('')

        elif symbol in Macros.keys():
            commands = self.cube.create_commands(Macros[symbol])
            self._execute(commands, invert=modifiers & key.MOD_SHIFT)
            self._set_command('')

    def _command_mode(self, symbol, modifiers):
        if symbol == key.EXCLAMATION:
            command, invert = self._get_command()
            self._set_command(':{}{}'.format('' if invert else '!', command))

        elif symbol == key.SPACE:
            self._set_command(self._command + ' ')

        elif symbol in [key.S]:
            self._set_command(':shuffle ')

        elif symbol_string(symbol) in Moves.keys():
            self._input_mode = InputMode.CommandDirect
            return

        elif symbol in range(key._0, key._9 + 1):
            self._set_command(self._command + str(symbol - key._0))

        elif symbol == key.Q:
            self._set_command(':quit')

        elif symbol == key.BACKSPACE:
            self._set_command(self._command.strip()[:-1])
            return

        elif symbol == key.ENTER:
            command, invert = self._get_command()
            if command.startswith('shuffle'):
                tokens = command.split(' ')
                count = int(tokens[1]) if len(tokens) > 1 and tokens[1].isnumeric() else 10
                sequence = self.cube.shuffle(count=count)
                commands = self.cube.create_commands(sequence)
                self._execute(commands=commands, speed=Speed.Fast)
            elif command == 'quit':
                sys.exit(0)
            elif command.isnumeric():
                index = int(command) - 1
                commands, speed = self.history.get(index)
                if commands:
                    self._execute(commands=commands, invert=invert, speed=speed)
            self._set_command('')
            return

        self._input_mode = InputMode.Command

    def _command_direct(self, symbol, modifiers):
        if symbol_string(symbol) in Moves.keys():
            command = symbol_string(symbol)
            if modifiers & key.MOD_SHIFT:
                command += "'"
            self._set_command(' '.join([self._command, command]))
            self._input_mode = InputMode.CommandDirect

        elif symbol in range(key._0, key._9 + 1):
            self._set_command(self._command.strip() + str(symbol - key._0))
            self._input_mode = InputMode.CommandDirect

        elif symbol == key.BACKSPACE:
            self._set_command(self._command.strip()[:-1])

        elif symbol == key.ENTER:
            commands = self.cube.create_commands(self._command[1:])
            self._execute(commands=commands)
            self._set_command('')

    def _execute(self, commands, invert=False, history=True, speed=Speed.Medium):
        if not commands:
            return
        if invert:
            commands = [c.invert() for c in commands[::-1]]
        if history:
            self.history.append(commands, speed=speed)
        for command in commands:
            command(speed=speed)

