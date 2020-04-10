class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n 

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new 

    if lst.head is None:       
        lst.head, lst.tail = first, last

    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None:
            first.prev = lst.tail
            lst.tail.next = first
            lst.tail = last
        elif cur.prev is None:
            last.next = lst.head
            lst.head.prev = last
            lst.head = first
        else:
            prev = cur.prev
            first.prev = prev
            last.next = cur
            prev.next = first
            cur.prev = last
    lst.size += len(arr)

def printList(lst):
    if lst.head is None:
        return 
    cur = lst.tail
    for _ in range(10):
        print(cur.data, end = ' ')
        cur = cur.prev
    
T = int(input())

for tc in range(1, T+1):
    print("#{}".format(tc), end=' ')
    N, M = map(int, input().split())
    numbers = LinkedList()
    for m in range(M):
        arr = list(map(int, input().split()))
        addList(numbers, arr)
    printList(numbers)
    print()