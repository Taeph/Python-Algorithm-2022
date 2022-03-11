# 프로그래머스 level1
# 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    
    # 중복된 신고는 1건으로 보기 때문에, 집합자료형으로 중복제거
    report_set = set()
    for i in report:
        report_set.add(i)
    # print(report_set)

    # 신고한사람, 신고당한사람 딕셔너리자료형 생성해서 관리
    id_dict = dict()
    id_result = dict()
    for i in id_list:
        id_dict[i] = []
        id_result[i] = 0
    # print(id_dict)

    # 신고받은사람 딕셔너리에 신고한사람 리스트로 추가
    for i in report_set:
        a,b = i.split()
        id_dict[b].append(a)
    # print(id_dict)

    # 신고횟수보다 크거나 같은 사람 찾아서, 신고한사람 숫자 넣어주기
    for i in id_dict:
        if len(id_dict[i]) >= k:
            for j in id_dict[i]:
                id_result[j] += 1            
    # print(id_result)

    # 결과에 넣기
    for i in id_result:
        answer.append(id_result[i])
    # print(answer)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3

answer = solution(id_list, report, k)
print(answer)