# 2022-03-11 (금)
# 프로그래머스 level1
# 음양 더하기

def solution(absolutes, signs):
    answer = 0

    # 요녀석은 생각보다 간단..매우
    for i in range(len(absolutes)):        
        sign = 1 if signs[i] else -1
        answer += absolutes[i] * sign
        

    return answer


print( solution([4,7,12], [True,False,True]) )
print( solution([1,2,3], [False,False,True]) )