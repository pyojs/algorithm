# SW Expert Academy 4676. 늘어지는 소리 만들기

T = int(input())
for tc in range(1, T+1):
    sound = list(input())
    H = int(input())
    location = list(map(int, input().split()))
    # -을 추가할 위치를 세는 배열 생성
    location_cnt = [0]*(len(sound)+1)
    for n in location:
        location_cnt[n] += 1
    # 뒤쪽부터 -을 추가
    for i in range(len(location_cnt)-1, -1, -1):
        if location_cnt[i]:
            sound.insert(i, '-'*location_cnt[i])
    # join을 통해 다시 합해서 출력
    print('#{} {}'.format(tc,''.join(sound)))