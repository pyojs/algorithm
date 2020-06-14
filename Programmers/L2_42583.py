  # programmers 42583. 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    # 시간 결과를 저장할 변수
    answer = 1
    # 다리를 지나고 있는 트럭을 저장할 배열
    cross = []
    # 다리를 지나고 있는 트럭의 시간을 저장할 배열
    temp_time = []
    # 다리를 건너게 하기 위한 반복문
    while True:
        # 시간 +1
        answer += 1
        # 건너지 않은 트럭이 있는 경우
        if len(truck_weights) > 0:
            # 다리 위에 트럭과 건너야할 트럭의 무게 합이 다리가 견딜 수 있는 무게보다 작은 경우
            if sum(cross) + truck_weights[0] <= weight:
                # 다리 위에 트럭을 추가
                cross.append(truck_weights.pop(0))
                # 추가한 트럭의 시간 추가
                temp_time.append(0)
        # 다리 위에 있는 트럭들의 시간 +1
        for i in range(len(temp_time)):
            temp_time[i] += 1
        # 맨 앞의 트럭 시간이 다리 길이 만큼 된 경우
        if temp_time[0] == bridge_length:
            # 건너는 배열과 시간 배열에서 제거
            cross.pop(0)
            temp_time.pop(0)
        # 건너는 트럭과 건너야할 트럭이 없는 경우 종료
        if len(cross) == 0 and len(truck_weights) == 0:
            break
    
    return answer