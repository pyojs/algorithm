# SW Expert Academy 1952. [모의 SW 역량테스트] 수영장

# 최소 가격을 계산하기 위한 함수
def check_price(k,s):
    global min_s
    if k > 11:
        # 계산한 가격이 현재 최소 가격보다 낮은 경우 저장
        if s < min_s:
            min_s = s
        else:
            return
        # 계산 도중 현재 최소 가격보다 커지는 경우 종료
    elif s > min_s:
        return
    else:
        # 1일, 1달, 3달 이용권 사용 경우를 계산
        for i in range(3):
            # 1일 이용권 사용 경우
            if i == 0:
                check_price(k+1, s + price[0]*month[k])
            # 1달 이용권 사용 경우
            elif i == 1:
                check_price(k+1, s + price[1])
            # 3달 이용권 사용 경우
            elif i == 2:
                check_price(k+3, s + price[2])

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    month = list(map(int, input().split()))
    # 1년 이용권을 최소 가격으로 설정해둠
    min_s = price[3]
    check_price(0,0)
    print('#{} {}'.format(tc, min_s))