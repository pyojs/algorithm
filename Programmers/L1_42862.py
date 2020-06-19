# programmers Level1_42862. 체육복

def solution(n, lost, reserve):
    # 학생 정보를 기록할 딕셔너리 생성
    students = {}
    # 결과를 저장할 변수
    answer = 0
    # 학생 정보 딕셔너리 갱신
    for i in range(1, n+1):
        students[i] = 1
    # 잃어버리 정보 갱신
    for i in lost:
        students[i] -= 1
    # 여벌 정보 갱신
    for i in reserve:
        students[i] += 1
    # 체육복을 빌려주는 반복문
    for i in lost:
        for j in reserve:
            # 체육복이 없는 학생 근처에 여벌이 있는 학생이 있는 경우 빌려줌
            if students[i] == 0 and students[j] == 2 and abs(i-j) == 1:
                students[i] += 1
                students[j] -= 1
    # 체육복이 있는 학생들 수만큼 결과 증가
    for i in range(1, len(students)+1):
        if students[i]:
            answer += 1
    return answer