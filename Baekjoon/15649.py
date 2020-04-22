# BAEKJOON 15649. N과 M (1)

N, M = map(int, input().split())

# 순열을 만들기 위한 함수
def per(a):
    # 반복을 완료 했을 때 결과를 저장
    if a == M:
        r = [0] * M
        for i in range(len(check)):
            if check[i]:
                r[check[i]-1] = arr[i]
        result.append(r)
    else:
        # check에 쓰일 순서를 저장하는 부분
        for i in range(N):
            if check[i] == 0:
                check[i] = a + 1
                per(a+1)
                check[i] = 0

# 1~N이 있는 배열을 만듬
arr = [i for i in range(1, N+1)]
# check에 순서를 저장할 예정
check = [0] * N
result = []
per(0)

# 출력
for k in range(len(result)):
    print(*result[k])