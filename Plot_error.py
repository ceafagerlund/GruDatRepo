import math
import numpy as np
import matplotlib.pyplot as plt

v = []
for i in range(1,8):
    v.append(1)
print(v)

e=1.6022e-19       # electron charge=-e
pi = math.pi
inf = math.inf
a=1.0e-9           # well width a=1 nm
hbar=1.0546e-34    # Plancks constant
m=9.1094e-31       # electron mass
E_NUM = []
###Following additions are energies such that abs(psi(a))<1e-16.
E_NUM.append(0.38462538)  #append E1 in eV for N = 10
E_NUM.append(0.3761292)     #append E1 in eV for N = 100
E_NUM.append(0.3760449) # N = 1000
E_NUM.append(0.3760441)      # N = 10 000
E_NUM.append(0.37604415)          #N = 100 000
E_NUM.append(0.37604415)          # N = 1000 000
E_NUM.append(0.37604415)    # N = 10 000 000
ENERGY = (hbar*pi/a)**2
ENERGY = ENERGY/(2*m)
ENERGY = ENERGY / e     #ENERGY in eV
error = []

#error.append(inf)
for i in range(0,7):
    error.append(abs(ENERGY - E_NUM[i]))

N = []
for i in range(0,7):
    N.append(i+1)


plt.close()
plt.figure(num=None, figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
plt.loglog(N, error, 'ro')
#limit=1.e-9
#plt.ylim(0, limit)
#plt.ylim(-limit, limit)
#plt.autoscale(False)
plt.xlabel('N')
plt.ylabel('error(N)')
#plt.savefig('psi.pdf')
plt.show()
