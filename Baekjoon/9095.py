# BAEKJOON 9095. 1, 2, 3 더하기

# 사용하는 숫자들
num_list = [1, 2, 3]

# 합을 만들기 위한 함수
def make_num(N, total):
    global cnt
    # 합이 입력된 정수와 같으면 개수 증가
    if total == N:
        cnt += 1
    # 합이 입력된 정수보다 커진 경우 종료
    elif total > N:
        return
    else:
        # 1, 2, 3을 더하며 재귀 사용
        for i in range(3):
            make_num(N, num_list[i]+total)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 카운트를 0에서 시작
    cnt = 0
    make_num(N, 0)
    print(cnt)