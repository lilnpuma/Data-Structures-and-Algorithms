# Uses python3
import sys

def get_change(m):
    count = 0
    count = m//10
    m = m % 10
    count = count + m // 5
    m = m % 5
    count = count + m
    return count

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
