# candidates

## test 1
```
def solution(X, Y, D):
    tmp=(Y-X)//D
    return tmp if tmp*D==(Y-X) else tmp+1
```
## test 2
```
def solution(X, Y, D):
    return (Y-X)//D if (Y-X)//D*D==(Y-X) else (Y-X)//D+1
```
## test 3
```
from math import ceil
def solution(X, Y, D):
    return ceil((Y-X)/D)
```
## test 4
```
import math
def solution(X, Y, D):
    return math.ceil((Y-X)/D)
```
# compar
time python3 test1.py && time python3 test2.py && time python3 test3.py && time python3 test4.py

# result
```
real	0m0.283s
user	0m0.275s
sys	0m0.008s

real	0m0.284s
user	0m0.276s
sys	0m0.008s

real	0m0.268s
user	0m0.252s
sys	0m0.016s

real	0m0.279s
user	0m0.267s
sys	0m0.012s
```
