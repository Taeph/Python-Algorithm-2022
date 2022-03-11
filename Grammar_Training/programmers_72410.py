# 프로그래머스 level1
# 신규 아이디 추천

# 다른 사람들 풀이 봤는데...
# python 데이터 형과, 내부 함수에 좀 더 익숙해 지면 좋을 것 같다..

def solution(new_id):
    answer = ''
    
    # step1 
    step1 = [i for i in new_id.lower()]
    # print(step1)
    
    # step2 
    # > 알파뱃소문자(97~122), 숫자(48~57), 빼기(45), 밑줄(95), 마침표(46) 문자열 배열을 만들어 둔다
    # 나는 이런식으로 사용가능 문자를 배열에 담아서 처리했는데, isalpha(), isdigit() 라는 함수가 있는 것 같다
    strArr = ['-','_','.']
    for i in range(48,58):
        strArr.append(chr(i))
    for i in range(97,123):
        strArr.append(chr(i))
    # 아이디에서 가능한 문자열 배열에 있는 것만 골라낸다
    step2 = [i for i in step1 if i in strArr]
    # print(step2)    
    
    # step3
    # > 마침표가 연속해서 나오면 제거 - 다른 문제 풀다가 알게된 replace를 사용해서 나아졌다 (원래는 idx, idx-1 이런식으로 했음...;)
    step3 = ''.join(i for i in step2)
    # print(step3)
    while True :
        if step3 == step3.replace('..','.'):
            break
        else :
            step3 = step3.replace('..','.')
    # print(step3)
    step3 = list(step3)
    # print(step3)

    # step4
    # > 마침표가 맨앞, 맨뒤에 있으면 제거
    if len(step3) > 0 and step3[0] == '.':
        step3 = step3[1:]

    if len(step3) > 0 and step3[-1] == '.':
        step3 = step3[:-1]
    step4 = step3
    # print(step4)

    # step5
    # > 빈 문자열 이라면, "a" 대입
    if len(step4) == 0:
        step4.append("a")
    step5 = step4
    # print(step5)

    # step6
    # > 길이가 16자 이상이면, 앞에서부터 15자리로 자르고, 마지막이 마침표이면 제거
    step6 = step5[0:15]
    if len(step6) == 15 and step6[14] == '.':
        step6 = step6[:-1]
    # print(step6)

    # step7
    # > 길이가 3이하라면, 최종문자를 3이 될때까지 붙여준다
    step7 = step6
    while len(step7) < 3:
        step7.append(step7[-1])
    # print(step7)

    answer = ''.join(i for i in step7)

    return answer

new_id1 = "...!@BaT#*..y.abcdefghijklm"
new_id2 = "z-+.^."
new_id3 = "=.="
new_id4 = "123_.def"
new_id5 = "abcdefghijklmn.p"

print( solution(new_id1) )
print( solution(new_id2) )
print( solution(new_id3) )
print( solution(new_id4) )
print( solution(new_id5) )
