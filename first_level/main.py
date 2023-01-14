import math
import random

from Classes import *

line_list = [Line(Point(random.randint(0, 900), random.randint(0, 900)),
                  Vector(random.randint(0, 900), random.randint(0, 900)))]

for i in line_list:
    print(i.get_point_along_line(math.pi / 4), i.get_derivative())
    

ellipse_list = [Ellipse(random.randint(0, 900), random.randint(0, 900))]

for i in ellipse_list:
    print(i.get_point_along_line(math.pi / 4), i.get_derivative(math.pi / 4))
