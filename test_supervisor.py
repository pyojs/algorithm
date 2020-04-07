N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for a in A:
    result += 1
    temp = a - B
    if temp > 0:
        result += temp//C
        if temp/C - temp//C > 0:
            result += 1

print(result)