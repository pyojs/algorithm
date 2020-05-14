# BAEKJOON 15657. N과 M (8)

# 수열을 만들고 출력하기 위한 함수
def sequence(k):
    # M개를 고른 경우 출력
    if k == M:
        print(*result)
    # 아직 M개를 고르지 못한 경우
    else:
        for i in range(N):
            # 비내림차순인 경우
            if k == 0 or result[-1] <= arr[i]:
                # 결과에 수를 저장하고 재귀 실행
                result.append(arr[i])
                sequence(k+1)
                # 사용이 끝나면 결과에서 제거
                result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 입력된 수를 오름차순으로 정렬
arr.sort()
# 결과를 저장할 배열
result = []
sequence(0)