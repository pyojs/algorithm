T = 10
for t in range(1, T+1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    # 각 노드가 실행되었는지 확인하는 리스트
    visited = [True for _ in range(v+1)]
    temp_list = list(map(int, input().split()))
    # 각 노드 번호 다음에 할 수 있는 작업을 저장
    for i in range(0, len(temp_list), 2):
        a = temp_list[i]
        b = temp_list[i+1]
        graph[b].append(a)
    # 결과를 저장할 리스트
    result = []
    # 노드를 결과값에 저장했는지 확인할 리스트
    do_list = [i for i in range(1, v+1)]
    count = v
    while count:
        for idx, i in enumerate(do_list):
            # 선행 노드가 실행되었는지 확인
            for j in graph[i]:
                if visited[j]:
                    break
            else:  
                # 선행노드가 모두 수행되었으면 실행
                # 노드가 실행된 것을 표시
                visited[i] = False
                result.append(i)
                count -= 1
                # 결과값에 저장한 노드는 삭제
                do_list.pop(idx)
                break
    print('#{} '.format(t), end='')
    print(*result)