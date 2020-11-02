from brain import *
from input import *


size_of_pixel = 20
input_val = Input(size_of_pixel)
input_val.run()
x1 = input_val.x1
y1 = input_val.y1
x2 = input_val.x2
y2 = input_val.y2
if x1 and x2 and y1 and y2:
    sett = Dijkstra(size_of_pixel)
    sett.run(x1, y1, x2, y2)



