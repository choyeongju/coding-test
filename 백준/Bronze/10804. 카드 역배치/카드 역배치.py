import sys
input = sys.stdin.readline

arr = list(range(1, 21))

for _ in range(10):
    A, B = map(int, input().split())
    arr[A-1:B] = reversed(arr[A-1:B])

print(*arr)
