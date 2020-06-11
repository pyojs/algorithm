# BAEKJOON 10828. 스택

import sys

input = sys.stdin.readline

N = int(input())
# 스택 구현을 위한 리스트 생성
stack = []
for _ in range(N):
    commmand = input().strip()
    # push인 경우
    if commmand[:4] == 'push':
        stack.append(int(commmand[5:]))
    # pop인 경우
    elif commmand == 'pop':
        # 스택에 정수가 존재하는 경우
        if len(stack):
            print(stack.pop())
        # 스택에 정수가 없는 경우
        else:
            print(-1)
    # size인 경우
    elif commmand == 'size':
        print(len(stack))
    # empty인 경우
    elif commmand == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    # top인 경우
    else:
        # 스택에 정수가 존재하는 경우
        if len(stack):
            print(stack[-1])
        # 스택에 정수가 없는 경우
        else:
            print(-1)