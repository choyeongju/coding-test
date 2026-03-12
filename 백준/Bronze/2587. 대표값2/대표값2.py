#arr = [int(input()) for _ in range(5)]
arr = []
for _ in range(5):
    arr.append(int(input()))

arr.sort()
print(int(sum(arr) / len(arr)))
print(arr[len(arr)//2])