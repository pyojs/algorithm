T = int(input())
for t in range(1, T+1):
    arr = []
    max_len = 0
    # 단어 중 제일 긴 길이를 찾음
    for n in range(5):
        arr.append(input())
        if len(arr[n]) > max_len:
            max_len = len(arr[n])
    # 찾을 길이로 배열 생성
    result_arr = [['' for _ in range(max_len)] for _ in range(max_len)]
    # 생성한 배열에 입력된 단어를 넣음(짧은 길이는 빈 공간 남김)
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            result_arr[j][i] = arr[j][i]
    #세로로 출력
    print('#{} '.format(t), end = '')
    for j in range(len(result_arr)):
        for i in range(len(result_arr[j])):
            print(result_arr[i][j], end = '')
    print()