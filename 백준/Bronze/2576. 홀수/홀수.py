result = 0;
minValue = 100;

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        result += n
        minValue = min(minValue, n)

if result == 0:
    print(-1)
else:
    print(result)
    print(minValue)