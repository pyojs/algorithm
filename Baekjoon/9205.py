# BAEKJOON 9205. 맥주 마시면서 걸어가기

from collections import deque

t = int(input())
for tc in range(t):
    n = int(input())
    house = list(map(int, input().split()))
    convenience = list(list(map(int, input().split())) for _ in range(n))
    festival = list(map(int, input().split()))
    # 편의점 위치 리스트 마지막에 페스티벌 위치를 추가
    convenience.append(festival)
    # 움직일 수 있는 최대 거리 저장
    beer_distance = 20*50
    # 해당 지점 방문 여부를 표시할 방문 배열 생성
    visited = [0]*(n+1)
    # 결과르 저장할 변수(못간다고 가정)
    result = 'sad'
    # 큐 사용
    q = deque()
    # 큐에 시작점인 집 위치를 추가
    q.append(house)
    while q:
        x, y = q.popleft()
        # 페스티벌 위치에 도달할 수 있으면
        if [x, y] == festival:
            # 결과에 happy 저장
            result = 'happy'
        # 편의점 위치 리스트 반복
        for i in range(n+1):
            # 거리가 1000이하이고 방문을 안한 경우 실행
            if abs(x-convenience[i][0]) + abs(y-convenience[i][1]) <= beer_distance and visited[i] == 0:
                # 방문여부를 표시하고 큐에 추가
                visited[i] = 1
                q.append(convenience[i])
    print(result)