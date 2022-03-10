# 2022-03-10 (목)
# 프로그래머스 level1
# 숫자 문자열과 영단어

def solution(s):
    answer = 0

    num_to_word = dict()
    # 딕셔너리 이렇게 초기화 하자
    num_to_word = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    # num_to_word['zero']  = '0'
    # num_to_word['one']   = '1'
    # num_to_word['two']   = '2'
    # num_to_word['three'] = '3' 
    # num_to_word['four']  = '4'
    # num_to_word['five']  = '5'
    # num_to_word['six']   = '6'
    # num_to_word['seven'] = '7'
    # num_to_word['eight'] = '8'
    # num_to_word['nine']  = '9'
    # print(num_to_word)

    i = 0
    temp = []
    word = ''
    
    for i in s:    
        # 숫자범위 안에 들어있으면 temp 넣고 다음 진행
        if ord(i) > 47 and ord(i) < 58 :
            temp.append(i)
        # 숫자범위 안에 없는 경우, 하나씩 붙여서 문자를 만들어서 비교한다
        else :
            word += i
            if word in num_to_word:
                # print(num_to_word[word])
                temp.append(num_to_word[word])
                word = ''

    # print(temp)  
    answer = int(''.join(i for i in temp))
    
    return answer

# replace 를 활용한 사람들이 많았음..
# 파이썬 기본 함수들을 좀 더 익힐 필요가 있다

s1 = "one4seveneight"
s2 = "23four5six7"
s3 = "2three45sixseven"
s4 = "123"
print( solution(s1) )
print( solution(s2) )
print( solution(s3) )
print( solution(s4) )
