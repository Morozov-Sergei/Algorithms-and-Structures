# Uses python3
import sys
import math
def gcd(a, b):
    if b == 0: return a
    return gcd(b,a%b)

def lcm(a, b):
    #write your code here
    return int(a)*int(b)//gcd(a,b)

if __name__ == '__main__':
    #input = sys.stdin.read()
    a, b = map(int, input().split())
    print(lcm(a, b))
    #print (1023473145*226553150)
    #print(math.ceil(lcm(1023473145, 226553150)))

