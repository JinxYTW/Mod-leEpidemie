import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import numpy as np

def dAdt(A, t, beta, gamma, N):
    """
    Calcule les équations différentielles du modèle SIR en fonction du temps

    Args:
        A (list): Contient les valeurs S, I et R initiales.
        t (float): Le temps (en jour)
        beta (float): Le taux de transmission 
        gamma (float): Le taux de rémission
        N (float): La taille totale de la population

    Returns:
        list: Contient S, I et R en fonction du temps
    """
    S= A[0]
    I = A[1]
    R = A[2]
    return [
        -beta/N * S * I,
        beta/N * S * I - gamma * I,
        gamma*I
    ]

# Construit les différentes valeurs pour l'axe des abscisses
times = np.arange(0, 100, 1) # De 0 à 100 par pas de 1

# Population totale
N = 1.1e7
# Probabilité d'être rétablis au jour suivant (t + 1)
gamma = 1/10
# Probabilité d'être infecté au jour suivant (t + 1)
beta = 0.2
# Quantité de personne infectée initiale et contagieuse
I0 = 574
# Quantité de personne susceptible d'être infectée
S0 = N - I0
# Quantité de personne rétabli
R0 = 0

# Résout les équations différentielles
sol = odeint(dAdt, y0=[S0, I0, R0], t=times, args=(beta, gamma, N))

S = sol.T[0] # Personnes susceptible d'être infectées
I = sol.T[1] # Personnes infectées
R = sol.T[2] # Personnes rétablies

# Affichage des courbes sur le même graphique
plt.plot(times, S, label='Susceptibles (non infectée)')
plt.plot(times, I, label='Infectées')
plt.plot(times, R, label='Rétablies')
plt.grid()