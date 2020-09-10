from brain import *
from input import *

"""
ONLY RUN HERE  
IT WILL ASK YOU TO SET START AND TARGET AND THEN YOU CAN DRAW
WALLS USING THE MOUSE AND THEN PRESS SPACE KEY  
"""

input_val = Input()
input_val.run()
x1 = input_val.x1
y1 = input_val.y1
x2 = input_val.x2
y2 = input_val.y2
sett = Settings()
sett.run(x1, y1, x2, y2)

