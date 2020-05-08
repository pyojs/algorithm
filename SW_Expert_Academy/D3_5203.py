# SW Expert Academy 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

# run과 triplet을 확인하는 함수
def check(player, win):
    global result, end, cnt
    # triplet인 경우(같은 숫자가 3개)
    if 3 in player:
        # 승자로 저장하고 종료
        result = win
        end = True
        return
    else:
        # 플레이어가 받은 카드 중 연속된 카드 개수 검사
        for k in range(10):
            # 숫자가 있으면 cnt 증가
            if player[k]:
                cnt += 1
                # 연속된 숫자가 3개인 경우
                if cnt == 3:
                    # 승자로 저장하고 종료
                    result = win
                    end = True
                    return
            # 숫자가 없으면 cnt를 초기화
            else:
                cnt = 0

T = int(input())
for tc in range(1, T+1):
    card = list(map(int, input().split()))
    # 결과를 저장할 변수(기본은 무승부)
    result = 0
    # 플레이어가 받은 카드를 저장할 배열
    A_list = [0]*10
    B_list = [0]*10
    # 반복문을 종료할 변수
    end = False
    for i in range(len(card)):
        # 연속된 카드 개수를 저장할 변수
        cnt = 0
        # 짝수 번째 카드인 경우 B에게
        if i % 2:
            B_list[card[i]] += 1
            check(B_list, 2)
        # 홀수 번째 카드인 경우 B에게
        else:
            A_list[card[i]] += 1
            check(A_list, 1)
        if end:
            break

    print('#{} {}'.format(tc, result))