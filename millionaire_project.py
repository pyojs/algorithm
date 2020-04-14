T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    result = 0

    while 1:
        temp_max = max(cost)
        temp_idx = cost.index(temp_max)
        for i in range(temp_idx):
            result += (temp_max - cost[i])
        if temp_idx == len(cost)-1 :
            break
        else:
            cost = cost[(temp_idx + 1):]
    print('#{} {}'.format(t, result))