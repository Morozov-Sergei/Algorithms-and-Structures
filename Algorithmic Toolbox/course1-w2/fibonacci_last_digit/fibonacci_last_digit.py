# Uses python3
import sys
fib = {0:0, 1:1}

def get_fibonacci_last_digit(n):
    global fib;
    if n in fib: return fib[n]
    last = 1;
    prelast = 0;
    fib = 0;
    for i in range(2,n+1):
        fib = (last + prelast)%10
        prelast = last;
        last = fib;
    return fib

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit(n))
