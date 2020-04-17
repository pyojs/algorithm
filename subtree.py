def count(k):
    global cnt
    if k in sub_dic:
        for i in sub_dic[k]:
            cnt += 1
            count(i)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    sub_dic = {}
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), 2):
        sub_dic[temp[i]] = sub_dic.get(temp[i], []) + [temp[i+1]]
    cnt = 1
    count(N)
    print('#{} {}'.format(tc, cnt))