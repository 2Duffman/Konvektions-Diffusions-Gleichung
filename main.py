import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import Aufgabe1
import Aufgabe3
import Aufgabe2

Ns = [10, 100, 1000, 10000]
epss = [0.5, 0.05, 0.005, 0.0005]
for eps in epss:
    for N in Ns:
        Aufgabe2.plot_stuff(N,eps)



for eps in epss:
    Aufgabe3.plotError(eps)