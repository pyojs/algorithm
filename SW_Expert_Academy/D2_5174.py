# SW Expert Academy 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree

# 서브 트리에 속한 노드의 개수를 알아내기 위한 함수
def count(k):
    global cnt
    # 자식 노드가 있는 경우 실행
    if k in sub_dic:
        # 자식 노드의 자식 노드들에 대해서 재귀 실행
        for i in sub_dic[k]:
            cnt += 1
            count(i)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 자식 노드 정보를 저장할 딕셔너리
    sub_dic = {}
    temp = list(map(int, input().split()))
    for i in range(0, len(temp), 2):
        sub_dic[temp[i]] = sub_dic.get(temp[i], []) + [temp[i+1]]
    cnt = 1
    count(N)
    print('#{} {}'.format(tc, cnt))