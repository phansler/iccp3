import funcs

nx = 500   #Space points
its = 1000   #Time points
dt = 0.001  #Time spacing

psi, V = funcs.ic(nx)

absdata, angdata = funcs.simulation(nx, its, dt, psi, V)  #In form [nx,its,dt]

funcs.animator(absdata, nx, its)

