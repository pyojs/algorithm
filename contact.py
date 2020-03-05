# BFS를 이용한 함수
def check(q):
    global max_num
    next_q = []
    temp_max_num = 0
    # q에 있는 개수만큼 반복
    while len(q):
        # 앞에 있는 숫자부터 처리
        n = q.pop(0)
        visited[n] = 1
        # 결과 저장
        if n > temp_max_num:
            temp_max_num = n
        # 다음에 방문할 노드에서 다시 방문할 노드를 탐색
        if n in c_dict:
            while len(c_dict[n]):
                n_temp = c_dict[n].pop()
                # 이미 방문한 경우 뒤에 내용 실행 X
                if visited[n_temp]:
                    continue
                # 방문하지 않았을 경우 다음에 실행하기 위핸 next_q에 저장
                next_q.append(n_temp)
    # 다음에 방문할 노드가 있을 경우 다시 함수 실행
    if len(next_q):
        check(next_q)
    # 아닌 경우 최종 결과 저장
    else:
        max_num = temp_max_num

T = 10
for t in range(1, T+1):
    L, S = map(int, input().split())
    temp_arr = list(map(int, input().split()))
    c_dict = {}
    # 각 노드에서 갈 수 있는 노드를 딕셔너리로 생성
    for i in range(0, len(temp_arr), 2):
        if temp_arr[i] in c_dict:
            c_dict[temp_arr[i]].append(temp_arr[i+1])
        else:
            c_dict[temp_arr[i]] = [temp_arr[i+1]]
    # 중복된 것이 있을 경우 제거
    for n in c_dict:
        c_dict[n] = list(set(c_dict[n]))
    # 방문 배열 생성(인덱스를 맞추기 위해 +1)
    visited = [0] * (L+1)
    max_num = 0
    # 시작점부터 함수 시작
    check([S])
    print('#{} {}'.format(t, max_num))