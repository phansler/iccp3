import numpy as np
def creator(nx):
    mu = 0.5
    sigma = 0.1
    x=np.linspace(0, 1, nx, 'complex')
    V=x
    psi = 0.5*np.exp(-(x-mu)**2 / (2 * sigma**2))
    V[:]=0
    V[-3:-1]=5
    print(V)
    return psi, V
