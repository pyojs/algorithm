# BAEKJOON 15651. N과 M (3)

def sequence(k):
    # 수열의 길이가 M이 되었을 때 출력
    if k == M:
        print(*result)
    # 수열의 길이가 M이 안될 때
    else:
        # 1부터 N까지의 숫자를 차례로 넣음
        for i in range(1, N+1):
            # 결과 배열의 마지막 숫자보다 작은 숫자를 넣을려고 할 때는 패스
            if result and i >= result[-1]:
                pass
            # 비내림차순인 경우
            else:
                # 결과에 추가하고 재귀 실행
                result.append(i)
                sequence(k+1)
                # 사용이 끝난 경우 제거
                result.pop()

N, M = map(int, input().split())
# 결과를 저장할 배열
result = []
sequence(0)
