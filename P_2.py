# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:52:16 2020

@author: Himanshu Tyagi
"""

import numpy as np
import matplotlib.pyplot as plt
n=1000
x=np.linspace(-5,5,n)
k=np.linspace(-1*np.pi/10,np.pi/10,100)

H=np.zeros((n,n),dtype='complex')
e=np.zeros((20,100))
G=2*np.pi*np.arange(-500,500,1)/10
f_v=np.zeros(n,dtype='complex')
for i in range(n):
 for j in range(n):
  f_v[i]=f_v[i]+(x[j]**4-3)*np.exp(-0.5*x[j]**2-1j*G[i]*x[j])/n

for a in range(len(k)):
 for b in range(n):
    for c in range(n):
        H[b][c]=f_v[b-c]/np.sqrt(10)
    H[b][b]=H[b][b]+(k[a]+G[b])**2/0.04

 E=np.linalg.eigvalsh(H)
 for i in range(20):
    e[i][a]=E[i] 

for i in range(1,8):
    plt.plot(k,e[i][:])
    plt.title("Dispersion relation")
    plt.xlabel("k")
    plt.ylabel("E")
plt.show()
for i in range(10):
    print("energy band gaps= ",e[i+1][0]-e[i][0])