def animator(input, nx, its):
    import numpy as np
    from matplotlib import pyplot as plt
    from matplotlib import animation

    #Making the figure
    fig = plt.figure()
    ax = plt.axes(xlim=(0,1), ylim=(-1,1))
    line, = ax.plot([], [], lw=2)

    #Initialization
    def init():
        line.set_data([], [])
        return line,

    #Animation function
    def animate(i):
        x = np.linspace(0, 1, nx)
        y = input[i,:]
        line.set_data(x,y)
        return line,

    #Call the animator
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames = its, interval = 500, blit=True)

    plt.show()
