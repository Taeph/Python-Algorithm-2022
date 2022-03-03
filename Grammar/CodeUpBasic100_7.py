# CodeUp 6092 ~ 6098

# 6098
home = [[0 for i in range(10)] for i in range(10)]

for i in range(10):
    temp = input().split()    
    for j in range(10):
        home[i][j] = int(temp[j])
#print(home)

x = 1
y = 1
for i in range(30) :
    # print(x,y)
    if home[x][y] == 2 :
        home[x][y] = 9
        break
    elif x == 8 and y == 8:
        home[x][y] = 9
        break
    else :
        home[x][y] = 9
        # 오른쪽으로 갈 수 있으면 오른쪽으로 이동
        if home[x][y+1] == 0 :
            y += 1
        # 오른쪽으로 못가면 아래로 이동
        elif home[x][y+1] == 1 :
            x += 1
        # 아래로 갈 수 있으면 아래로 이동
        elif home[x+1][y] == 0 :
            x += 1
        # 아래로 못가면 오른쪽으로 이동
        elif home[x+1][y] == 1 :
            y += 1

    # for i in range(10):
    #     for j in range(10):
    #         print(home[i][j], end=' ')
    #     print()
    
for i in range(10):
    for j in range(10):
        print(home[i][j], end=' ')
    print()


# 6097
w,h = input().split()
w = int(w)
h = int(h)
boards = [[0 for i in range(h)] for i in range(w)]

n = int(input())
for i in range(n):
    l,d,x,y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)-1
    y = int(y)-1
    if d == 0:
        for i in range(l):
            boards[x][y+i] = 1
    else:
        for j in range(l):
            boards[x+j][y] = 1

for i in range(w):
    for j in range(h):
        print(boards[i][j], end=' ')
    print()


# 6096
p = [[0 for j in range(19)] for i in range(19)]
for i in range(19):
    a = input().split()
    for j in range(19):
        p[i][j] = int(a[j])

n = int(input())
for i in range(n):
    x,y = input().split()
    x = int(x)-1
    y = int(y)-1

    for j in range(19):
        if p[x][j] == 1:
            p[x][j] = 0
        else:
            p[x][j] = 1

        if p[j][y] == 1:
            p[j][y] = 0
        else:
            p[j][y] = 1    

    for i in range(19):
        for j in range(19):
            print(p[i][j], end=' ')
        print()


# 6095
d = [[0 for j in range(19)] for i in range(19)] # List Comprehension
n = int(input())
for i in range(n):
    a = input().split()
    x = int(a[0])-1
    y = int(a[1])-1
    d[x][y] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=' ')
    print()

# 6094
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

min_v = a[0]
for i in range(n):
    min_v = (min_v if (min_v < a[i]) else a[i])

print(min_v)

# 6093
n = int(input())
a = input().split()

for i in range(1,n+1):
    print(a[n-i], end=' ')


# 6092
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')