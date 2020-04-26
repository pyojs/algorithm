# SW Expert Academy 1259. [S/W 문제해결 응용] 7일차 - 금속막대

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    stick = list(map(int, input().split()))
    # 기준을 잡을 금속 막대(입력 1번째) 선정
    chain = stick[0:2]
    
    # 막대가 모두 연결될 때까지 진행
    while len(chain) != 2*n:
        for i in range(2, 2*n, 2):
            # 연결되어있는 막대의 뒷부분과 일치할 경우 추가
            if stick[i] == chain[len(chain)-1]:
                chain.append(stick[i])
                chain.append(stick[i+1])
            # 연결되어있는 막대의 앞부분과 일치할 경우 추가
            if stick[i+1] == chain[0]:
                chain.insert(0, stick[i+1])
                chain.insert(0, stick[i])

    print('#{} '.format(tc), end = '')
    print(*chain)
