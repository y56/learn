N=39
ct=0
head=[]
tail=[]
while N>1:
    head.append(ct%26)
    tail.append((ct+2*N-2)%26)
    ct+=4*N-4
    N-=2
if N==1:
    head.append((ct+1)%26)
    for x in head+tail[::-1]:
        print(chr(ord('A')+x), end='')


