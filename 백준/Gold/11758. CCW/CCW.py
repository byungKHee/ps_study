import sys
input = sys.stdin.readline

def vector(p1, p2):
    return [p2[0] - p1[0], p2[1] - p1[1]]

def cross(v1, v2):
    return v1[0]*v2[1] - v1[1]*v2[0]

P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

v1 = vector(P1, P2)
v2 = vector(P2, P3)

answer = cross(v1, v2)
if answer < 0:
    print(-1)
elif answer > 0:
    print(1)
else:
    print(0)