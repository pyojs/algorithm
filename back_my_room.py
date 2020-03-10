T = int(input())
for tc in range(1, T+1):
    N = int(input())
    b_stu = [list(map(int,input().split())) for _ in range(N)]
    # 복도를 배열로 만듬
    hallway = [0] * 200
    for x in b_stu:
        # 방번호가 작은 순서로 정렬
        if x[0] > x[1]:
            x[0], x[1] = x[1], x[0]
        # 방 번호를 복도 번호로 변화하며 지나가는 곳의 수를 증가
        for i in range((x[0]-1)//2, (x[1]+1)//2):
            hallway[i] += 1
    print('#{} {}'.format(tc, max(hallway)))