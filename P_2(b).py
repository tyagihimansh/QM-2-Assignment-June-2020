# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 13:45:05 2020

@author: Himanshu Tyagi
"""

import time
t0= time.time()
from numpy import pi, linspace, zeros, cos, array, exp, inf, sort, shape
from numpy.linalg import eigvalsh
import matplotlib.pyplot as plt
def eigenvalues(N, m=1):
  n=1000
  h =1
  e= zeros([50, 20])
  for k in range(0,50):
    x= linspace(-5-k/2, 5+k/2, n)
    dx= x[1]- x[0]
    L= linspace(10, 50, 50)
    H= zeros((n,n))
   
    for i in range(n):
        if i>0:
            
            H[i-1,i]= -0.5*(h**2)/(m*dx**2)
        H[i,i] = ((x[i]**4) - 3)*exp(-0.5*x[i]**2) + 1*(h**2)/(m*dx**2)
        if i+1<n:
            H[i+1, i] = -0.5*(h**2)/(m*dx**2)
     
    E = sort(eigvalsh(H))
    
    for i in range(20):
        e[k,i] = E[i]
  fig = plt.plot(L, e)
  plt.title('Eigenvalues vs Box Length')
  plt.xlabel('$L$')
  plt.ylabel('$E_i$')
  print(len(x))
  plt.show()
  plt.plot(L, e[:,::2])
  plt.title('Even Parity')
  plt.xlabel('$L$')
  plt.ylabel('$E_i$')
  print(len(x))
  plt.show()
  plt.plot(L, e[:,1::2])
  plt.title('Odd Parity')
  plt.xlabel('$L$')
  plt.ylabel('$E_i$')
  print(len(x))
  plt.show()
  print(e)
  return E
eigenvalues(20)
t1= time.time()
print('Time =',t1-t0)      