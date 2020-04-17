# SW Expert Academy 3752. 가능한 시험 점수

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 가능한 점수를 결과에 추가했는지 확인하는 배열
    score_check = [1] + [0] * sum(arr)
    # 결과를 저장할 배열(0점은 무조건 나와서 미리 넣어둠)
    result_score = [0]
    # 각 문제의 점수를 기존 결과값에 더하며 최종 결과값을 만드는 반복문
    for k in arr:
        # 반목분을 수행하며 리스트 내용이 바뀌기 때문에 임시 리스트 생성
        temp = list(result_score)
        for n in temp:
            # 기존 결과에 없으면 추가하는 조건문
            if not score_check[n+k]:
                score_check[n+k] = 1
                result_score.append(n + k)
    print('#{} {}'.format(t, len(result_score)))