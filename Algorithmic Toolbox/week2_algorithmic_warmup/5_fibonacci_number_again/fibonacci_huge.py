# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    f=[]
    Pisano_pd = 0
    if n == 0:
        return 0
    for i in range(n):
        if i == 0 or i == 1:
            f.append(1)
        else:
            f.append( (f[i-1] + f[i-2]) % m)
            if f[i-1] == 0 and f[i] == 1:
                Pisano_pd = i
                n = n % Pisano_pd
                return get_fibonacci_huge_naive(n, m)

    return f[n-1] % m

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
