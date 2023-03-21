import numpy as np
from scipy import sparse
import matplotlib.pyplot as plt
import Aufgabe1

#plottet beide Verfahren und die exakte Lösung in ein Diagramm für gegebenes N und eps
def plot_curves(N, eps):
    approx_first = [0] + list(Aufgabe1.firstEquation(N, eps)) + [0]
    approx_second = [0] + list(Aufgabe1.secondEquation(N, eps)) + [0]
    exact_solution =  [Aufgabe1.given_solution(i * (1/10000), eps) for i in range(10000)] + [0]
    xs = [i * (1/N) for i in range(N)] + [1]
    xs2 = np.linspace(0, 1, 10001)
    fig, ax = plt.subplots()
    l1, = ax.plot(xs2, exact_solution)
    l2, = ax.plot(xs, approx_first)
    l3, = ax.plot(xs, approx_second)
    ax.set_title(f"N = {N}, eps = {eps}")
    fig.legend((l1, l2, l3), ('Exakte Lösung', 'Verfahren 1', 'Verfahren 2'), loc='upper left')
    #speichert den Plot als Bild ab
    plt.savefig(f"./Images/Lösungen N = {N}, eps = {eps}.png" )
    plt.close()
