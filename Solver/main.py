#!/usr/bin/env python3

from pyglet.gl import *
from pyglet.window import NoSuchConfigException
import pyautogui
from rubiks import CubeController, CubeView
import parser
import cube
#import kociemba
import time
import threading
#import video
def solveCube(solved):
    s = ''
    for command in solved.split():
        if len(command) == 1:
            s += command[0].lower()
        elif command[1] == "'":
            s += command[0].upper()
        elif command[1] == '2':
            s += command.lower() * 2
    time.sleep(5)
    pyautogui.typewrite(s, interval=0.5)

if __name__ == '__main__':
    
    
    c = cube.Cube()
    c.scrambler(5)
    c.display()
    #solved = kociemba.solve(parser.parser_cube2solver(c.getConfig()))
    
    solved="F2 B"
    config = parser.parser_2dto3d(c.getConfig())
    print(solved)
    controller = CubeController(conf=config)

    platform = pyglet.window.get_platform()
    display = platform.get_default_display()
    screen = display.get_default_screen()
    try:
        template = pyglet.gl.Config(depth_size=24, sample_buffers=1, samples=4)
        config = screen.get_best_config(template)
    except NoSuchConfigException:
        config = screen.get_best_config()

    window = pyglet.window.Window(width=1024, height=768, caption="The Rubik's Cube", resizable=True, config=config)
    window.push_handlers(controller.on_key_press)
    view = CubeView(controller, window)
    t = threading.Thread(target=solveCube, args = (solved, ))
    t.start()
    pyglet.app.run()
