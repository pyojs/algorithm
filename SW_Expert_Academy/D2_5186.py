# SW Expert Academy 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    # 자리수를 검사할 변수
    cnt = 0
    # 결과를 저장할 변수
    result = ''
    # N이 0이되거나 자리수가 13자리이상이 될 때 까지 반복
    while N != 0 and cnt < 13:
        # N을 2배 해주고 자리수를 하나 추가
        N *= 2
        cnt += 1
        # N이 1보다 크거나 같으면 1을 저장하고 N을 -1
        if N >= 1:
            result += '1'
            N -= 1
        # N이 1보다 작은 경우 0을 저장
        else:
            result += '0'
    # 자리수가 13자리 이상이면 overflow 출력
    if cnt == 13:
        print('#{} {}'.format(tc, 'overflow'))
    # 자리수가 13자리 미만이면 결과 출력
    else:
        print('#{} {}'.format(tc, result))