# programmers Level1_42576. 완주하지 못한 선수

def solution(participant, completion):
    # 참가한 선수 정보를 저장할 딕셔너리 생성
    participant_dic = {}
    # 참가자 이름을 기준으로 딕셔너리 갱신
    for i in participant:
        participant_dic[i] = participant_dic.get(i, 0) + 1
    # 완주자 이름을 기준으로 딕셔너리 갱신
    for i in completion:
        participant_dic[i] = participant_dic.get(i, 0) - 1
    # 이름이 남아있는 경우 리턴
    for name, i in participant_dic.items():
        if i > 0:
            return name