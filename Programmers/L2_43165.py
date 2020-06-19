# programmers Level2_43165. 타겟 넘버

# 결과를 저장할 변수
answer = 0
def solution(numbers, target):
    # 결과를 구하기 위한 함수
    def target_number(k, total):
        global answer
        # 모든 숫자를 적용한 경우
        if k == len(numbers):
            # 값이 타겟과 같으면 결과 +1
            if total == target:
                answer += 1
        else:
            # 숫자를 더할지 뺄지 정하는 반복문
            for i in range(2):
                if i == 0:
                    target_number(k+1, total+numbers[k])
                else:
                    target_number(k+1, total-numbers[k])
    target_number(0, 0)
    return answer