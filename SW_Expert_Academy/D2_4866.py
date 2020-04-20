# SW Expert Academy 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

T = int(input())
for t in range(1, T+1):
    S = input()
    # 스택으로 활용할 리스트
    stack = []
    # 결과를 저장할 변수(가능하다고 가정)
    result = 1
    for i in S:
        # 여는 괄호인 경우 스택에 추가
        if i == '(' or i == '{':
            stack.append(i)
        # 닫는 괄호인 경우 실행
        if i == ')' or i == '}':
            # 스택에 괄호가 저장되어 있는 경우
            if len(stack) != 0:
                # 스택에 마지막에 추가되어 있는 괄호를 빼서 검사
                temp = stack.pop()
                # 짝이 맞으면 패스
                if i == ')' and temp == '(':
                    pass
                elif i == '}' and temp == '{':
                    pass
                # 짝이 맞지 않으면 결과를 0으로 바꾸고 종료
                else:
                    result = 0
                    break
            # 스택에 괄호가 없는데 닫는 괄호가 들어오면 결과를 0으로 바꾸고 종료
            else:
                result = 0
                break
    # 검사를 종료했는데 스택에 괄호가 남아있으면 결과를 0으로 바꿈
    if len(stack) != 0:
        result = 0
    
    print('#{} {}'.format(t, result))