# Uses python3
import sys

def get_change(m):
    #write your code here
    total = m//10 +m%10//5 + m%10%5
    return total

if __name__ == '__main__':
    n = int(input())
    print(get_change(n))
