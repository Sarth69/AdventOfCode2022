from itertools import pairwise
import re

sensors = {}

lines = open('jour15Input.txt').read().splitlines()
MAX_DIM = 4_000_000

def dist(a, b):
    x,y = a
    xx,yy = b
    return abs(xx-x) + abs(yy-y)

for line in lines:
    sx,sy, bx,by = map(int,re.findall(r'-?\d+', line))
    sensors[(sx,sy)] = dist((sx,sy), (bx,by))

for y in range(0, MAX_DIM+1):
    ranges = []
    for (sx, sy), d in sensors.items():
        dy = abs(sy - y)
        if d > dy:
            dx = d - dy
            ranges.append((max(0,sx-dx), min(MAX_DIM+1, sx+dx+1)))

    # Dummy range at end.
    ranges = sorted(ranges) + [(MAX_DIM, MAX_DIM+10)]

    # Edge case. Pun intended.
    if ranges[0][0] == 1:
        print('part2', HI * 4000000 + y)
        exit()

    HI = 0
    for (_,hi), (lo, _) in pairwise(ranges):
        HI = max(HI, hi)
        if HI < lo:
            print('part2', HI * 4000000 + y)
            quit()