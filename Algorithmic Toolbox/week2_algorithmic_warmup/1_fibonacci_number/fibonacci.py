# Uses python3
def calc_fib(n):
    f=[]
    if n == 0:
        return 0
    for i in range(n):
        if i == 0 or i == 1:
            f.append(1)
        else:
            f.append( f[i-1] + f[i-2])
    return f[n-1]

n = int(input())
print(calc_fib(n))
