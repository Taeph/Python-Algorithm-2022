# 프로그래머스 level1
# 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = []

    # 내 번호중 당첨 안 된 숫자만 찾아냄
    temp = [i for i in lottos if i not in win_nums]
    # print(temp)

    # 당첨 안 된 숫자의 개수
    left_nums = len(temp)
    # print(left_nums)

    # 0의 개수
    cnt = temp.count(0)
    # print(cnt)

    # 최대순위는 0이 모두 맞았다, 최소순위는 0이 모두 틀렸다 
    max_rate = (left_nums-cnt+1) if (left_nums-cnt+1) <= 6 else 6
    min_rate = (left_nums)+1 if (left_nums)+1 <= 6 else 6

    answer.append(max_rate)
    answer.append(min_rate)

    return answer


# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]

# lottos = [0, 0, 0, 0, 0, 0]
# win_nums = [38, 19, 20, 40, 15, 25]

lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]

answer = solution(lottos, win_nums)
print(answer)