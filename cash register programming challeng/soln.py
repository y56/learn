import sys
def findChange(rem):
    ans=[]
    while rem > 0.01:
        if rem >= 100.0:
            ans.append("ONE HUNDRED")
            rem -= 100.0
        elif rem >= 50.0:
            ans.append("FIFTY")
            rem -= 50.0
        elif rem >= 20.0:
            ans.append("TWENTY")
            rem -= 20.0
        elif rem >= 10.0:
            ans.append("TEN")
            rem -= 10.0
        elif rem >= 5.0:
            ans.append("FIVE")
            rem -= 5.0
        elif rem >= 2.0:
            ans.append("TWO")
            rem -= 2.0
        elif rem >= 1.0:
            ans.append("ONE")
            rem -= 1.0
        elif rem >= 0.5:
            ans.append("HALF DOLLAR")
            rem -= 0.5
        elif rem >= 0.25:
            ans.append("QUARTER")
            rem -= 0.25
        elif rem >= 0.1:
            ans.append("DIME")
            rem -= 0.1
        elif rem >= 0.05:
            ans.append("NICKEL")
            rem -= 0.05
        else:
            ans.append("PENNY")
            rem -= 0.01
    ans.sort()
    return ','.join(ans)
    
def func(line):
    pp, ch = line.rstrip("\n").split(';')
    rem=float(ch)-float(pp)
    if rem == 0:
        return "ZERO"
    elif rem < 0:
        return "ERROR"
    else:
        return findChange(rem)
    
for line in sys.stdin:
    print(func(line), end="")
