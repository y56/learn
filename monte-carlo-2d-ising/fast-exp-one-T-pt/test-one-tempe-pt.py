from __future__ import division
import numpy as np
from numpy.random import rand

import inspect, os
print inspect.getfile(inspect.currentframe()) # script filename (usually with path)
print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script directory

import datetime
print(datetime.datetime.now())

#----------------------------------------------------------------------
##  BLOCK OF FUNCTIONS USED IN THE MAIN CODE
#----------------------------------------------------------------------
def initialstate(N):   
    ''' generates a random spin configuration for initial condition'''
    state = 2*np.random.randint(2, size=(N,N))-1
    return state


def mcmove(config, beta):
    '''Monte Carlo move using Metropolis algorithm '''
    for i in range(N):
        for j in range(N):
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s =  config[a, b]
                nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                cost = 2*s*nb
                Pindex = int(cost/4-1)
                if cost < 0:
                    s *= -1
                elif rand() < P_2D[Pindex]:
                    s *= -1
                config[a, b] = s
    return config


def calcEnergy(config):
    '''Energy of a given configuration'''
    energy = 0
    for i in range(len(config)):
        for j in range(len(config)):
            S = config[i,j]
            nb = config[(i+1)%N, j] + config[i,(j+1)%N] + config[(i-1)%N, j] + config[i,(j-1)%N]
            energy += -nb*S
    return energy/4.


def calcMag(config):
    '''Magnetization of a given configuration'''
    mag = np.sum(config)
    return mag
## change these parameters for a smaller (faster) simulation 
nt      = 1         #  number of temperature points
N       = 36         #  size of the lattice, N x N
eqSteps = 10000       #  number of MC sweeps for equilibration
mcSteps = 30000       #  number of MC sweeps for calculation

FileEnergy = "Data_Energy_L10_80pt.txt"
FileMagnet = "Data_Magnet_L10_80pt.txt"
FileC = "Data_SpHeat_L10_80pt.txt"
FileX = "Data_Suscep_L10_80pt.txt"
FileFigure = "Fig_total_L10_80pt.png"


T       = np.linspace(1.8, 3.0, nt); 
E,M,C,X = np.zeros(nt), np.zeros(nt), np.zeros(nt), np.zeros(nt)
iNSite = 1.0/(N*N)
# divide by number of samples, and by system size to get intensive values
#----------------------------------------------------------------------
#  MAIN PART OF THE CODE
#----------------------------------------------------------------------
for tt in range(nt):
    E1 = M1 = E2 = M2 = 0
    config = initialstate(N)
    iT=1.0/T[tt]; iT2=iT*iT;
    
    P_2D = np.zeros(2)
    P_2D[0] = np.exp(-4*iT)
    P_2D[1] = P_2D[0] * P_2D[0]
    
    
    for i in range(eqSteps):         # equilibrate
        mcmove(config, iT)           # Monte Carlo moves
    counter = 0
    for i in range(mcSteps):
        mcmove(config, iT)           
        Ene = calcEnergy(config)     # calculate the energy
        Mag = calcMag(config)        # calculate the magnetisation
        
        if i % 10 == 0:
            Ene = calcEnergy(config)     # calculate the energy
            Mag = calcMag(config)        # calculate the magnetization
            counter += 1
            E1 = E1 + Ene      # collect energy
            M1 = M1 + Mag      # collect magnetization
            E2 = E2 + Ene*Ene  # square of energy
            M2 = M2 + Mag*Mag  # square of magnetization
    icounter = 1.0/counter
    E[tt] = icounter*iNSite*E1
    M[tt] = icounter*iNSite*M1
    C[tt] = (icounter*E2 - icounter*icounter*E1*E1)*iT2*iNSite
    X[tt] = (icounter*M2 - icounter*icounter*M1*M1)*iT*iNSite

#### save the data
with open(FileEnergy, 'w') as f:
    for tt in range(nt):
        f.write("{}\t{}\n".format(T[tt], E[tt]))
with open(FileMagnet, 'w') as f:
    for tt in range(nt):
        f.write("{}\t{}\n".format(T[tt], M[tt]))
with open(FileC, 'w') as f:
    for tt in range(nt):
        f.write("{}\t{}\n".format(T[tt], C[tt]))
with open(FileX, 'w') as f:
    for tt in range(nt):
        f.write("{}\t{}\n".format(T[tt], X[tt]))



import matplotlib.pyplot as plt

f = plt.figure(figsize=(18, 10)); # plot the calculated values    

sp =  f.add_subplot(2, 2, 1 );
plt.scatter(T, E, s=50, marker='o', color='IndianRed')
plt.xlabel("Temperature (T)", fontsize=20);
plt.ylabel("Energy ", fontsize=20);         plt.axis('tight');

sp =  f.add_subplot(2, 2, 2 );
plt.scatter(T, abs(M), s=50, marker='o', color='RoyalBlue')
plt.xlabel("Temperature (T)", fontsize=20); 
plt.ylabel("Magnetization ", fontsize=20);   plt.axis('tight');

sp =  f.add_subplot(2, 2, 3 );
plt.scatter(T, C, s=50, marker='o', color='IndianRed')
plt.xlabel("Temperature (T)", fontsize=20);  
plt.ylabel("Specific Heat ", fontsize=20);   plt.axis('tight');   

sp =  f.add_subplot(2, 2, 4 );
plt.scatter(T, X, s=50, marker='o', color='RoyalBlue')
plt.xlabel("Temperature (T)", fontsize=20); 
plt.ylabel("Susceptibility", fontsize=20);   plt.axis('tight');
plt.savefig('FileFigure_origin.png')
print(datetime.datetime.now())
