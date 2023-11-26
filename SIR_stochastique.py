import numpy as np
import matplotlib.pyplot as plt
import random
import math

S, I, R = 100, 1, 0
N = S + I + R

beta = 0.04
gamma = 0.01

def sir(SIR, params, dt):
    
    beta, gamma, N = params

    S,I,R = SIR
    
    # proportion de la quantité de personnes passant de S à I 
    prop = beta*I*S/N

    # La probabilité d'infectés et de réémis est exponentielle en fonction du temps 
    ifrac = 1.0 - math.exp(-prop*dt)
    rfrac = 1.0 - math.exp(-gamma*dt)

    # Renvoie le nombre de succés de la loi binomiale
    infection = np.random.binomial(S,ifrac)
    recovery = np.random.binomial(I,rfrac)

    return [S-infection,I+infection-recovery,R+recovery]

def simulate(beta, gamma, I0, N, tempsMax):
    params = beta, gamma, N
    #temps = np.arange(1, 100)
    t = 1
    SIR = [[N-I0*N], [I0*N], [0]]
    tend = 500
    while t < tempsMax:
        S, I, R = sir([SIR[0][-1], SIR[1][-1], SIR[2][-1]], params, t)
        SIR[0].append(S)
        SIR[1].append(I)
        SIR[2].append(R)
        t += 1

    temps = np.arange(1, t+1)
    
    plt.plot(temps, SIR[0], label='Susceptibles (non infectées)')
    plt.plot(temps, SIR[1], label='Infectées')
    plt.plot(temps, SIR[2], label='Rétablies')
    plt.xlabel('Temps (jours)')
    plt.ylabel('Population')
    plt.legend()
    plt.grid()
    plt.show() 
