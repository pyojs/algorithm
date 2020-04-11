class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addLast(data):
    global pHead 
    if pHead is None:
        pHead = Node(data, None)
        return
    p = pHead
    while p.link is not None:
        p = p.link 
    p.link = Node(data, None)
    return

def insert(idx, data):
    global pHead
    p = pHead
    n = 0
    if idx == 0:
        pHead = Node(data, pHead)
        return
    while n < idx-1:
        p = p.link
        n += 1 
    p.link = Node(data, p.link)
    return

def get(idx):
    global pHead
    p = pHead
    n = 0
    while p is not None and n < idx:
        p = p.link
        n += 1
    if p is not None:
        return p.data
    else:
        return -1

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    pHead = None
    s = list(map(int, input().split()))
    
    for i in range(N):
        addLast(s[i])

    for i in range(M):
        cmd = list(map(int, input().split()))
        insert(cmd[0], cmd[1])

    print("#{} {}".format(tc, get(L)))