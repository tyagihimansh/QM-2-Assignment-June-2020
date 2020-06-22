# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:48:51 2020

@author: Himanshu Tyagi
"""
import time
t0= time.time()
from numpy import pi, linspace, zeros, cos, array
from numpy.linalg import eigvalsh
import matplotlib.pyplot as plt
def Eigenvalues(N, M= 1, a=1, g= 1, I= 300):
    n=3000
    h =1
    x= linspace(0, 2*pi, n)
    dx= x[1]- x[0]
    H= zeros((n,n))
    for i in range(n):
        H[i-1,i]= -0.5*(h**2)/(I * dx**2)
        H[i,i] = M*g*a*(1 - cos(x[i])) + 1*(h**2)/(I * dx**2)
        if i+1<n:
            H[i+1, i] = -0.5*(h**2)/(I * dx**2)
        else:
            H[0, i] = -0.5*(h**2)/(I * dx**2)
    E = eigvalsh(H)
    fig = plt.plot(E[:N])
    plt.grid()
    plt.title('First 300 Eigenvalues')
    plt.xlabel('$i$')
    plt.ylabel('$E_i$')
    z=[]
    for i in range(200):
        if E[i+1]-E[i]<1E-7:
            z.append(i)
    return (E), fig, print('1st Eigenvalue = {}, \n50th Eigenvalue = {}, \n200th Eigenvalues = {}'.format(E[0], E[49], E[199])), print('degeneracy Starts at state', z[0])
w= Eigenvalues(300)
t1= time.time()
print('Time =',t1-t0)      