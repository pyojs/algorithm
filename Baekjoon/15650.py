# BAEKJOON 15650. N과 M (2)

N, M = map(int, input().split())

# 조합을 만들기 위한 함수
def cob(a):
    # 쓰는 경우 1, 안쓰는 경우 0
    c = [1, 0]
    # 반복 완료 시 결과 저장 / 순서대로 저장하는 것도 필요
    if a == N:
        if sum(check) == M:
            r = [0] * M
            k = 0
            for i in range(len(check)):
                if check[i]:
                    r[k] = arr[i]
                    k += 1
            result.append(r)
    else:
        for i in range(2):
            check[a] = c[i]
            cob(a+1)

# 1~N이 있는 배열 생성
arr = [i for i in range(1, N+1)]
# check로 사용 여부 결정 예정
check = [0] * N
result = []
cob(0)

# 출력
for k in range(len(result)):
    print(*result[k])