# SW Expert Academy 4008. [모의 SW 역량테스트] 숫자 만들기

# 연산을 하기 위한 함수
def cal(k, i, r):
    # 초기 r을 num_list[0]로 설정
    one = r
    two = num_list[k+1]
    if i == 0:
        r = one + two
    elif i == 1:
        r = one - two
    elif i == 2:
        r = one * two
    elif i == 3:
        # 소수점 이하 버림을 하기 위한 int
        r = int(one/two)
    # 연산 결과를 리턴
    return r

# 순열을 구하기 위한 함수
def per(k, r):
    global max_result, min_result
    # 연산자 개수만큼 반복한 경우 결과값 비교 (연산자 개수 : N-1)
    if k == N-1:
        # 최대, 최소 확인
        if r > max_result:
            max_result = r
        if r < min_result:
            min_result = r
        return
    else:
        # 연산자 개수 리스트에 있는 값을 수정하면서 재귀함수 사용
        for i in range(len(oper_num)):
            # 연산자 개수가 0이 아닐 경우 구문 실행
            if oper_num[i]:
                # 연산자를 사용할 경우 해당 값 -1
                oper_num[i] -= 1
                per(k+1, cal(k, i, r))
                # 사용이 끝난 경우 다시 해당 값 +1
                oper_num[i] += 1
        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # ['+', '-', '*', '/'] 연산자 순서
    oper_num = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    max_result = -987654321
    min_result = 987654321
    per(0, num_list[0])
    print('#{} {}'.format(tc, max_result-min_result))