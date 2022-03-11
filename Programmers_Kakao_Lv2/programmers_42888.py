# 2022-03-11 (금)
# 프로그래머스 level2
# 오픈채팅방

# 처음에 문자열로 처리를 했는데, replace 때문에 시간초과도 나고 틀리기도 해서 
# 딕셔너리와 리스트를 활용해서 해보니까 성공했따!
def solution(record):
    answer = []
    
    id_list = []
    action_list = []

    uid_dict = dict()
    uid_dict = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for i in record:
        arr = i.split(' ')
        uState = arr[0]
        uPk = arr[1]
        
        if uState == 'Enter':
            uId = arr[2]
            uid_dict[uPk] = uId
            id_list.append(uPk)
            action_list.append(uState)
        elif uState == 'Change':
            uId = arr[2]
            uid_dict[uPk] = uId
        else :
            id_list.append(uPk)
            action_list.append(uState)
    
    for i in range(len(id_list)):
        tempId = id_list[i]
        tempAction = action_list[i]
        text = uid_dict[tempId] + uid_dict[tempAction]
        answer.append(text)
    
    return answer


print( solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]) )