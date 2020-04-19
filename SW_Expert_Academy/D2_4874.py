# SW Expert Academy 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth

T = int(input())
for tc in range(1, T+1):
    arr = list(input().split())
    # 연산자 종류
    task_list = ['+', '-', '*', '/']
    # 스택 연산을 하기 위한 리스트
    result_list = []
    # 결과를 저장할 변수 생상
    result = ''
    for s in arr:
        # 들어온 것이 연산자인 경우
        if s in task_list:
            # 숫자가 하나인데 연산자가 들어온 경우 에러
            if len(result_list) == 1:
                result = 'error'
                break
            # 숫자가 두개 이상인 경우 연산 후 저장
            a = int(result_list.pop())
            b = int(result_list.pop())
            if s == '+':
                temp = b + a
            elif s == '-':
                temp = b - a
            elif s == '*':
                temp = b * a
            elif s == '/':
                temp = b // a
            result_list.append(str(temp))
        # 들어온 것이 .일 경우
        elif s == '.':
            # 숫자가 하나 남아 있으면 출력
            if len(result_list) == 1:
                result = result_list.pop()
            # 숫자가 여러개 남아 있는 경우 에러
            else:
                result = 'error'
                break
        # 들어온 것이 숫자일 경우
        else:
            result_list.append(s)
    print('#{} {}'.format(tc, result))