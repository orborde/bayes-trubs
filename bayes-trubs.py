#! /usr/bin/env python3

import math
import matplotlib.pyplot as plt

def f(x):
    assert x >= 0 and x <= 1

    if x == 1/4 or x == 3/4:
        return math.inf
    elif x < 1/2:
        return math.log2(math.log2(1/abs(x - 1/4)))
    else:
        return 0.25 / abs(x - 3/4)


points = []
STEPS=1000
for x in range(0, STEPS+1):
    x = x/STEPS
    y = f(x)
    points.append( (x,y) )

xs,ys = zip(*points)
plt.plot(xs, ys)
plt.axis([0,1, 0,30])
plt.show()
