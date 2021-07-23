# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
grid = []
for i in range(n):
    grid.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if grid[x][y] == 0:
        grid[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > (n-1) or ny < 0 or ny > (m-1):
                continue
            elif grid[nx][ny] == 1:
                continue

            else:
                dfs(nx, ny)
        return True

    else:
        return False

cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt += 1
print(cnt)