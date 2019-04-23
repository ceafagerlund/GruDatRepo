#Praktik övn. 4 uppg. 1, Alexander Fagerlund

import matplotlib.pyplot as plt
import time
from time import clock


def PowTimer(N):
    """Timer function for pow."""
    PowTimes = []
    for i in range(0,len(N)):
        start = time.clock()
        pow(N[i])
        PowTimes.append(time.clock() - start)
    print("pow:",PowTimes)
    return PowTimes

def SumTimer(a,N):
    """Timer function for sum1."""
    Sum1Times = []
    Sum2Times = []
    for i in range(0,len(N)):
        n = N[i]
        start = time.clock()
        sum1(a[:n])
        Sum1Times.append(time.clock() - start)
        start = time.clock()
        sum2(a[:n])
        Sum2Times.append(time.clock() - start)
    print("sum1:",Sum1Times,"sum2:",Sum2Times)
    if ReturnSelector == 1:
        return Sum1Times
    else:
        return Sum2Times

def pow(n):
    """Return 2**n, where n is a nonnegative integer."""
    if n == 0:
        return 1
    x = pow(n//2)
    if n%2 == 0:
        return x*x
    return 2*x*x

def sum1(a):
	"""Return the sum of the elements in the list a."""
	n = len(a)
	if n == 0:
		return 0
	if n == 1:
		return a[0]
	return sum1(a[:n//2]) + sum1(a[n//2:])

def sum2(a):
	"""Return the sum of the elements in the list a."""
	return _sum(a, 0, len(a)-1)

def _sum(a, i, j):
	"""Return the sum of the elements from a[i] to a[j]."""
	if i > j:
		return 0
	if i == j:
		return a[i]
	mid = (i+j)//2
	return _sum(a, i, mid) + _sum(a, mid+1, j)

N = [10,100,1000,10000,100000,1000000]  # test lengths and values
a = []
for i in range(0,1000000):              #test array
    a.append(1)
PowTimes = PowTimer(N)
ReturnSelector = 1                     #want to return time for sum1
SumTimes = SumTimer(a,N)

#plt.plot(N,PowTimes)                    #plot times for pow 
plt.scatter(N,PowTimes)
#plt.xscale('log')
plt.xlabel("Tal n")
plt.ylabel("Tid för pow(n)")
plt.show()

plt.plot(N,SumTimes,'r')                #plot times for sum1
#plt.scatter(N,SumTimes)
plt.xlabel("Arraylängder n")
plt.ylabel("Tid för sum1(n)")
plt.show()

ReturnSelector = 2                      #want times for sum2
SumTimes = SumTimer(a,N)            
#plt.plot(N,SumTimes,'r')                #plot times for sum2
plt.scatter(N,SumTimes)
plt.xlabel("Arraylängder n")
plt.ylabel("Tid för sum2(n)")
plt.show()
