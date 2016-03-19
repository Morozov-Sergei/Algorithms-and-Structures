# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    sorted_seg = sorted(segments, key = lambda x: x.end)
    # print(segments)
    # print(sorted_seg)

    points.append(sorted_seg[0].end)
    for s in sorted_seg:
        if not points[-1] in range(s.start, s.end+1):
            points.append(s.end)
    return points

if __name__ == '__main__':
    # inputFile = open("/Users/lert/PycharmProjects/course1-w3/covering_segments/input","r")
    n, *data = map(int, sys.stdin.read().split())
    #n, *data = map(int, inputFile.read().split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
