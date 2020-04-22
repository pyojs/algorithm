# SW Expert Academy 2819. 격자판의 숫자 이어 붙이기

# 배열의 인덱스 내부임을 확인하기 위한 함수
def wall(x, y):
    if x > N-1 or x < 0 or y > N-1 or y < 0:
        return False
    return True

# 숫자를 생성하기 위한 함수
def num_make(s, x, y, r):
    # 일곱 자리 수가 완성되었을 때
    if s == 6:
        # 결과값에 들어가 있지 않다면 추가
        if r not in result:
            result.append(r)
    else:
        # 4가지 방향으로 가기 위한 반복문
        for d in range(4):
            if wall(x+dx[d], y+dy[d]):
                num_make(s+1, x+dx[d], y+dy[d], r+arr[y+dy[d]][x+dx[d]])

T = int(input())
for tc in range(1, T+1):
    N = 4
    # str로 사용하는 것이 편해 그대로 받아옴
    arr = [list(input().split()) for _ in range(N)]
    # 우, 좌, 하, 상
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 결과값들을 저장할 리스트
    result = []
    # 배열의 모든 원소를 방문하기 위한 반복문
    for j in range(N):
        for i in range(N):
            num_make(0, i, j, arr[j][i])
    
    print('#{} {}'.format(tc, len(result)))
