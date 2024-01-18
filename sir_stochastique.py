# Version stochastique
def sir(u, parms, t):
    bet, gamm, iota, N, dt = parms
    S, I, R = u

    # Calcul du taux d'infection
    lambd = bet * (I + iota) / N

    # Calcul des fractions d'infection et de récupération
    ifrac = 1.0 - math.exp(-lambd * dt)
    rfrac = 1.0 - math.exp(-gamm * dt)

    # La binomial fait intervenir l'aspect aléatoire du modèle
    infection = np.random.binomial(S, ifrac)
    recovery = np.random.binomial(I, rfrac)

    # Mise à jour des compartiments S, I, R selon le modèle SIR
    return [S - infection, I + infection - recovery, R + recovery]

# Simulation
def simu(gamma, beta, I0, N):
    parms = [beta, gamma, 0.01, N, 0.1]
    step = 0.1
    
    #parms = [beta, gamma, 0.01, N, step]
    
    sampleCount = 1000
    tempsMax = 100
    
    t = np.linspace(0, tempsMax, sampleCount)
    S = np.zeros(sampleCount)
    I = np.zeros(sampleCount)
    R = np.zeros(sampleCount)
   
    u = [N-I0, I0, 0]
    S[0],I[0],R[0] = u
    for j in range(1, sampleCount):
        u = sir(u,parms,t[j])
        S[j],I[j],R[j] = u
    return S, I, R, t

# Affichage
def plot(gamma=0.1, beta=0.7, I0=1, N=1000):
    S, I, R, t = simu(gamma, beta, I0, N)
    plt.plot(t, S, label='Susceptibles (non infectées)')
    plt.plot(t, I, label='Infectées')
    plt.plot(t, R, label='Rétablies')
    plt.xlabel('Temps (jours)')
    plt.ylabel('Population')
    plt.title("Modélisation stochastique")
    plt.legend()
    plt.grid()
    plt.show()

    print(abs(R[0] - R[100]) / N)
    
    return S, I, R, t
plot()