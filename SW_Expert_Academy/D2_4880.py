# SW Expert Academy 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임

# 1등을 찾기 위한 함수
def check(start, end):
    # 시작점과 끝점이 같아진 경우 계산 시작
    if start == end:
        return start
    else:
        # 토너먼트에서 게임을 진행할 학생 선출
        v1 = check(start, (start+end)//2)
        v2 = check((start+end)//2+1, end)

        if card[v1] == 1 and card[v2] == 2: #가위, 바위
            return v2
        elif card[v1] == 1 and card[v2] == 3: #가위, 보
            return v1
        elif card[v1] == 2 and card[v2] == 1: #바위, 가위
            return v1
        elif card[v1] == 2 and card[v2] == 3: #바위, 보
            return v2
        elif card[v1] == 3 and card[v2] == 1: #보, 가위
            return v2
        elif card[v1] == 3 and card[v2] == 2: #보, 바위 
            return v1
        elif card[v1] == card[v2]: #같을 때 v1 반환 
            return v1

T = int(input())
for t in range(1 ,T+1):
    N = int(input())
    card = list(map(int, input().split()))

    print('#{} {}'.format(t, check(0, len(card)-1)+1))
