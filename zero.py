N = int(input())
result_list = []
for n in range(N):
    temp = int(input())
    if temp == 0:
        result_list.pop()
    else:
        result_list.append(temp)
print(sum(result_list))