import sys
input = sys.stdin.readline

T = int(input())
arr = list(map(int, input().split()))

Y = 0
M = 0

for t in arr:
    Y += (t // 30 + 1) * 10
    M += (t // 60 + 1) * 15

if Y < M :
    print("Y", Y)
elif Y > M :
    print("M", M)
else:
    print("Y M", Y)