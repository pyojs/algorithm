num_list = [1, 2, 3]

def make_num(N, total):
    global cnt
    if total == N:
        cnt += 1
    elif total > N:
        return
    else:
        for i in range(3):
            make_num(N, num_list[i]+total)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cnt = 0
    make_num(N, 0)
    print(cnt)