# 고른 식재료들의 시너지들의 합을 구하는 함수
def taste(A):
    total = 0
    for i in A:
        for j in A:
            if i != j:
                total += arr[i][j]
    return total

# 식재료를 반으로 나누는 조합을 구하는 함수
def select(a):
    global min_dif
    c = [1, 0]
    # 고른 식재료가 N//2개 인 경우 실행
    if sum(check) == N//2:
        A = []
        B = []
        # 각 식재료를 A와 B에 나누는 과정
        for k in range(len(check)):
            if check[k]:
                A.append(k)
            else:
                B.append(k)
        A_result = taste(A)
        B_result = taste(B)
        # 결과값 비교
        if abs(A_result - B_result) < min_dif:
            min_dif = abs(A_result - B_result)
    # 종료 조건
    elif a == N:
        return
    else:
        # 조합을 만들기 위한 반복, 재귀
        for i in range(2):
            check[a] = c[i]
            # A의 조합만 구하면 B는 자동으로 결정
            # -> 1번째 재료를 A에서 사용한다고 가정하고 문제를 품
            if check[0]:
                select(a+1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    min_dif = 987654321
    select(0)
    print('#{} {}'.format(t, min_dif))