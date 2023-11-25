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

params = beta, gamma, N
for dt in range(1, 200, 0.1):
      SIR = sir(SIR, params, dt)

