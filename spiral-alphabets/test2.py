def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
        
    abc=1
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            a[k][i]=abc
            abc+=1
            
        k += 1
 
        for i in range(k, m):
            a[i][n - 1]=abc
            abc+=1
        n -= 1
 
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                a[m - 1][i]=abc
                abc+=1
            m -= 1
 
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                a[i][l]=abc
                abc+=1
            l += 1
 
a=[[0]*40 for i in range(40)]
R = 39
C = 39
 
spiralPrint(R, C, a)
 
for i in range(40):
#    while a[i][i] > 90:
#        a[i][i]-=26
    print(chr(ord("A")-1+a[i][i]%26),end='')

