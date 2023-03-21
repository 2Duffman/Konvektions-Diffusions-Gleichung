import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import Aufgabe1

#returns l^2 Norm of give vector subtracted by the exact solution evaluated at the gritpoints
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

#calls calcError for Aufgabe1 and Aufgabe2 for all given values of eps
def calcErrors(eps:float, equation:int):
    errors = []
    for i in (10,100,1000,10000):
        if (equation==1):
            errors.append(calcError(i, eps,Aufgabe1.firstEquation(i, eps)))
        if (equation==2):
            errors.append(calcError(i, eps,Aufgabe1.secondEquation(i, eps)))
    return errors

#plots Errors calculated by calcError function into a scatter plot
def plotError(eps:float):
    fig, ax = plt.subplots()
    e1 = ax.scatter([10,100,1000,10000], calcErrors(eps,1))
    e2 = ax.scatter([10,100,1000,10000], calcErrors(eps,2))
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('N')
    ax.set_ylabel('Fehler')
    fig.legend((e1,e2), ('Verfahren 1', 'Verfahren 2'), loc='upper left')
    plt.savefig(f"./Images/Fehler eps = {eps}.png" )
    plt.close()
