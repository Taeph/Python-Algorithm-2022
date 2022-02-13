# CodeUp 6058 ~ 
# 6063 ~ 6070 >> 조건문(if)
# 6071 ~ 6076 >> 반복문(for)

# 6076
n = int(input())
for i in range(n+1) : 
    print(i)
# range(n) >> 0, 1, ~ n-2, n-1 수열
# range(s, e) >> s, s+1, ~ e-2, e-1 수열
# range(s, e, k) >> s, s+k, ~ e-2k, e-k 수열

# 6075
n = int(input())
a = 0
while a<=n :
    print(a)
    a += 1 

# 6074
c = ord(input())
t = ord('a')
while t<=c :
    print(chr(t), end=' ') # print(..., end='') 같이 작성하면 출력값 이후 ''을 출려한다
    t += 1

# 6073
n = int(input())
while n != 0 :
    n = n-1
    print(n)

# 6072
n = int(input())
while n != 0 :
    print(n)
    n = n-1

# 6071
n = 1
while n != 0 :
    n = int(input())
    if n != 0 :
        print(n)

# 6070
m = int(input())
if m==12 or m==1 or m==2 :
    print('winter')
elif m//3 == 1 :
    print('spring')
elif 6<=m and m<=8 :
    print('summer')
else :
    print('fall')

# 6069
c = input()
if c=='A' :
    print('best!!!')
elif c=='B' :
    print('good!!')
elif c=='C' :
    print('run!')
elif c=='D' :
    print('slowly~')
else :
    print('what?')

# 6068
n = int(input())
if n>=90 :
    print('A')
elif n>=70 and n<90 :
    print('B')
elif n>=40 and n<70 :
    print('C')
else :
    print('D')

# 6067
n = int(input())
if n%2==0 and n<0 :
    print('A')
elif n%2!=0 and n<0 :
    print('B')
elif n%2==0 and n>0 :
    print('C')
else :
    print('D')

# 6066
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0 :
    print('even')
else :
    print('odd')
if b%2 == 0 :
    print('even')
else :
    print('odd')
if c%2 == 0 :
    print('even')
else :
    print('odd')

# 6065
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0 :
    print(a)
if b%2 == 0 :
    print(b)
if c%2 == 0 :
    print(c)

# 6064
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = (a if(a<=b) else b) # a 와 b 중 작은값
f = (d if(d<=c) else c) # (a 와 b 중 작은값) 과 c 중 작은값
print(f)

# 6063
a, b = input().split()
a = int(a)
b = int(b)
c = (a if (a>=b) else b) # 3항연산
print(c)
# 3항연산
# Python   >> x if C else y  >> C가 true 이면 x, False 이면 y
# 다른언어 >> C ? x : y      >> C가 true 이면 x, False 이면 y 

# 6062
a, b = input().split()
c = int(a)
d = int(b)
print(c^d)

# 6061
a, b = input().split()
c = int(a)
d = int(b)
print(c|d)

# 6060
a, b = input().split()
c = int(a)
d = int(b)
print(c&d)

# 6059
a = int(input())
print(~a)
# 기본(비트단위) 연산자 : not(~), and(&), or(|), xor(^), left shift(<<), right shift(>>)
# 비트단위 연산은 연산 속도가 빠르다