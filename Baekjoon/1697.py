# BAEKJOON 1697. 숨바꼭질

from collections import deque

N, K = map(int, input().split())
# 결과를 저장할 변수
result = 0
# 거리를 저장할 배열
distance = [0]*100001
# 큐 활용
q = deque()
q.append(N)
while q:
    x = q.popleft()
    # 동생 위치에 도달한 경우
    if x == K:
        # 결과에 거리를 저장하고 종료
        result = distance[x]
        break
    else:
        # 다음으로 갈 수 있는 위치 검사
        for next_x in (x+1, x-1, x*2):
            # 인덱스 내부, 해당 위치에 방문 하지 않았던 경우 실행
            if next_x >= 0 and next_x <= 100000 and distance[next_x] == 0:
                distance[next_x] = distance[x] + 1
                q.append(next_x)
print(result)