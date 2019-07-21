# https://hackmd.io/2KBqq0S0TqKvtqUHUhyyTg#revision-solution-from-others-0

# https://leetcode.com/problems/reverse-integer/discuss/4055/Golfing-in-Python

def reverse(x):
    print("Input is", x)
    if x > (2**31 -1):
        print("Input > max, should return 0")
    if x < (-2**31):
        print("Input < min, should return 0")
    if x >= 0:
            if int(str(x)[::-1]) > (2**31 - 1):
                print("Output > max, should return 0")
    else:
            if -int(str(x)[-1:0:-1]) < (-2**31):
                print("Output < min, should return 0")
    
    s = (x > 0) - (x < 0)  # positive-->1; negative-->-1; 0-->0
    r = int(str(x*s)[::-1]) # x*s = abs(x) 
    print("return")
    return s*r * (r < 2**31)  # put the sign back and ???


print("-2**31-2")
print(reverse(int(-2**31-2)))

