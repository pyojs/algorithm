# BAEKJOON 15664. N과 M (10)

# 수열을 만들고 출력하기 위한 함수
def sequence(k):
    # M개를 고른 경우 출력
    if k == M:
        print(*result)
    # 아직 M개를 고르지 못한 경우
    else:
        for i in range(len(arr)):
            # 정렬된 배열에서 수의 개수만큼 사용하지 않고 비내림차순인 경우 실행
            if k == 0 or (visit_count[i] != arr_dict[arr[i]] and result[-1] <= arr[i]):
                # 수의 사용 횟수를 +1
                visit_count[i] += 1
                # 결과에 추가하고 재귀 실행
                result.append(arr[i])
                sequence(k+1)
                # 수의 사용이 끝난 경우 사용 횟수를 줄이고 결과에서 제거
                visit_count[i] -= 1
                result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 중복된 숫자의 개수를 세기 위한 딕셔너리 생성
arr_dict = {}
for i in range(N):
    arr_dict[arr[i]] = arr_dict.get(arr[i], 0) + 1
# 입력된 배열에서 중복된 숫자 제거
arr = list(set(arr))
# 입력된 수를 오름차순으로 정렬
arr.sort()
# 입력된 배열에서 숫자의 사용 회수를 검사할 배열
visit_count = [0]*len(arr_dict)
# 결과를 저장할 배열
result = []
sequence(0)