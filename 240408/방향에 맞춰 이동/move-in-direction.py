n = int(input()) #움직일 값 받기

#dx, dy 설정하기
dx,dy = [1, 0, -1, 0], [0, -1, 0, 1]
x = 0
y = 0
#n만큼 for문 돌면서 입력 받아서 위치 이동하기
for i in range(n):
    t_position = list(input().split(" "))
    if t_position[0]=='E':
        x = x+ dx[0]*int(t_position[1])
        y = y+ dy[0]*int(t_position[1])
    elif t_position[0]=='N':
        x = x+ dx[3]*int(t_position[1])
        y = y+ dy[3]*int(t_position[1])
    elif t_position[0]=='W':
        x = x+ dx[2]*int(t_position[1])
        y = y+ dy[2]*int(t_position[1])
    elif t_position[0]=='S':
        x = x+ dx[1]*int(t_position[1])
        y = y+ dy[1]*int(t_position[1])
print(x,y)