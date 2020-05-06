# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    f=[]
    sum  = 0
    dict = {
    0:0,
    1:1,
    2:4,
    3:9,
    4:6,
    5:5,
    6:6,
    7:9,
    8:4,
    9:1
    }
    if n <= 1:
        return n
    for i in range(n % 60):
        if i == 0 or i == 1:
            f.append(1)
            sum = (sum + f[i]) % 10
        else:
            f.append( (f[i-1] + f[i-2]) % 10)
            sum = (sum + dict[(f[i] % 10)])  % 10


    return sum % 10

if __name__ == '__main__':
    n = int(stdin.readline())
    print(fibonacci_sum_squares_naive(n))
