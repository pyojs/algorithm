# BAEKJOON 7568. 덩치

N = int(input())
people = list(list(map(int, input().split())) for _ in range(N))
# 등수를 저장할 변수
result = [1]*N
# 등수를 정하기 위한 반복문
for j in range(N):
    for i in range(N):
        # 같은 인덱스가 아닐 때 실행
        if i != j:
            # 몸무게와 키가 모두 작은 경우
            if people[j][1] < people[i][1] and people[j][0] < people[i][0]:
                # 등수를 +1
                result[j] += 1
print(*result)