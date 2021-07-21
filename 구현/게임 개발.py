n, m = map(int, input().split())
x, y, pos = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited[x][y] = True

while True:
    for i in range(4):
        flag = False
        if pos == 0:
            pos = 3
        else:
            pos -= 1

        nx = x + dx[pos]
        ny = y + dy[pos]

        # 움직일 수 있는 조건이라면
        if grid[nx][ny] != 1 and visited[nx][ny] != True:
            visited[nx][ny] = True
            x = nx
            y = ny
            cnt += 1
            flag = True  # 4번 돌았지만 위치를 옮긴 상황을 기록
            break
    if i == 3:
        if flag == True:
            continue
        elif grid[x - dx[pos]][y - dy[pos]] == 1:
            break
        else:
            x -= dx[pos]
            y -= dy[pos]
print(cnt)