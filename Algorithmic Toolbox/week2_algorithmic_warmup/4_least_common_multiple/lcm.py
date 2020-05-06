# Uses python3
import sys

def lcm_naive(a, b):
    return (int (a*b/ gcd_naive(a, b)))

def gcd_naive(a, b):
    # current_gcd = 1
    # for d in range(2, min(a, b) + 1):
    #     if a % d == 0 and b % d == 0:
    #         if d > current_gcd:
    #             current_gcd = d
    if b == 0:
        return a

    return gcd_naive(b, (a % b))
if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))