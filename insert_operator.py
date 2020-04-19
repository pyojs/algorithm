def calculator(k, r):
    global max_result, min_result
    if k == N-1:
        if r > max_result:
            max_result = r
        if r < min_result:
            min_result = r
    else:
        for i in range(4):
            if operator[i]:
                operator[i] -= 1
                if i == 0:
                    calculator(k+1, r+num_list[k+1])
                elif i == 1:
                    calculator(k+1, r-num_list[k+1])
                elif i == 2:
                    calculator(k+1, r*num_list[k+1])
                elif i == 3:
                    calculator(k+1, int(r/num_list[k+1]))
                operator[i] += 1

N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_result = -987654321
min_result = 987654321

calculator(0, num_list[0])
print(max_result)
print(min_result)