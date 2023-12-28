import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Total population, N.
N = 1000
# Initial number of infected and recovered individuals, I0 and R0.
I0, R0 = 1, 0
# Everyone else, S0, is susceptible to infection initially.
S0 = N - I0 - R0
# Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma = 0.2, 1./10 
# A grid of time points (in days)
t = np.linspace(0, 160, 160)

# The SIR model differential equations.
def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# The Poisson process for contact between infectives and susceptibles.
def poisson_process(A,n,I):
    return np.random.poisson(A/n*I)

# Initial conditions vector
y0 = S0, I0, R0

# Integrate the SIR equations over the time grid, t.
for i in range(1,len(t)):
    # Solve the SIR equations for the next time step using odeint.
    ret = odeint(deriv,y0,[t[i-1],t[i]],args=(N,beta,gamma))
    # Update the initial conditions for the next time step.
    y0 = ret[1]
    # Calculate the number of new infections during this time step.
    new_infections = poisson_process(beta,I0,N)*S0
    # Update the number of infected individuals.
    I0 += new_infections
    # Update the number of susceptible individuals.
    S0 -= new_infections
    # Update the number of recovered individuals.
    R0 += gamma*I0

S,I,R = N-S0-R0,I0,R0

# Plot the data on three separate curves for S(t), I(t) and R(t)
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111)
ax.plot(t,S/1000,'b',alpha=0.5,lw=2,label='Susceptible')
ax.plot(t,I/1000,'r',alpha=0.5,lw=2,label='Infected')
ax.plot(t,R/1000,'g',alpha=0.5,lw=2,label='Recovered with immunity')
ax.set_xlabel('Time /days')
ax.set_ylabel('Number (1000s)')
ax.set_ylim(0,N/1000)
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(b=True)
legend=ax.legend()
legend.get_frame().set_alpha(0.5)

plt.show()