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
    plt.scatter([1,10,100,1000,10000], calcErrors(eps, equation))
    plt.show()

def calcErrors(eps:float, equation:int):
    errors = []
    for i in (1,10,100,1000,10000):
        if (equation==1):
            errors.append(calcError(i, eps,Aufgabe1.firstEquation(i, eps)))
        if (equation==2):
            errors.append(calcError(i, eps,Aufgabe1.secondEquation(i, eps)))
    return errors
plotError(0.5,1)