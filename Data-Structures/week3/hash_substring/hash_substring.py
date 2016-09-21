# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    _multiplier = 263
    _prime = 1000000007
    P = len(pattern)
    T = len(text)

    def _hash_func(s):
        ans = 0
        for c in reversed(s):
            ans = (ans * _multiplier + ord(c)) % _prime
        return ans

    def preComputeHash(text, P):
        H = [ 0 for i in range(T-P+1)]
        S = text[T-P:]
        H[T-P] =_hash_func(S)
        y = 1
        for i in range(1, P + 1):
            y = (y * _multiplier)%_prime
        for i in range(T-P-1,-1, -1):
            H[i]=(_multiplier*H[i+1] + ord(text[i]) - y*ord(text[i+P]))%_prime
        return H

    result = []
    pHash = _hash_func(pattern)
    H = preComputeHash(text, P)
    for i in range(0, T - P + 1):
        if pHash != H[i]:
            continue
        if pattern ==text[i:i+P]:
            result.append(i)
    return result


DEBUG = False
if __name__ == '__main__':
    if DEBUG:
        print_occurrences(get_occurrences('aaaaa','baaaaaaa'))
    else:
        print_occurrences(get_occurrences(*read_input()))

