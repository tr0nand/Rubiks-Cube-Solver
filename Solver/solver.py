import pycuber as pc
from pycuber.solver import CFOPSolver
from time import sleep
#from webcam import faces
# faces after detection can be imported here to solve the cube

array_default = '000000000111111111222222222333333333444444444555555555'

array = 'yyyrggowwbyogybgoyrygoorrwrggbbwgwwooowwbrwrybbryrbbog'

cube_default = pc.Cube()

cubie = pc.array_to_cubies(array)

cube_main = pc.Cube(cubie)

print(cube_main)

#cube_main

solver = CFOPSolver(cube_main)

steps = solver.solve()
#steps = steps.mirror()

step_list = list(steps)
print(steps)
print(len(steps))

cube_solve = pc.Cube(cubie)

for i in range(len(step_list)):
    cube_solve(steps[i])
    print(cube_solve)
    sleep(0.3)
