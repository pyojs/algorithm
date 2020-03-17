r1, c1, r2, c2 = map(int, input().split())
n = max(abs(r1), abs(c1), abs(r2), abs(c2))
arr = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

if n % 2 == 0:
    temp = n + 1

x, y = n, n
k = 1

cnt = 1
turn = 0
a = 1
d = 0

while k <= (2*temp+1)**2:
    if k == 1:
        if x >= c1+n and x <= c2+n and y >= r1+n and y <= r2+n:
            arr[y][x] = k
        x += 1
        k += 1
        a += 1
    else :
        if x >= c1+n and x <= c2+n and y >= r1+n and y <= r2+n:
            arr[y][x] = k
        x += dx[d%4]
        y += dy[d%4]
        if turn == 4:
            turn = 0
            a += 2
            x += 1
            y += 1
        cnt += 1
        k += 1
        if cnt == a:
            d += 1
            cnt = 0
            turn += 1

for j in range(len(arr)):
    for i in range(len(arr[j])):
        print('{:2}'.format(arr[j][i]), end = ' ')
    print()