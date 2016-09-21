# Uses python3
import sys


def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal(n):
    seq = []
    dp =[ -1 for x in range(0, n+1)]
    dp[1] = 0;
    for i in range(2, n+1):
        dp[i] = 1 + dp[i-1];
        if i%2==0:
            dp[i] = min( dp[i] , 1+ dp[i//2] );
        if i%3==0:
            dp[i] = min( dp[i] , 1+ dp[i//3] );

    while n >=1:
        seq.append(n)
        val = dp[n-1] +1
        opt = min( val , 1+ dp[n//2] if not n%2 else val, 1+ dp[n//3] if not n%3 else val)
        if opt == 1+ dp[n//3] :
                n = n // 3
        elif opt == 1+ dp[n//2]:
                n = n // 2
        else:
                n = n - 1
    return reversed(seq)


input = sys.stdin.read()
n = int(input)
#n = 96234
sequence = list(optimal(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
