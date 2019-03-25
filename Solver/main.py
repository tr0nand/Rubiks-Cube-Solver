#!/usr/bin/env python3
import cv2
import os
from average import average_color
from knn import colorrec
import pycuber as pc
from pycuber.solver import CFOPSolver
from time import sleep

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
    directory = 'img'
    if not os.path.isdir(directory):
        os.mkdir(directory)
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    img_counter = 0
    xpos = 125
    ypos = 185
    size = 50
    faces_solve = []
    colpredict = colorrec()
    while rval and img_counter !=6:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 32:
            imgname = "img"+str(img_counter)+".png"
            frame = frame[ypos:ypos + 3*size,xpos:xpos+3*size]
            cv2.imwrite(os.path.join(directory,imgname), frame)
            print("Face {} taken".format(img_counter+1))
            cubeFace = average_color(frame)
            col1 = cubeFace.face1()
            col2 = cubeFace.face2()
            col3 = cubeFace.face3()
            col4 = cubeFace.face4()
            col5 = cubeFace.face5()
            col6 = cubeFace.face6()
            col7 = cubeFace.face7()
            col8 = cubeFace.face8()
            col9 = cubeFace.face9()
            faces = []
            faces.append(str(colpredict.color(col1)))
            faces.append(str(colpredict.color(col2)))
            faces.append(str(colpredict.color(col3)))
            faces.append(str(colpredict.color(col4)))
            faces.append(str(colpredict.color(col5)))
            faces.append(str(colpredict.color(col6)))
            faces.append(str(colpredict.color(col7)))
            faces.append(str(colpredict.color(col8)))
            faces.append(str(colpredict.color(col9)))
            cubeFace.makeface(faces,size,img_counter)
            print(faces)
            k = input('Is this face correct?(Y/N)\n')
            if str(k) == str('N'):
                img_counter = img_counter - 1
            else:
                for i in range(9):
                    faces_solve.append(faces[i][2])
                #print(faces)
                print(faces_solve)
                img_counter = img_counter + 1

        else:
            cv2.rectangle(img=frame, pt1=(xpos, ypos),pt2=(xpos+size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + size, ypos),pt2=(xpos + 2*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos),pt2=(xpos + 3*size,ypos+size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos, ypos + size),pt2=(xpos+size,ypos+ 2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + size, ypos + size),pt2=(xpos + 2*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + size),pt2=(xpos + 3*size,ypos+2*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos, ypos + 2*size),pt2=(xpos+size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + size, ypos+2*size),pt2=(xpos + 2*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)
            cv2.rectangle(img=frame, pt1=(xpos + 2*size, ypos + 2*size),pt2=(xpos + 3*size,ypos+3*size), color=(255, 0, 0), thickness=2, lineType=8, shift=0)

    vc.release()
    cv2.destroyWindow("preview")
    faces_solve=['g', 'g', 'g', 'r', 'r', 'r', 'r', 'r', 'r', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'o', 'o', 'o', 'g', 'g', 'g', 'g', 'g', 'g', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'o', 'o', 'o', 'o', 'o', 'o', 'r', 'r', 'r', 'b', 'b', 'b', 'b', 'b', 'b']

    #print(faces_solve)

    array_default = '000000000111111111222222222333333333444444444555555555'

    faces_solve = ''.join(faces_solve)
    array = faces_solve

    cube_default = pc.Cube()

    cubie = pc.array_to_cubies(array)

    cube_main = pc.Cube(cubie)

    print(cube_main)

    solver = CFOPSolver(cube_main)

    steps = solver.solve()

    step_list = list(steps)
    print(steps)
    print(len(steps))

    cube_solve = pc.Cube(cubie)

    c = cube.Cube()
    c.scrambler(steps)
    c.display()
    #solved = kociemba.solve(parser.parser_cube2solver(c.getConfig()))
    
    solved=str(steps)
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
