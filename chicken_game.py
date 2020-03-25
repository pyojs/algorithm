def chicken(a, k):
    global chicken_distance
    # 치킨집 M개를 선택한 경우 실행
    if k == M:
        # 거리 비교를 위한 임시 배열
        temp_distance = [987654321] * len(house_location)
        # 선택된 치킨집의 치킨 거리 조사
        for m in range(len(chicken_location)):
            if selec_chicken[m] == 1:
                for h in range(len(house_location)):
                    # 치킨 거리 임시 저장
                    temp_result = abs(chicken_location[m][0]-house_location[h][0]) + abs(chicken_location[m][1]-house_location[h][1])
                    # 현재 선택에서 치킨 거리를 비교하며 작은 값을 넣음
                    if  temp_result < temp_distance[h]:
                        temp_distance[h] = temp_result
        # 현재 선택에서 치킨거리 합을 최종 값과 비교하며 작을 경우 저장                        
        if sum(temp_distance) < sum(chicken_distance):
            chicken_distance = temp_distance
    # 치킨집 M개를 선택하기 위한 재귀
    else:
        for n in range(a, len(chicken_location)):
            if selec_chicken[n] == 0:
                selec_chicken[n] = 1
                chicken(n, k+1)
                selec_chicken[n] = 0

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
# 집의 위치와 치킨집의 위치를 저장
house_location = []
chicken_location = []
for j in range(N):
    for i in range(N):
        if city[j][i] == 1:
            house_location.append([i, j])
        elif city[j][i] == 2:
            chicken_location.append([i, j])
# 치킨집 선택을 위한 방문 배열
selec_chicken = [0] * len(chicken_location)
# 결과를 저장할 배열
chicken_distance = [987654321] * len(house_location)
chicken(0, 0)
print(sum(chicken_distance))