for _ in range(3):
    a, b, c, d = map(int, input().split())
    arr = [a, b, c, d]
    # 또는 arr = list(map(int, input().split()))

    zero = 0
    for i in arr:
        if i == 0:
            zero += 1
    # 또는 zero = arr.count(0)

    if zero == 0:
        print('E')
    elif zero == 1:
        print('A')
    elif zero == 2:
        print('B')
    elif zero == 3:
        print('C')
    else:
        print('D')
