# BAEKJOON 15654. N과 M (5)

# 수열을 만들고 출력하기 위한 함수
def sequence(k):
    # M개를 고른 경우 출력
    if k == M:
        print(*result)
    # 아직 M개를 고르지 못한 경우
    else:
        for i in range(N):
            # 지금 넣으려는 수를 사용하지 않은 경우
            if visited[i] == 0 :
                # 사용했다고 체크하고 결과에 추가 후 재귀 실행
                visited[i] = 1
                result.append(arr[i])
                sequence(k+1)
                # 사용이 끝나면 결과에서 제거하고 사용한다고 체크한 것을 원래대로 돌림
                result.pop()
                visited[i] = 0

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 입력된 수를 오름차순으로 정렬
arr.sort()
# 결과를 저장할 배열
result = []
# 수를 사용하였는지 확인할 배열
visited = [0 for _ in range(N)]
sequence(0)