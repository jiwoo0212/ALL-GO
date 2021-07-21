dx = [1, -1, 1, -1, -2, -2, 2, 2]
dy = [-2, -2, 2, 2, 1, -1, 1, -1]

start = input()
x = int(start[1])-1
y = (ord(start[0])-97)

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx<0 or nx>7 or ny<0 or ny>7:
        continue
    else:
        cnt += 1
print(cnt)