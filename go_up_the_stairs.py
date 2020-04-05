def score(n):
    scores.append(stairs[0])
    if n == 1:
        return
    scores.append(stairs[0] + stairs[1])
    if n == 2:
        return
    scores.append(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))
    for i in range(3, N):
        scores.append(max(scores[i-3] + stairs[i-1] + stairs[i], scores[i-2] + stairs[i]))

N = int(input())
stairs = [int(input()) for _ in range(N)]
scores = []
score(N)
print(scores[-1])