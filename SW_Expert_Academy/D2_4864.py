# SW Expert Academy 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    # 결과를 저장할 변수
    result = 0
    # 문자열 인덱스를 바꾸기 위한 변수
    i, j = 0, 0
    while j < len(str2) and i < len(str1):
        # 글자가 일치하지 않는 경우
        if str1[i] != str2[j]:
            # 시작점 수정
            j -= i
            i = -1
        # 글자가 일치하는 경우 각 문자열 다음 인덱스 비교
        j += 1
        i += 1
        # 문자열 1의 길이만큼 된 경우 결과를 저장하고 종료
        if i == len(str1):
            result = 1
            break
    print('#{} {}'.format(tc, result))
