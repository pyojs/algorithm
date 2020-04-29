# SW Expert Academy 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수

T = int(input())
for tc in range(1, T+1):
    N, num = input().split()
    # 결과를 저장할 변수
    result = ''
    # 각 자리수를 4자리 2진수로 표현하기 위한 반복문
    for n in range(int(N)):
        # 각 자리수를 4자리 2진수로 바꾸고 결과에 저장
        result += "{0:b}".format(int('0x'+num[n], 16)).zfill(4)
    print('#{} {}'.format(tc, result))