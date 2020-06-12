# BAEKJOON 9012. 괄호

T = int(input())
for _ in range(T):
    PS = input()
    # 스택 사용을 위한 배열 생성
    stack = []
    for s in PS:
        # 들어온 문자가 (인 경우
        if s == '(':
            # 스택에 추가
            stack.append(s)
        # 들어온 문자가 )인 경우
        else:
            # 스택에 문자가 존재하고 마지막이 (인 경우
            if len(stack) and stack[-1] == '(':
                # 스택의 마지막 괄호 제거
                stack.pop()
            # 아닌 경우 NO를 출력하고 종료
            else:
                print('NO')
                break
    # 반복문을 다 돌 경우
    else:
        # 스택에 문자가 남아 있으면
        if len(stack):
            # NO를 출력
            print('NO')
        # 스택이 비어 있으면
        else:
            # YES 출력
            print('YES')