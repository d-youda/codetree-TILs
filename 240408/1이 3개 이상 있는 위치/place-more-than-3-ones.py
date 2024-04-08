n = int(input())  #nxn 크기의 격자
# input_arr = input()
array = []
for _ in range(n):
    row = input().split()
    row = [int(num) for num in row]
    array.append(row)
# print(array)
def in_range(x,y):
    return (x>=0 and x<n) and (y>=0 and y<n) # 0<= x,= n (y도 이와 동일)

ddx, ddy = [1, 0, -1, 0], [0, 1, 0, -1]
result = 0 #인접한 칸에 숫자 1이 개 이상 적힌 서로 다른 칸 수
for i in range(n):
    for j in range(n):
        near = 0 #인접한 칸의 1 포함 갯수
        for dx, dy in zip(ddx, ddy):
            if((in_range(i+dx,j+dy) and (array[i+dx][j+dy]) == 1)):
                near += 1
        if near >= 3:
            result += 1
print(result)