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


    character   line style

    "."         point marker
    ","         pixel marker
    "o"         circle marker
    "v"         triangle_down marker
    "^"         triangle_up marker
    "<"         triangle_left marker
    ">"         triangle_right marker
    "1"         tri_down marker
    'x'         x marker
    'H'         hexagon1 marker
    'h'         hexagon2 marker
    'D'         diamond marker

'''
x=[1, 2, 3, 4]
plt.plot(x, np.power(x, 2), color='r', marker='^', linestyle=':',linewidth=1)
plt.plot(x, np.power(x, 3), color='g', marker='o', linestyle='-.',linewidth=1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y=x^2')
plt.show()
