# CodeUp 6032 ~ 6058

# 6058
a, b = input().split()
c = bool(int(a))
d = bool(int(b)) 
print( (not c) and (not d) )

# 6057
a, b = input().split()
c = bool(int(a))
d = bool(int(b)) 
print( ( (not d) and (not c) ) or (c and d) )

# 6056
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print( (c and (not d)) or ( (not c) and d ) ) # xor > 다른 경우에만 true 

# 6055
a, b = input().split()
print(bool(int(a)) or bool(int(b))) # or == || > 하나라도 true 이면 true

# 6054
a, b = input().split()
print(bool(int(a)) and bool(int(b))) # and == && > 둘다 true 이면 true

# 6053
n = int(input())
print(not bool(n)) # not == !

# 6052
n = int(input())
print(bool(n)) # bool(n) n 값이 0이면 False, 그 외엔 True

# 6051
a, b= input().split()
print(int(a) != int(b))

# 6050
a, b= input().split()
print(int(a) <= int(b))

# 6049
a, b= input().split()
print(int(a) == int(b))

# 6048
a, b= input().split()
print(int(a) < int(b))

# 6047
a, b = input().split()
a = int(a)
b = int(b)
print(a<<b)

# 6046
a = int(input())
print(a<<1) 
# 왼쪽 비트시프트 (<<) 값이 2배
# 오른쪽 비트시프트 (>>) 값이 1/2배
# 실수는 불가능하다

# 6045
a, b, c = input().split()
d = int(a)+int(b)+int(c)
print(d, format(d/3, '.2f'))

# 6044
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, '.2f'))

# 6043
f1, f2 = input().split()
f3 = float(f1) / float(f2)
print(format(f3, ".3f"))

# 6042
a = float(input())
print(format(a, ".2f")) # a 값을 소수 2자리까지 보여줌 (3자리에서 반올림)
# format(값, ".보여질자리수f")

# 6041
n1, n2 = input().split()
print(int(n1)%int(n2)) # n1 에서 n2 를 나눈 나머지

# 6040
n1, n2 = input().split()
print(int(n1)//int(n2)) # n1 에서 n2 를 나눈 몫

# 6039
f1, f2 = input().split()
f3 = float(f1)**float(f2)
print(f3)

# 6038
a, b = input().split()
c = int(a) ** int(b) # a 의 b 제곱
print(c)

# 6037
n = input()
s = input()
print(int(n)*s)

# 6036
w, n = input().split()
print(w*int(n))

# 6035
f1, f2 = input().split()
print(float(f1) * float(f2))

# 6034
a, b = input().split()
print(int(a)-int(b))

# 6033
c = input()
print(chr(ord(c)+1))

# 6032
n = int(input())
print(-n)