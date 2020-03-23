# 점의 임시 x 위치를 찾기 위한 함수
def temp_x(dot):
    for x in range(len(arr)-1):
        if dot >= arr[x] and dot < arr[x+1]:
            return x
# 점의 정확한 위치를 찾는 함수
def result_xy(dot, x_temp):
    y_temp= 0
    # 점의 숫자와 x_temp가 같은 경우 x축 가장 밑줄에 해당함으로 바로 리턴
    if dot != arr[x_temp]:
        # 다른 경우 정확한 위치를 찾기 위해 반복문 수행
        x_temp += 1
        temp_r = arr[x_temp]
        while temp_r != dot:
            temp_r -= 1
            x_temp -= 1
            y_temp += 1
    return x_temp, y_temp

T = int(input())
# x축에 가장 밑줄에 해당하는 숫자들을 배열에 저장
arr = [1]
i = 1
while 1:
    arr.append(arr[i-1] + i+1)
    # p와 q의 범위가 10000 이하 -> 적당한 크기 생성
    if len(arr) > 300 :
        break
    i += 1

for tc in range(1, T+1):
    p, q = map(int, input().split())
    # p, q의 현재 임시 x 위치를 찾음
    x_temp_p = temp_x(p)
    x_temp_q = temp_x(q)
    
    # p, q의 정확한 x, y 위치를 찾음
    x_temp_p, y_temp_p = result_xy(p, x_temp_p)
    x_temp_q, y_temp_q = result_xy(q, x_temp_q)

    # p, q 위치로 결과 위치를 찾음
    x_result = x_temp_p + x_temp_q
    y_result = y_temp_p + y_temp_q

    # 연산 결과로 나온 점을 찾음
    result = arr[x_result + y_result + 2] - y_result - 1
    print('#{} {}'.format(tc, result))