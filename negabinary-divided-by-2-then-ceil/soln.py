"""
base-(-2) representation
Negabinary
"""
import math
def bit(res): # convert num to bit
    ans = []
    while res != 0:
        ans.append(abs(res % (-2)))
        res = math.ceil(res/(-2))
    return ans
def basicsolution(A): # sloww but confident to be correct
    res = 0
    tmp = 1
    for x in A:
        res += x * tmp
        tmp *= -2
    res = int(math.ceil(res / (2.0)))
    ans = []
    while res != 0:
        ans.append(abs(res % (-2)))
        res = math.ceil(res/(-2))
    return ans

A=[0]*10+[1]
print(A)
print(basicsolution(A))

def goodsolution(A):
    for i,x in enumerate(A):
        if i==0:
            continue
        if x==1:
            A[i-1]+=1
    for x in A:
        assert 0<=x<=2
    limit=len(A)
    for i in range(limit):
        if A[i]>2 or A[i]<0:
            print("A[i] BAD!!!")
        if A[i]==2:
            if i==limit-2:
                if A[i+1]==0:
                    A[i]-=2
                    A[i+1]+=1
                    A.append(1)
                elif A[i+1]==1 or A[i+1]==2:
                    A[i]-=2
                    A[i+1]-=1
                else:
                    print("weird, when dealing w/ second last")
            elif i==limit-1:
                A.append(1)
                A.append(1)
                if len(A)!=limit+2:
                    print("weird, when dealing w/ last")
            else:
                if A[i+1]==0:
                    A[i]-=2
                    A[i+1]+=1
                    A[i+2]+=1
                elif A[i+1]==1 or A[i+1]==2:
                    A[i]-=2
                    A[i+1]-=1
                else:
                    print("for some i<=limit-3, A[i+1] BAD!!!")
    while A and A[-1]==0:
        A.pop()
    return A

AA=9999
for i in range(-AA,AA):
#    print(i, bit(i))
    assert basicsolution(bit(i))==goodsolution(bit(i))

print(goodsolution([1]*100000))
print(goodsolution([1]*100001))
print(goodsolution([1]+[0]*100000))
print(goodsolution([0]*100000+[1]))

