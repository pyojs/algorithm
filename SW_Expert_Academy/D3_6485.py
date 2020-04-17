# SW Expert Academy 6485. 삼성시의 버스 노선

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # 결과를 저장할 딕셔너리 생성
    result_dict = {}
    for n in range(N):
        A, B = list(map(int, input().split()))
        # 노선 정보를 받아서 지나는 정류장의 count를 하나씩 증가
        for m in range(A, B+1):
            result_dict[m] = result_dict.get(m, 0) + 1
    P = int(input())
    C = []
    for c in range(P):
        C.append(int(input()))
  
    print('#{}'.format(t), end = ' ')
    
    # 출력을 원하는 정류장의 count를 딕셔너리에 가져옴
    # 딕셔너리에 없을 경우 0을 출력
    for x in C:
        if x in result_dict:
            print(result_dict[x], end =' ')
        else:
            print('0', end = ' ')
    print()