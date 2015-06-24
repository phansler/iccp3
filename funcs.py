def simulation(nx, its, dt, psi, V):

    import numpy as np
    import scipy.sparse.linalg as sp

    dx = np.divide(1.0, nx)
    absdata = np.zeros((its+1, nx))
    angdata = np.zeros((its+1, nx))

    # Force boundaries
    m = 1  # Mass
    absdata[0, :] = np.absolute(psi)
    angdata[0, :] = np.angle(psi)
    """
    We want to solve the system A * psi [t+1] = B * psi [t]
    Here A = 1-iH * dt/2, B = 1 + iH * dt/2.
    Note hbar = 1
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

    #  Periodic boundary conditions
    B[0, -1] = diagoneB[0]
    B[-1, 0] = diagoneB[0]
    A[0, -1] = diagoneA[0]
    A[-1, 0] = diagoneA[0]

    for t in range(its):
        newb = np.dot(B, psi)
        psi, info = sp.bicgstab(A, newb)
        absdata[t+1, :] = np.absolute(psi)
        angdata[t+1, :] = np.angle(psi)

    return absdata, angdata

def ic(nx):
    import numpy as np
    mu = 0.5
    p = 10
    sigma = 0.1
    x = np.linspace(0, 1, nx, 'complex')
    V = x
    psi = 0.5*np.exp(-(x-mu)**2 / (2 * sigma**2) + 1j*p*x)
    V[:]=0
    print(nx)
    V[12*nx/16:14*nx/16] = 100000
    print(V)
    return psi, V

def animator(inputvec, nx, its):
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import animation

    #  Making the figure
    fig = plt.figure()
    ax = plt.axes(xlim=(0,1), ylim=(-1,1))
    line, = ax.plot([], [], lw=2)

    #  Initialization
    def init():
        line.set_data([], [])
        return line,

    #  Animation function
    def animate(i):
        x = np.linspace(0, 1, nx)
        y = inputvec[i,:]
        line.set_data(x,y)
        return line,

    #  Call the animator
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames = its, interval = 50, blit=True)

    plt.show()
