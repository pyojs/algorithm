# SW Expert Academy 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    # 화물의 무게와 트럭의 적재용량을 내림차순 정렬
    w.sort(reverse=True)
    t.sort(reverse=True)
    # 결과를 저장할 변수
    result = 0
    # 트럭 번호를 지정할 변수
    num = 0
    # 화물의 개수만큼 반복문 실행
    for i in range(len(w)):
        # 트럭의 적재용량보다 작거나 같은 화물인 경우
        if t[num] >= w[i]:
            # 결과에 더하고 다음 트럭을 불러옴
            result += w[i]
            num += 1
            # 트럭의 번호가 개수보다 커지면 종료
            if num == len(t):
                break
    print('#{} {}'.format(tc, result))