# Uses python3
import sys

def fibonacci_sum_naive(n):
    f=[]
    sum  = 0
    if n <= 1:
        return n
    for i in range(n % 60):
        if i == 0 or i == 1:
            f.append(1)
            sum = (sum + f[i]) % 10
        else:
            f.append( (f[i-1] + f[i-2]) % 10)
            sum = (sum + (f[i] % 10) ^ 2 ) % 10



    return sum % 10




if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_naive(n))
