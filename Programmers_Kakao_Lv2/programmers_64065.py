# 2022.03.16 (수)
# 프로그래머스 level2
# 튜플

def solution(s):
    answer = []
    # 앞뒤에 필요없는 문자 없애고, 배열로 자르기
    s1 = s[2:-2].split('},{')
    # print(s1)

    sList = []
    # 문자열 값을 배열로 만든다음
    # 딕셔너리를 만들어서 (key, value) 를 (튜플길이, 튜플값) 로 넣어준다
    sDict = dict()
    for i in range(len(s1)):
        sList = s1[i].split(',')
        sDict[len(sList)] = sList
    # print(sDict)

    # key가 작은것부터 반복하면서 answer에 넣어주고,
    for i in range(len(list(sDict.keys()))):
        idx = i+1
        if idx == 1:
            answer.append(sDict[idx][0])
        else:
            # 다음 key에서 answer에 들어가있는 값 제외하고 남는 값 넣어주기
            target = [j for j in sDict[idx] if j not in answer]
            answer.append(target[0])

    # 문자열을 숫자로 변경
    for i in range(len(answer)):
        answer[i] = int(answer[i])

    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))