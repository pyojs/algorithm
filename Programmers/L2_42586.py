# programmers Level2_42586. 기능개발

def solution(progresses, speeds):
    # 결과를 저장할 배열
    answer = []
    # 모든 작업을 마칠 때까지 반복문 실행
    while progresses:
        # 작업을 진행하는 반복문
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
        # 배포할 기능 개수를 기록할 변수
        temp_answer = 0
        # 제일 앞의 기능의 개발이 완료된 경우
        if progresses[0] >= 100:
            # 배포 개수 증가
            temp_answer += 1
            # 이후에 있는 기능 탐색
            for i in range(1, len(progresses)):
                # 개발 완료가 안된 경우 반복문 종료
                if progresses[i] < 100:
                    break
                # 개발 완료가 된 경우 배포 개수 증가
                else:
                    temp_answer += 1
        # 배포 개수만큰 제거
        for _ in range(temp_answer):
            progresses.pop(0)
            speeds.pop(0)
        # 배포될 것이 있는 경우
        if temp_answer:
            # 결과에 추가
            answer.append(temp_answer)
    return answer