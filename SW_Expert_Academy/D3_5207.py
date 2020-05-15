# SW Expert Academy 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색

# 이진 탐색을 실행할 함수
def binary_search(l, r, d):
    # 중심 원소의 인덱스 m
    m = (l+r)//2
    # 찾는 정수가 A[m]인 경우 True
    if A[m] == target:
        return True
    # 찾는 정수가 중심보다 오른쪽에 있는 경우
    if A[m] < target:
        # l의 값을 수정
        l = m + 1
        # 이전에 탐색했던 방향과 같으면 False 반환
        if d == 2:
            return False
        # 탐색 방향을 d에 저장
        d = 2
    # 찾는 정수가 중심보다 왼쪽에 있는 경우
    else:
        # r의 값을 수정
        r = m - 1
        # 이전에 탐색했던 방향과 같으면 False 반환
        if d == 1:
            return False
        # 탐색 방향을 d에 저장
        d = 1
    # 반환 값으로 재귀 실행
    return binary_search(l, r, d)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # A를 오름차순 정렬
    A.sort()
    B = list(map(int, input().split()))
    # 결과를 저장할 변수
    result = 0
    # B를 순회하기 위한 반복문
    for i in range(M):
        # 찾을 값을 target에 저장
        target = B[i]
        # 이진 탐색 실행
        if binary_search(0, N-1, 0):
            # 찾은 경우 결과 +1
            result += 1

    print('#{} {}'.format(tc, result))