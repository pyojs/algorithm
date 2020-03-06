T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            x_cnt = 0
            y_cnt = 0
            testx = i
            testy = j
            # 0이 아닌 숫자가 발견될 경우 실행
            while testx < N and testy < N and arr[testy][testx]:
                # 행 길이 검사
                while testy < N and arr[testy][testx]:
                    testy += 1
                    y_cnt += 1
                testy = j
                # 열 길이 검사
                while testx < N and arr[testy][testx]:
                    testx += 1
                    x_cnt += 1
                testx = i
                # 행, 열, 크기 순서로 결과에 저장
                result.append([y_cnt, x_cnt, y_cnt*x_cnt])
                # 찾은 행렬을 모드 0으로 바꾸면서 다시 탐색하지 않도록 변경
                for y in range(y_cnt):
                    for x in range(x_cnt):
                        arr[testy+y][testx+x] = 0
    # 찾은 행렬을 정렬하는 코드(크기, 행 순서)
    result.sort(key=lambda x: (x[2], x[0]))
    
    print('#{} {} '.format(t, len(result)), end = '')
    for a in range(len(result)):
        print(*result[a][0:2], end = ' ')
    print()