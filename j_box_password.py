T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    # 사각형은 변이 4개 -> 각 변에 들어가는 숫자 개수 체크
    r = N//4
    result = []
    # 한 변에 들어가 있는 숫자 개수만큼 반복한 후에는 처음과 같은 상태
    for i in range(r):
        for j in range(0, len(arr), r):
            # 슬라이싱을 해서 결과에 추가 안되어 있을 경우만 append
            if arr[j:j+r] not in result:
                result.append(arr[j:j+r])
        # 배열의 맨 뒤의 항목을 맨 앞으로 가져옴
        arr.insert(0, arr.pop())
    
    for n in range(len(result)):
        # str로 들어가 있기 때문에 join을 이용하여 16진수로 만들고, int를 이용하여 10진수로 변환
        result[n] = int(''.join(result[n]),16)

    # 내림차순으로 정렬(K번째로 큰 수이기 때문)
    result.sort(reverse=True)

    print('#{} {}'.format(t, result[K-1]))