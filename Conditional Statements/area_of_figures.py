import math
from math import pi

figure= input()
square="square"
rectangle="rectangle"
circle="circle"
triangle="triangle"

if figure==square:
    side=float(input())
    area=side**2
    print(area)
elif figure==rectangle:
    side1=float(input())
    side2=float(input())
    area=side1*side2
    print(area)
elif figure==circle:
    radius=float(input())
    area=pi*(radius**2)
    print(area)
elif figure==triangle:
    side=float(input())
    height=float(input())
    area=(side*height)/2
    print(area)