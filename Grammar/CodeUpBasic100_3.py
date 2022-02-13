# CodeUp 6025 ~ 6031

# 6031
c = int(input())
print(chr(c)) # 정수값을 유니코드 문자로 변환

# char -> int 는 ord
# int -> char 는 chr

# 6030
b = ord(input()) # 10진수 유니코드 값으로 변환 ord = (ordinal position)
print(b)

# 6029
a = input() 
n = int(a, 16) # 16진수로 변환
print('%o'% n) # 8진수로 변환

# 6028
a = input()
n = int(a)
print('%X'% n) # %X 는 16진수 (대문자)

# 6027
a = input()
n = int(a)
print('%x'% n) # %x 는 16진수 (소문자)
print('%o'% n) # %o 는 8진수

# 6026
f1 = input()
f2 = input()
f3 = float(f1) + float(f2)
print(f3)

# 6025
n1, n2 = input().split()
n3 = int(n1) + int(n2)
print(n3)
