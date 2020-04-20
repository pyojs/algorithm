# SW Expert Academy 1859. 백만 장자 프로젝트

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cost = list(map(int, input().split()))
    # 이익을 저장할 변수
    result = 0
    while 1:
        # 현 시점에서 미래의 최고 매매가와 그 인덱스 저장
        temp_max = max(cost)
        temp_idx = cost.index(temp_max)
        # 최고 매매가 이전까지 원료를 사서 파는 이익 저장
        for i in range(temp_idx):
            result += (temp_max - cost[i])
        # 최고 매매가의 인덱스가 마지막인 경우 종료
        if temp_idx == len(cost)-1 :
            break
        # 배열을 최고 매매가 이후 날부터만 저장하고 다시 실행
        else:
            cost = cost[(temp_idx + 1):]
    print('#{} {}'.format(tc, result))