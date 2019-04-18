# -*- coding: utf-8 -*-
# Python simulation of an electron in a 1d infinite box potential
# Integrate time independent SE using the Verlet method
# Boundary conditions are found by shooting
# MW 190402


from pylab import *
import numpy as np
import matplotlib.pyplot as plt


def eigenstates(Energy,colorcounter):

    a=1.0e-9           # well width a=1 nm
    hbar=1.0546e-34    # Plancks constant
    m=9.1094e-31       # electron mass
    e=1.6022e-19       # electron charge=-e
    c=2.0*m/hbar**2    # constant in Schrödinger equation
    N=10000             # number of mesh points
    dx=a/N             # step length
    dx2=dx**2          # step length squared

    EeV = Energy          # input energy in eV: test 0.3 , 0.4 , 0.3760 , 1.5
    E = EeV*e          # input energy in J
    #E = 6.024978632810431e-20   #MY exact value for E1, in J
    #EeV = E/e
    #print('Exact solution:')
    #print('E1=',(hbar*np.pi/a)**2/(2.0*m)/e,'eV')
    #print('E2=',(hbar*2.0*np.pi/a)**2/(2.0*m)/e,'eV')

    # potential energy function
    def V(x):
        y = 0.0
        #y=e*5.*x/a # triangular potential
        #if x>0. and x<1. : y=e*5.*(x/a-1.) # finite triangular potential
        return y

    # initial values and lists
    x = 0.0             # initial value of position x
    psi = 0.0           # wave function at initial position
    dpsi = 1.0          # derivative of wave function at initial position
    x_tab = []          # list to store positions for plot
    psi_tab = []        # list to store wave function for plot
    x_tab.append(x/a)
    psi_tab.append(psi)

    for i in range(N) :
        d2psi = c*(V(x)-E)*psi
        d2psinew = c*(V(x+dx)-E)*psi
        psi += dpsi*dx + 0.5*d2psi*dx2
        dpsi += 0.5*(d2psi+d2psinew)*dx
        x += dx
        x_tab.append(x/a)
        psi_tab.append(psi)

    print('E=',EeV,'eV , psi(x=a)=',psi)


    if colorcounter == 1:
        plt.plot(x_tab, psi_tab, linewidth=1, color='red')
    elif colorcounter == 2:
        plt.plot(x_tab, psi_tab, linewidth=1, color='green')
    elif colorcounter == 3:
        plt.plot(x_tab, psi_tab, linewidth=1, color='blue')
    elif colorcounter == 4:
        plt.plot(x_tab, psi_tab, linewidth=1, color='purple')
    elif colorcounter == 5:
        plt.plot(x_tab, psi_tab, linewidth=1, color='orange')
    plt.xlim(0, 1)
    plt.xlabel('x/a')
    plt.ylabel('$\psi$')
    #plt.savefig('psi.pdf')

eigenstates(0.37604415,1)
eigenstates(1.5041768,2)
eigenstates(3.384398,3)
eigenstates(6.016708,4)
eigenstates(9.401108,5)
plt.show()
