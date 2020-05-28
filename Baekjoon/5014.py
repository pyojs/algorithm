# BAEKJOON 5014. 스타트링크

from collections import deque

F, S, G, U, D = map(int, input().split())
# 결과를 저장할 변수(기본으로 못간다고 가정)
result = 'use the stairs'
# 층에 가기 위해 눌러야할 버튼 횟수를 저장하기 위한 배열
cnt = [0]*(F+1)
cnt[S] = 1
# 큐 사용
q = deque()
q.append(S)
while q:
    location = q.popleft()
    # 해당 위치에 도달할 경우
    if location == G:
        # 결과에 저장하고 종료
        result = cnt[location] - 1
        break
    # U버튼과 D 버튼을 누르는 경우
    for i in [U, D]:
        # U 버튼이면서 최대 층수를 초과하지 않고 층에 도착한 적이 없는 경우
        if i == U and location+U <= F and cnt[location+U] == 0:
            cnt[location+U] = cnt[location] + 1
            q.append(location+U)
        # D 버튼이면서 1층 보다 높고 층에 도착한 적이 없는 경우
        elif i == D and location-D >=1 and cnt[location-D] == 0:
            cnt[location-D] = cnt[location] + 1
            q.append(location-D)
print(result)