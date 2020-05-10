# python3
import sys


def compute_min_refills(distance, tank, stops):
    count = 0
    fuel = tank
    if fuel == distance:
        return 0

    if ((len(stops) + 1) * tank) < distance:
        return -1
    pits =[]
    for i in range(len(stops)):
        if i == 0:
            pits.append(stops[i])
        else:
            pits.append(stops[i] - stops[i-1])
    pits.append(distance - stops[-1])
    if max(pits) > tank:
        return -1
    for i in range(len(stops)):
        fuel = fuel - pits[i]
        if fuel < pits[i + 1]:
            count = count + 1
            fuel = tank




    return count

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
