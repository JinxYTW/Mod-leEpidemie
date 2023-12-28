import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import numpy as np

def dAdt(A, t, beta, gamma, N):
    """
    Calculates the derivative of the SIR model with respect to time.

    Args:
        A (list): A list containing the current values of S, I, and R.
        t (float): The current time.
        beta (float): The transmission rate.
        gamma (float): The recovery rate.
        N (float): The total population.

    Returns:
        list: A list containing the derivatives of S, I, and R with respect to time.
    """
    S= A[0]
    I = A[1]
    R = A[2]
    return [
        -beta/N * S * I,
        beta/N * S * I - gamma * I,
        gamma*I
    ]

times = np.arange(0, 100, 1)
gamma = 1/10
N = 1.1e7
beta = 0.39
S0, I0, R0 = N-574, 574, 0
sol = odeint(dAdt, y0=[S0, I0, R0], t=times, args=(beta, gamma, N))

S = sol.T[0]
I = sol.T[1]
R = sol.T[2]

plt.plot(times, S)
plt.plot(times, I)
plt.plot(times, R)
plt.grid()