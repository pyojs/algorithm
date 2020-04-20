# SW Expert Academy 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기

T = int(input())
for t in range(1, T+1):
    # 결과를 저장할 리스트
    result = []
    S = input()
    # 초기 설정(첫번째 글자만 넣음)
    result.append(S[0])
    for i in range(1, len(S)):
        # 결과 리스트에 문자가 있을 경우 실행
        if len(result) != 0:
            # 결과 리스트의 마지막 문자와 새로 들어오는 글자가 같은 경우 삭제
            if result[-1] == S[i]:
                result.pop()
            # 결과 리스트의 마지막 문자와 새로 들어오는 글자가 다른 경우 추가
            else:
                result.append(S[i])
        # 결과 리스트에 문자가 없으면 추가
        else:
            result.append(S[i])
    print('#{} {}'.format(t, len(result)))