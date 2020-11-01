from brain import *
from input import *

"""
ONLY RUN HERE  
IT WILL ASK YOU TO SET START AND TARGET AND THEN YOU CAN DRAW
WALLS USING THE MOUSE AND THEN PRESS SPACE KEY  
"""

size_of_pixel = 20
input_val = Input(size_of_pixel)

input_val.run()
x1 = input_val.x1
y1 = input_val.y1
x2 = input_val.x2
y2 = input_val.y2
if x1 and y1 and x2 and y2 and not (x1 == y1 and y1 == x2 and x2 == y2):
    sett = Settings(size_of_pixel)
    sett.run(x1, y1, x2, y2)


