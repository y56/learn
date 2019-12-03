from __future__ import print_function
from __future__ import division

import sys

from pyspark import SparkContext

import numpy as np
import datetime

from numpy.random import rand

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
nt      = 16         #  number of temperature points
N       = 16         #  size of the lattice, N x N
eqSteps = 16       #  number of MC sweeps for equilibration
mcSteps = 16       #  number of MC sweeps for calculation

FileEnergy = "mini_Data_Energy_L10_80pt.txt"
FileMagnet = "mini_Data_Magnet_L10_80pt.txt"
FileC = "mini_Data_SpHeat_L10_80pt.txt"
FileX = "mini_Data_Suscep_L10_80pt.txt"
FileFigure = "mini_Fig_total_L10_80pt.png"


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

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: spark-submit sort <inputfile> <outputfile>", file=sys.stderr)
        exit(-1)
        
    sc = SparkContext(appName="PythonSortyy")
    
    time4 = list(T) + ['WWWWWWWW'] + list(T) + ['WWWWWWWW'] + list(T) + ['WWWWWWWW'] + list(T)
    EMCX = list(E) + ['WWWWWWWW'] + list(M) + ['WWWWWWWW'] + list(C) + ['WWWWWWWW'] + list(X)

    a = sc.textFile(sys.argv[1], 1)
    nums = a.flatMap(lambda x: range(0, 4*N+3))
    word = nums.map(lambda x: [time4[int(x)], EMCX[int(x)]])
    out  = word
    out.saveAsTextFile('/user/student2/mini')

    i = 0
    while i < 100:
        i += 1
        print("WWWWWWWWWWWWWWWWWWWWWWW")

    sc.stop()
                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                          1,5           Top
