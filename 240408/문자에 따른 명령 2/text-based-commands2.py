dx,dy = [1, 0, -1, 0], [0, -1, 0, 1]

x,y = 0,0

position = list(input())
dir = 3 #북쪽 바라보고 시작하기 때문
for index in position:
    if index=="F":
        x,y = x+dx[dir], y+dy[dir]
    elif index=="R":
        dir = (dir+1)%4
    elif index == "L":
        dir = (dir-1)%4

print(x,y)