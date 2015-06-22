def updater(nx, its, dt, psi, V):

    import numpy as np
    import scipy.sparse.linalg as sp

    dx = np.divide(1.0, nx)
    absdata = np.zeros((its+1, nx))
    angdata = np.zeros((its+1, nx))

    # Force boundaries
    psi[0] = 0
    psi[-1] = 0
    m = 1  # Mass
    absdata[0, :] = np.absolute(psi)
    angdata[0, :] = np.angle(psi)
    """
    We want to solve the system A * psi [t+1] = B * psi [t]
    Here A = 1-iH * dt/2, B = 1 + iH * dt/2.
    Note in our case so far, dx=dt=1 ,hbar = 1
    """
    # Initialization of Crank-Nicholson Matrix
    diagzeroA = 1 - dt / (2 * 1j * m * dx**2) - (dt / (2 * 1j)) * V
    diagoneA = dt / (4 * 1j * m * dx**2) * np.ones(nx-1)
    diagzeroB = -1 * diagzeroA + 2
    diagoneB = -1 * diagoneA

    def tridiagmatcreator(a, b, c, k1=-1, k2=0, k3=1):
        return np.diag(a, k1) + np.diag(b, k2) + np.diag(c, k3)

    A = tridiagmatcreator(diagoneA, diagzeroA, diagoneA)
    B = tridiagmatcreator(diagoneB, diagzeroB, diagoneB)

    for x in range(its):
        newb = np.dot(B, psi)
        psi = sp.bicgstab(A, newb)
        absdata[x+1, :] = np.absolute(psi[0])
        angdata[x+1, :] = np.angle(psi[0])

    return absdata, angdata






















