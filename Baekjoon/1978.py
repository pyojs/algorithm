# BAEKJOON 1978. 소수 찾기

N = int(input())
arr = list(map(int, input().split()))
# 결과를 저장할 변수
result = 0
# 입력된 수를 검사
for n in range(N):
    # 2부터 해당하는 숫자 전까지 검사
    for i in range(2, arr[n]):
        # 자신과 1을 제외한 약수가 있는 경우 종료
        if arr[n] % i == 0:
            break
    # 반복문을 마쳤을 경우
    else:
        # 숫자가 1이 아니면 결과 +1
        if arr[n] != 1:
            result += 1
print(result)