import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import Aufgabe1


def calcError(N:int, eps:float, calculatedPoints):
    calculatedPoints2 = [0] + list(calculatedPoints) + [0]
    dx=1/N
    uHat=[]
    for i in (range(N+1)):
        uHat.append(Aufgabe1.given_solution(i*dx , eps))
    res = 0
    for i in (range(N+1)):
        res += dx* (uHat[i]-calculatedPoints2[i])**2
    return np.sqrt(res)

def plotError(eps:float, equation:int):
    fig = plt.figure()
    ax = fig.add_subplot(2, 1, 1)
    plt.scatter([10,100,1000,10000], calcErrors(eps, equation))
    plt.title("Fehler für \u03B5=%.4f"%eps+", Verfahren %d" %equation)
    ax.set_xscale('log')
    plt.savefig(f"./Images/Fehler eps = {eps} Verfahren {equation}.png" )

def calcErrors(eps:float, equation:int):
    errors = []
    for i in (10,100,1000,10000):
        if (equation==1):
            errors.append(calcError(i, eps,Aufgabe1.firstEquation(i, eps)))
        if (equation==2):
            errors.append(calcError(i, eps,Aufgabe1.secondEquation(i, eps)))
    return errors

for i in (1,2):
    for eps in (0.5,0.05,0.005,0.0005):
        plotError(eps,i)