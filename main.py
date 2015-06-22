"""
Program by Perry Hansler for solving the 1D Schrödinger equation.
Comes with creator, updater and animator module
Creator is a small function which allows for easier initialization of psi and V
It is currently set to a Gaussian for psi and a thin barrier for V

Updater uses the Crank Nicholson scheme to update the schrödinger equation using finite differences
It also saves the magnitude and phase of the data per timestep in the matrices absdata and angdata.

Animator uses the absdata and angdata to make a 'moving graph' movie.
"""

import creator
import updater
import animator

nx = 100   #Space points
its = 1000   #Time points
dt = 0.001  #Time spacing

psi, V = creator.creator(nx)

absdata, angdata = updater.updater(nx, its, dt, psi, V)  #In form [nx,its,dt]

animator.animator(absdata, nx, its)

