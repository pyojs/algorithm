# BAEKJOON 14889. 스타트와 링크

# 팀을 구성하고 능력치 차이를 구하는 함수
def soccer(n, k):
    global gap
    # 팀 구성이 끝났을 때 실행
    if n == N//2 -1:
        # 팀별 능력치와 차이를 구함
        start = 0
        link = 0
        for j in range(N):
            for i in range(N):
                if visited[i] and visited[j]:
                    start += ablility[j][i]
                elif not(visited[i]) and not(visited[j]):
                    link += ablility[j][i]
        temp_gap = abs(start-link)
        # 현재 차이보다 작은 경우 저장
        if temp_gap < gap:
            gap = temp_gap
    # 능력치 차이가 0이 된 경우 종료
    elif gap == 0:
        return
    # 팀 구성을 하면서 실행
    else:
        for i in range(k, N):
            if visited[i] == 0:
                visited[i] = 1
                soccer(n+1, i)
                visited[i] = 0
N = int(input())
ablility = [list(map(int, input().split())) for _ in range(N)]
# 1번 사람의 팀을 결정함으로 중복 방지
# -> 코드에서 start팀에 고정함으로 조합의 수를 줄임
# -> 이 코드에선 [1, 1, 0, 0]과 [0, 0, 1, 1]은 같은 경우 취급
visited = [1]+[0]*(N-1)
gap = 987654321
soccer(0, 1)
print(gap)