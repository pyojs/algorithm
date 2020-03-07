T = 10
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    p = False
    
    while 1:
        # 제일 앞의 숫자에서 1~5 사이의 수를 뺌
        for k in range(1, 6):
            temp = arr.pop(0) - k
            # 뺀 숫자가 0보다 큰 경우는 맨 뒤에 숫자를 추가
            if temp > 0:
                arr.append(temp)
            # 뺀 숫자가 0인경우 맨 뒤에 0을 추가하고 종료
            else:
                arr.append(0)
                p = True
                break
        if p:
            break
    print('#{} '.format(t), end = '')
    print(*arr)