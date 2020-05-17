# BAEKJOON 15665. N과 M (11)

# 수열을 만들고 출력하기 위한 함수
def sequence(k):
    # M개를 고른 경우 출력
    if k == M:
        print(*result)
    # 아직 M개를 고르지 못한 경우
    else:
        for i in range(len(arr)):
            # 결과에 추가하고 재귀 실행
            result.append(arr[i])
            sequence(k+1)
            # 사용이 끝난 경우 결과에서 제거
            result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 입력된 배열에서 중복된 숫자 제거
arr = list(set(arr))
# 입력된 수를 오름차순으로 정렬
arr.sort()
# 결과를 저장할 배열
result = []
sequence(0)