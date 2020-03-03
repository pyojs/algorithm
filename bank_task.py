T = int(input())
for t in range(1, T+1):
    N_2 = list(input())
    N_3 = list(input())

    N_2_result = []
    # 들어온 2진수를 하나씩 바꾸며 리스트에 저장
    for i in range(len(N_2)):
        if N_2[i] == '1':
            N_2[i] = '0'
            N_2_result.append(int(''.join(N_2), 2))
            N_2[i] = '1' 
        else:
            N_2[i] = '1'
            N_2_result.append(int(''.join(N_2), 2))
            N_2[i] = '0'
    
    N_3_result = []
    # 들어온 3진수를 하나씩 바꾸며 리스트에 저장
    for i in range(len(N_3)):
        if N_3[i] == '2':
            N_3[i] = '0'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '1'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '2'
        elif N_3[i] == '1':
            N_3[i] = '0'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '2'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '1'
        else :
            N_3[i] = '1'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '2'
            N_3_result.append(int(''.join(N_3), 3))
            N_3[i] = '0'

    result = 0
    # 2진수 결과 리스트에서 3진수 결과 리스트에 같은 값이 있는 숫자 저장
    for n in N_2_result:
        if n in N_3_result:
            result = n
            break
        
    print('#{} {}'.format(t, result))