# 2022-03-10 (목)
# 프로그래머스 level1
# [1차] 다트 게임

def solution(dartResult):
    answer = 0

    dartResult_list = list(dartResult.replace("10","a"))
    
    # 여기부터 조금 오류, 0~9 까지인 줄 알았으나
    # 0~10 까지였음 저렇게 고정적으로 위치를 설정 할 수 없다..
    
    # 내가 해결한 방법...
    # 10을 a로 바꿔줘서 고정적으로 위치를 사용..ㅎㅎ..

    if dartResult_list[2] != '*' and dartResult_list[2] != '#' :
        dartResult_list.insert(2, ' ')

    if dartResult_list[5] != '*' and dartResult_list[5] != '#' :
        dartResult_list.insert(5, ' ')

    if len(dartResult_list) != 9 :
        dartResult_list.insert(8, ' ')

    score_list = []
    for i in range(3) :
        score = dartResult_list[i*3]
        score = 10 if score == 'a' else int(score)
        bonus = dartResult_list[i*3+1]
        option = dartResult_list[i*3+2]

        # 보너스 처리
        if bonus == 'S':
            score = score
        elif bonus == 'D':
            score = score ** 2
        else :
            score = score ** 3

        # 옵션 처리
        if option == '*':
            score = score * 2
            if i > 0 :
                score_list[i-1] = score_list[i-1] * 2
        elif option == '#':
            score = score * -1
        else :
            score = score

        score_list.append(score)
    
    for i in score_list :
        answer += int(i)

    return answer


print( solution('1S2D*3T') )
print( solution('1D2S#10S') )
print( solution('1D2S0T') )
print( solution('1S*2T*3S') )
print( solution('1D#2S*3S') )
print( solution('1T2D3D#') )
print( solution('1D2S3T*') )
