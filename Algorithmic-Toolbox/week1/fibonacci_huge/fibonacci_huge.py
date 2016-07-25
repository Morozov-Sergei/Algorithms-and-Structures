# Uses python3
import sys

fib = {0:0, 1:1}

def get_fibonacci_mod(n,m):
    global fib;
    if n in fib: return fib[n]
    last = 1;
    prelast = 0;
    fib = 0;
    for i in range(2,n+1):
        fib = (last + prelast)%m
        prelast = last;
        last = fib;
    return fib

def get_fibonaccihuge(n,m):
    global fib;
    if n in fib: return fib[n]
    last = 1;
    prelast = 0;
    rfib = 0;
    for i in range(2,n+1):
        rfib = (last + prelast)%m
        prelast = last;
        last = rfib;
        if prelast == 0 and last == 1:
            rfib = get_fibonacci_mod(n%(i-1),m)
            break;
    return rfib


if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonaccihuge(n, m))
    #print(get_fibonaccihuge(281621358815590, 30524))