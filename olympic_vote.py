T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A_vote = [0]*len(A)
    for i in range(len(B)):
        for j in range(len(A)):
            # B보다 작거나 같은 A가 나온 경우 수를 증가시킴
            # A를 반복하던 것도 중지
            if A[j] <= B[i]:
                A_vote[j] += 1
                break
    print('#{} {}'.format(tc, A_vote.index(max(A_vote))+1))