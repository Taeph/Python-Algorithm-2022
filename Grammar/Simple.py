# 코딩테스트 준비

python 기준으로 연산횟수가 5억번 5초 정도 걸림 (c언어의 경우 1초)

코딩테스트는 보통 시간제한이 1~5초 정도 

문제에서 가장 먼저 확인해야 하는 것은 시간제한
N의 범위에 따라 그에 맞는 시간복잡도를 고려하여 알고리즘 설계를 해야한다

지문 읽기 및 컴퓨터적 사고
요구사항(복잡도) 분석
문제 해결을 위한 아이디어 찾기
소스코드 설계 및 코딩

일반적으로 핵심 아이디어를 캐치하면, 구현자체는 어렵지 않도록 만든다.

import time
start_time = time.tiem()
end_time = time.time()
print("time :", end_time - start_time)


# 파이썬 기초문법 - 자료형

# 정수형
a = 1000
print(a)

a = -7
print(a)

a = 0
print(a)

# 실수형
b = 157.93
print(b)

b = -1873.2
print(b)

b = 5.
print(b)    # 5.0

b = .12
print(b)    # 0.12

# 지수표현(e)
c = 1e9
print(c)    # 1,000,000,000

c = 72.25e1
print(c)    # 722.5

c = 1005e-3
print(c)    # 1.005

d = 0.3 + 0.6
print(d)    # 0.899999999999

if d == 0.9 :
    print(True)
else :
    print(False)

실수의 연산에서 원하는 값을 얻을 수 없다
round() 함수를 활용하여, 정확도를 높혀야 한다
round(125.235, 2) = 125.23

# 사칙연산
e = 7
f = 3
print(7 / 3)    # 2.3333333333335 (나눈값)
print(7 % 3)    # 1 (나머지)
print(7 // 3)   # 2 (몫)
print(7 ** 3)   # 343 (세제곱)
print(7 ** 0.5) # 2.6457513110645907 (제곱근)

# 리스트
list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = []
list_c = list()
list_d = [0] * 5

앞에서 indexing 할 때는 0 부터 시작
print(list_a[0])    # 1
print(list_d)       # [0,0,0,0,0]

뒤에서 indexing 할 때는 -1 부터 시작
print(list_a[-1])   # 10
print(list_a[-3])   # 8

연속적인 위치를 갖는 원소들 가져올때 slicing을 사용
slicing 할때, 끝 index는 +1 을 해서 사용한다
print(list_a[1:4])  # [2,3,4]

리스트 컴프리헨션
리스트를 초기화하는 방법 중 하나
대괄호 안에 조건문과 반복문을 사용하여 리스트를 초기화
list_e = [i for i in range(10)]
print(list_e)   # [0,1,2,3,4,5,6,7,8,9]
list_f = [i for i in range(20) if i % 2 == 1]
print(list_f)   # [1,3,5,7,9,11,13,15,17,19]
list_g = [i * i for i in range(10)]
print(list_g)   # [1,4,9,16,25,36,49,64,81]

특히 2차원 배열을 초기화 할때, 편리하다
list_h = [[0] * m for _ in range(n)]    # 좋은 방법 - 원하는대로 m * n 배열 생성
list_i = [[0] * m] * n                  # 잘못된 방법 - 이렇게 하면 모두 같은 객체로 인식한다 

반복문에 _ 가 자주 사용된다
특정 i 값을 계속 더해주는 경우, i를 명시한다
result = 0
for i in range(1, 10):
    result += i
print(result)

단순히 반복하고 싶을때, _ 를 사용한다
for _ in range(5):
    print('Hello World')

리스트에서 자주 사용되는 함수
arr = [1, 2, 3]
arr.append(4)               # 하나의 원소 삽입 - O(1)
print(arr)                  # [1,2,3,4]

arr.sort(reverse = True)    # 내림차순 정렬 - O(NlogN)
print(arr)                  # [4,3,2,1]

arr.sort()                  # 오름차순 정렬 - O(NlogN)
print(arr)                  # [1,2,3,4]

arr.reverse()               # 리스트 원소 순서 뒤집기 - O(N)
print(arr)                  # [4,3,2,1]

arr.insert(3, 2)            # 특정 index에 값 넣기 - O(N)
print(arr)                  # [4,3,2,2,1]

print(arr.count(2))         # 특정 값 갯수 세기 - O(N) 

arr.remove(2)               # 특정 값 하나만 제거 - O(N)
print(arr)                  # [4,3,2,1]

특정 값들을 리스트에서 제거
remove_set = [3,2]
result = [i for i in arr if i not in remove_set]    # arr리스트를 돌면서, remove_set에 없으면 result 리스트에 추가
print(result)   # [4,1]


# 문자열
"" or ''
print('Hi')
print("Hello")

a = "KangTaeJun"
print(a[0:4])  # "Kang"
print(a*3)     # "KangTaeJunKangTaeJunKangTaeJun"

변경이 불가능 하다
a[5] = "J"     # 에러발생

# 튜플
튜플은 한번 값이 설정되면, 변경이 불가능 하다
(리스트는 가능했다)
리스트를 사용할 때 보다 작은 메모리를 사용한다

tuple_a = (1,2,3,4,5,6,7,8)
print(tuple_a[3])   # 4
print(tuple_a[3:5]) # 4,5,6

변경이 불가능 하다
tuple_a[0] = 10     # 에러발생

서로 다른 성질의 데이터를 묶어서 관리해야할 때 많이 사용된다

# 딕셔너리
(Key,Value) 를 쌍으로 가지는 자료형이다
리스트, 튜플 과 같이 순차적으로 저장되지 않는다
내부적으로 Hash Table을 사용하기 때문에 상수시간의 연산속도

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['오랜지'] = 'Orange'
print(data)     # {'사과': 'Apple', '바나나': 'Banana', '오랜지': 'Orange'}

if '사과' in data :
    print('사과가 존재한다')

상수시간이 걸리기 때문에, 데이터를 저장하고 관리하는데 리스트보다 훨씬 효율적이다
키 데이터만 뽑아서 리스트로 사용하고 싶으면 keys()
값 데이터만 뽑아서 리스트로 사용하고 싶으면 values()
print(data.keys())      # dict_keys(['사과', '바나나', '오랜지']) 
print(data.values())    # dict_values(['Apple', 'Banana', 'Orange'])

key_list = list(data.keys()) 
이런식으로 리스트로 변경해서 사용한다

# 집합자료형
중복을 허용하지 않고, 순서가 없다
집합은 리스트나 문자열로 초기화 할 수 있다 
set() 함수 사용

data = set([1,1,2,2,3,3])
print(data)     # {1,2,3}

data = {1,1,2,3,4,4}
print(data)     # {1,2,3,4}

합집합, 교집합, 차집합 연산을 사용할 수 있다
합집합 = a | b 
교집합 = a & b
차집합 = a - b

data.add(val)
data.update([val,val,val])
data.remove(val)

리스트, 튜플은 순서가 있어서 indexing 으로 접근
사전자료형, 집합자료형은 연산이 상수시간이 걸린다 (키값으로는 변하지않는 값 사용해야함)
