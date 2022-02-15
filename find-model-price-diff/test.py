import numpy as np

N = 10000
x = np.linspace(0,N-1,N)

for xx in x:
	print(xx, np.exp(-0.05*xx))

for xx in x:
	print(xx, np.exp(-0.06*xx))

for xx in x:
	print(xx, np.exp(-0.07*xx))

for xx in x:
	print(xx, np.exp(-0.08*xx))

print(np.__version__)

