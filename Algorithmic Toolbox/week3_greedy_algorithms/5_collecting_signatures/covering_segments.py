# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    superseg =[]
    print(segments)
    for s in segments:
        points.append(s.start)
        points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.readline()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
