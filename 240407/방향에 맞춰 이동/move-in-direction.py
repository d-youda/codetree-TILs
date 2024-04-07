n = int(input()) #움직일 값 받기

#dx, dy 설정하기
dx_dy = {
    'W': [-1, 0],
    'S': [0, -1],
    'E': [1, 0],
    'N': [0, 1]
}
x = 0
y = 0
#n만큼 for문 돌면서 입력 받아서 위치 이동하기
for i in range(n):
    t_position = list(input(""))
    x = x + int(t_position[2]) * dx_dy[t_position[0]][0]

    y = y + int(t_position[2]) * dx_dy[t_position[0]][1]

print(x, y)