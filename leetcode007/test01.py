# https://hackmd.io/2KBqq0S0TqKvtqUHUhyyTg#revision-solution-from-others-0

# https://leetcode.com/problems/reverse-integer/discuss/4055/Golfing-in-Python

def reverse(x):
    print(x)
    if x > (2**31 -1):
        print("Input > max")
    if x < (-2**31):
        print("Input < min")
    if x >= 0:
            if int(str(x)[::-1]) > (2**31 - 1):
                print("Output > max")
    else:
            if -int(str(x)[-1:0:-1]) < (-2**31):
                print("Output < min")
    
    s = (x > 0) - (x < 0)  # positive-->1; negative-->-1; 0-->0
    r = int(str(x*s)[::-1]) # x*s = abs(x) 
    return s*r * (r < 2**31)  # put the sign back and ???

import sys

#print(sys.argv)
#print(sys.argv[0])
#print(sys.argv[1])
print(reverse(int(eval(sys.argv[1]))))
