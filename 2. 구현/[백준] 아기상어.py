from collections import deque
n = int(input())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    try:
        start = (i, row.index(9))
        print(start)
    except:
        pass
    grid.append(row)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, level):
    cnt = 0
    queue = deque([(x,y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>(n-1) or ny<0 or ny>(n-1):
                continue
            if visited[nx][ny]==True:
                continue
            cnt += 1
            if grid[nx][ny]!= 0 and grid[nx][ny] < level :
                return (nx, ny), cnt
            queue.append((nx,ny))
            # print('nx, ny', nx, ny)
            visited[nx][ny] = True
    return False, cnt


cnt = 0
x, y = start
level = 2
level_up = 0

while True:
    visited =[[False for _ in range(n)] for _ in range(n)]
    xy, step_cnt = bfs(x, y, level)
    print(xy, step_cnt)
    if xy != False: 
        x, y = xy
        grid[x][y] = 0
        level_up += 1
    else: # 엄마 상어 불러야됌 전단계의 cnt가 최종 cnt. 따라서 아무것도 더해주지 않는다
        break

    if level_up == level:
        level += 1

print(cnt)
