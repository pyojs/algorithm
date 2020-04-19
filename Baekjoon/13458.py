# BAEKJOON 13458. 시험 감독

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

result = 0
for a in A:
    # 총감독관 수 1명 더함
    result += 1
    # 남은 사람 수 계산
    remainder = a - B
    # 남은 사람이 양수인 경우 실행
    if remainder > 0:
        # 부감독관 수를 계산해서 더함
        result += remainder//C
        # 나머지가 남는 경우 부감독관 수 +1
        if remainder/C - remainder//C > 0:
            result += 1
print(result)