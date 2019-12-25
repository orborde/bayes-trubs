#! /usr/bin/env python3

import math
import matplotlib.pyplot as plt
from fractions import Fraction

import geom

def f(x):
    assert x >= 0 and x <= 1

    if x == 1/4 or x == 3/4:
        return math.inf
    elif x < 1/2:
        return math.log2(math.log2(1/abs(x - 1/4)))
    else:
        return 0.25 / abs(x - 3/4)

def trunc_geom_pmf(k, theta):
    if k > f(theta):
        return 0

    return geom.pmf(k, theta)

def posterior(theta, samples):
    pdf = 1
    for k in samples:
        pdf *= trunc_geom_pmf(k, theta)
    return pdf

samples = []
while True:
    sample = geom.sample(1/4)
    print('sampled', sample)
    samples.append(sample)

    for theta in [Fraction(1,4), Fraction(3/4)]:
        print('posterior(',theta,') =', posterior(theta, samples))
    print('posterior(1/4)/posterior(3/4) =',
          posterior(Fraction(1/4), samples) /  posterior(Fraction(3/4), samples))

    points = []
    STEPS=1000
    for x in range(0, STEPS+1):
        p = x/STEPS
        y = posterior(p, samples)
        points.append( (p,y) )

    xs,ys = zip(*points)
    plt.plot(xs, ys)
    plt.waitforbuttonpress()
    plt.close()
