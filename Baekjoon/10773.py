# BAEKJOON 10773. 제로

N = int(input())
# 결과를 저장할 배열
result_list = []
for n in range(N):
    num = int(input())
    # 0이 들어온 경우 가장 최근에 들어온 수 삭제
    if num == 0:
        result_list.pop()
    # 다른 숫자가 들어온 경우 추가
    else:
        result_list.append(num)
print(sum(result_list))