import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

# Définit les équations
def dAdt(A, t, beta, gamma, N):
    S= A[0]
    I = A[1]
    R = A[2]
    return [
        -beta/N * S * I,
        beta/N * S * I - gamma * I,
        gamma*I
    ]
	
# Résout les équations différentielles
def solveEq(gamma = 0.1, beta = 0.7, population = 10000, infectees = 1, tmax=100):
	S, I, R = population - infectees, infectees, 0
	# Chaque indice dans S,I et R correspondra à un jour
	temps = np.arange(0, tmax, 1) # De 0 à tmax par pas de 1
	res = odeint(dAdt, y0=[S, I, R], t=temps, args=(beta, gamma, population))
	S, I, R, t = res.T[0], res.T[1], res.T[2], temps
	return S, I, R, t

# Affichage graphique
def show(S, I, R, temps):
    plt.plot(temps, S, label='Susceptibles (non infectées)')
    plt.plot(temps, I, label='Infectées')
    plt.plot(temps, R, label='Rétablies')
    plt.xlabel('Temps (jours)')
    plt.ylabel('Population')
    plt.title("Modélisation déterministe")
    plt.legend()
    plt.grid()
    plt.show()

# Lance la simulation (utilisé dans jupyter avec la fonction interact)
def solveAndShow(gamma = 0.1, beta = 0.7, population = 10000, infectees = 1, tmax=100):
    S,I,R,t=solveEq(gamma, beta, population, infectees, tmax)
    R0 = I[int(1/gamma)] # On prend la moyenne en jour
    show(S,I,R,t)
    return S,I,R,R0
	
solveAndShow()
