# BAEKJOON 2231. 분해합

N = int(input())
# 결과를 저장하는 변수(생성자 없다고 가정)
result = 0
# 입력된 수까지 모든 수를 반복문으로 대입
for n in range(N+1):
    # 각 자리수를 표시해주기 위해 str 활용
    numbers = str(n)
    # 분해합을 저장할 변수
    total = n
    # total에 각 자리수를 더함
    for number in numbers:
        total += int(number)
    # 입력된 분해합과 같은 total이 나오면 n을 저장하고 종료
    if total == N:
        result = n
        break
print(result)