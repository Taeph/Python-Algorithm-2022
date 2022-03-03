# CodeUp 6077 ~ 6091

# 6091
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
i = 1
while not (i%a==0 and i%b==0 and i%c==0) :
    i += 1
print(i)
# 최소공배수 알고리즘
# 최대공약수 알고리즘 
# 공부하기

# 6090
a, m, d, n = input().split()
a = int(a)
m = int(m)
d = int(d)
n = int(n)-1
while n != 0 :
    a = a*m+d
    n -= 1
print(a)


# 6089
a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)-1
while n != 0 :
    a = a*r
    n -= 1
print(a)


# 6088
a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)-1
while n != 0 :
    a += d
    n -= 1
print(a)    


# 6087
n = int(input())
i = 1
while i <= n :
    if i%3 != 0 :
        print(i, end=' ')
    i += 1


# 6086
n = int(input())
total = 0
for i in range(1, n+1) :
    total += i
    if total >= n :
        break
print(total)
    

# 6085
w, h, b = input().split()
w = int(w)
h = int(h)
b = int(b)
result = float(w * h * b / 8 / 1024 / 1024)
print(format(result, '.2f'),'MB')

# 6084
h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)
result = float(h * b * c * s / 8 / 1024 / 1024)
print(format(result, '.1f'),'MB',sep=' ')


# 6083
r, g, b = input().split()
r = int(r)
g = int(g)
b = int(b)
total = 0
for i in range(0, r) :
    for j in range(0, g) :
        for k in range(0, b) :
            print(i,j,k, sep=' ')
            total += 1
print(total)


# 6082
n = int(input())
for i in range (1, n+1) :
    if i%10==3 or i%10==6 or i%10==9 :
        print('X', end=' ')
    else :
        print(i, end=' ')


# 6081
h = input()
a = int(h, 16)
for i in range(1, 16) :
    print('%X'%a,'*','%X'%i,'=','%X'%int(a*i), sep='') # sep='값' print에서 ,로 연결한 값들을 '값'으로 붙인다


# 6080
a, b = input().split()
a = int(a)
b = int(b)
for i in range(1, a+1) :
    for j in range(1, b+1) :
        print(i, j)


# 6079
n = int(input())
total = 0
for i in range(0, n+1) :
    total += i
    if total >= n :
        print(i)
        break
    

# 6078
c = ''
while c != 'q' :
    c = input()
    print(c)


# 6077
n = int(input())
total = 0
for i in range (1, n+1) :
    if i%2 == 0 :
        total += i
print(total)