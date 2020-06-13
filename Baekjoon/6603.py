# BAEKJOON 6603. 로또

def find(n, a):
    # 6개의 수를 선택한 경우
    if n == 6:
        print(*result)
    else:
        # 오름차순으로 출력
        for i in range(a, len(S)):
            # 아직 숫자를 사용 안한 경우
            if visited[i] == 0:
                # 사용 여부에 체크, 결과에 추가하고 재귀 실행
                visited[i] = 1
                result.append(S[i])
                find(n+1, i+1)
                # 사용이 끝난 경우 사용 여부를 없애고, 제거
                visited[i] = 0
                result.pop()

while 1:
    arr = list(map(int, input().split()))
    # 마지막 입력줄인 경우(0이 들어온 경우) 종료
    if arr[0] == 0:
        break
    else:
        # k와 S로 분리
        k, S = arr[0], arr[1:]
        # 방문 여부를 저장할 배열 생성
        visited = [0]*len(S)
        # 결과를 저장할 배열 생성
        result = []
        find(0, 0)
    print()