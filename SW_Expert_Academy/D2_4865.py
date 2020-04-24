# SW Expert Academy 4865. [파이썬 S/W 문제해결 기본] 3일차 - 글자수

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # 결과를 저장할 딕셔너리
    s_dict = {}
    # 딕셔너리 초기 세팅
    for s in str1:
        s_dict[s] = 0
    # 문자열 1에 포함된 글자가 문자열 2에 몇 개 있는지 검사
    for s in str2:
        if s in s_dict:
            s_dict[s] += 1
    # 최종 결과를 저장할 변수
    result = 0
    for val in s_dict.values():
        if val > result:
            result = val
    
    print('#{} {}'.format(tc, result))
