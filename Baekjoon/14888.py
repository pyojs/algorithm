# BAEKJOON 14888. 연산자 끼워넣기

# 최대값과 최소값을 찾기 위한 함수
def calculator(k, r):
    global max_result, min_result
    # 연산자를 다 사용한 경우 실행
    if k == N-1:
        # 기존의 결과와 비교하며 값 저장
        if r > max_result:
            max_result = r
        if r < min_result:
            min_result = r
    else:
        for i in range(4):
            # 연산자가 있는 경우 실행
            if operator[i]:
                # 사용했다는 의미로 -1
                operator[i] -= 1
                # +
                if i == 0:
                    calculator(k+1, r+num_list[k+1])
                # -
                elif i == 1:
                    calculator(k+1, r-num_list[k+1])
                # *
                elif i == 2:
                    calculator(k+1, r*num_list[k+1])
                # /
                elif i == 3:
                    calculator(k+1, int(r/num_list[k+1]))
                # 사용이 끝나면 다시 +1
                operator[i] += 1

N = int(input())
num_list = list(map(int, input().split()))
operator = list(map(int, input().split()))
# 결과를 저장할 변수
max_result = -987654321
min_result = 987654321

calculator(0, num_list[0])
print(max_result)
print(min_result)