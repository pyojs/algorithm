# SW Expert Academy 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색

# 이진 탐색을 실행하는 함수
def binary_search(left, right, center, find):
    # 탐색 횟수를 저장할 변수
    cnt = 0
    # 반복문 실행
    while True:
        # 중간 페이지가 찾아야하는 페이지 보다 큰 경우
        if center > find:
            # 오른쪽을 중간 페이지로 변경
            right = center
            cnt += 1
            center = int((left + right)/2)
        # 중간 페이지가 찾아야하는 페이지 보다 작은 경우
        elif center < find:
            # 왼쪽을 중간 페이지로 변경
            left = center
            cnt += 1
            center = int((left + right)/2)
        # 중간페이지와 일치하는 경우 결과를 반환하고 종료
        else:
            return cnt

T  = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    left, right = 1, P
    # 중간 페이지 계산
    center = int((left + right)/2)
    A_cnt = binary_search(left, right, center, Pa)
    B_cnt = binary_search(left, right, center, Pb)
    # 탐색 게임에서 이긴 사람을 알아내는 조건문
    if A_cnt < B_cnt:
        result = 'A'
    elif A_cnt > B_cnt:
        result = 'B'
    else:
        result = '0'
    
    print('#{} {}'.format(tc, result))
