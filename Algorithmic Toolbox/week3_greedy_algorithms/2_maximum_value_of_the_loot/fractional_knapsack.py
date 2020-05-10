# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    priority =[]
    for i in range(len(values)):
        priority.append(values[i]/weights[i])
    while capacity != 0:
        maxp = max(priority)
        if maxp == 0:
            return round(value, 4)
        p = priority.index(maxp)
        w = weights[p]
        if w < capacity:
            value = value + values[p]
            priority[p] = 0
            capacity = capacity - w
        else:
            value = value + (values[p] * capacity) / w
            capacity = 0
    return round(value, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
