# programmers Level2_42588. 탑

def solution(heights):
    # 결과를 저장할 배열
    answer = [0] * len(heights)
    # 결과를 찾기 위한 반복문
    for i in range(len(heights)-1, -1, -1):
        for j in range(i, -1, -1):
            # 자신보다 왼쪽에 높은 탑을 만난 경우
            if heights[i] < heights[j]:
                # 결과에 저장하고 종료
                answer[i] = j+1
                break
    return answer