from matplotlib import pyplot as plt
import numpy as np


# x=[1, 2, 3, 4]
# plt.plot(x,np.power(x,2))
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('y=x^2')
# plt.show()

'''	
    character   color

    blue        b
    green       g
    red         r
    cyan        c
    magenta     m
    yellow      y
    black       k
    white       w


    Marker	Description

    .	Point
    ,	Pixel
    o	Circle
    v	Triangle Down
    ^	Triangle Up
    <	Triangle Left
    >	Triangle Right
    1	Tri-down (Tripod Down)
    2	Tri-up (Tripod Up)
    3	Tri-left (Tripod Left)
    4	Tri-right (Tripod Right)
    s	Square
    p	Pentagon
    *	Star
    h	Hexagon1
    H	Hexagon2
    +	Plus
    x	X
    D	Diamond
    d	Thin Diamond
    `	`
    _	Horizontal Line
    
    Line Style Code	   Description
    
    '-'	               Solid Line
    '--'	           Dashed Line
    '-.'	           Dash-Dot Line
    ':'	               Dotted Line
    ''                 (empty)	No Line




'''
x=[1, 2, 3, 4]
plt.plot(x, np.power(x, 2), color='r', marker='^', linestyle=':',linewidth=1)
plt.plot(x, np.power(x, 3), color='g', marker='o', linestyle='-.',linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=x^2')
plt.show()
