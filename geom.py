#! /usr/bin/env python3

import random

def pmf(k, p):
    return (1 - p)**(k-1) * p

def sample(p):
    k = 1
    while random.random() > p:
        k += 1
    return k

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import util
    NUM_SAMPLES = 100000
    P = .1

    samples = [sample(P) for _ in range(NUM_SAMPLES)]
    n_bins = max(samples) - min(samples) + 1
    plt.hist(samples, bins=n_bins, alpha=.5, label='sampled')
    scounts = util.count(samples)

    artificial_samples=[]
    for k in range(min(samples), max(samples)+1):
        count = pmf(k, P) * len(samples)
        artificial_samples.extend([k]*int(count))
    plt.hist(artificial_samples, bins=n_bins, alpha=.5, label='reference')
    acounts = util.count(artificial_samples)

    for k in range(min(samples), max(samples)+1):
        print(k, scounts[k], acounts[k])

    plt.show()
