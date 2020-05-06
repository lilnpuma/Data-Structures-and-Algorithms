# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    f=[]
    m = m % 60
    n = n % 60
    if n < m:
        n = n + m + 1

    sum  = 0
    if n == 1:
        return 1
    for i in range(n):
        if i == 0 or i == 1:
            f.append(1)
        else:
            f.append( (f[i-1] + f[i-2]) %  10)
        # if m == 0:
            # if i in range (0, n):
            #     sum = sum + f[i]
        if i in range((m - 1) , (n + 1)):
            
            sum = sum + f[i]
    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
