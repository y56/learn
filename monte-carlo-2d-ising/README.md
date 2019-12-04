## 0.38 min on u5 
```python
nt      = 1         #  number of temperature points
N       = 36         #  size of the lattice, N x N
eqSteps = 1000       #  number of MC sweeps for equilibration
mcSteps = 3000       #  number of MC sweeps for calculation
T       = np.linspace(1.8, 3.0, nt);  # one pt as 1.8
```
## 4.05 min on u5 
```python
nt      = 1         #  number of temperature points
N       = 36         #  size of the lattice, N x N
eqSteps = 10000       #  number of MC sweeps for equilibration
mcSteps = 30000       #  number of MC sweeps for calculation
T       = np.linspace(1.8, 3.0, nt);  # one pt as 1.8
```

## np.linspace(0.015, 4.5, nt=45)

```
np.linspace(0.015, 4.5, nt)

array([0.015     , 0.11693182, 0.21886364, 0.32079545, 0.42272727,
       0.52465909, 0.62659091, 0.72852273, 0.83045455, 0.93238636,
       1.03431818, 1.13625   , 1.23818182, 1.34011364, 1.44204545,
       1.54397727, 1.64590909, 1.74784091, 1.84977273, 1.95170455,
       2.05363636, 2.15556818, 2.2575    , 2.35943182, 2.46136364,
       2.56329545, 2.66522727, 2.76715909, 2.86909091, 2.97102273,
       3.07295455, 3.17488636, 3.27681818, 3.37875   , 3.48068182,
       3.58261364, 3.68454545, 3.78647727, 3.88840909, 3.99034091,
       4.09227273, 4.19420455, 4.29613636, 4.39806818, 4.5       ])
```