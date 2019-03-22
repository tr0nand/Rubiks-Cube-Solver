#! /usr/bin/env python3

import cube
import math
import random

def parser_cube2solver(config):
    cubestring = ""
    temp = []
    for i in config:
        if i == 0:
            temp.append("F")
        elif i == 1:
            temp.append("R")
        elif i == 2:
            temp.append("B")
        elif i == 3:
            temp.append("L")
        elif i == 4:
            temp.append("U")
        elif i == 5:
            temp.append("D")
    temp = [temp[i : i + 9] for i in range(0, len(temp), 9)]
    temp2 = []
    temp2.extend(temp[cube.Side.U])
    temp2.extend(temp[cube.Side.R])
    temp2.extend(temp[cube.Side.F])
    temp2.extend(temp[cube.Side.D])
    temp2.extend(temp[cube.Side.L])
    temp2.extend(temp[cube.Side.B])
    cubestring = ''.join(temp2)
    return cubestring

def parser_2dto3d(conf):
    cubestring = ""
    for i in range(len(conf)):
        if conf[i] == cube.Color.RED:
            conf[i] = 3
        elif conf[i] == cube.Color.BLUE:
            conf[i] = 4
        elif conf[i] == cube.Color.ORANGE:
            conf[i] = 5
        elif conf[i] == cube.Color.GREEN:
            conf[i] = 2
        elif conf[i] == cube.Color.WHITE:
            conf[i] = 1
        elif conf[i] == cube.Color.YELLOW:
            conf[i] = 6
    config_parts = [conf[i:i+9] for i in range(0, 54, 9)]
    temp = []
    config_parts[cube.Side.B][0], config_parts[cube.Side.B][2] = config_parts[cube.Side.B][2], config_parts[cube.Side.B][0]
    config_parts[cube.Side.B][3], config_parts[cube.Side.B][5] = config_parts[cube.Side.B][5], config_parts[cube.Side.B][3]
    config_parts[cube.Side.B][6], config_parts[cube.Side.B][8] = config_parts[cube.Side.B][8], config_parts[cube.Side.B][6]
    temp.extend(config_parts[cube.Side.U])
    temp.extend(config_parts[cube.Side.L])
    temp.extend(config_parts[cube.Side.F])
    temp.extend(config_parts[cube.Side.R])
    temp.extend(config_parts[cube.Side.B])
    temp.extend(config_parts[cube.Side.D])
    cubestring = ' '.join(map(str, temp))
    return cubestring
