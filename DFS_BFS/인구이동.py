# 인구이동 bfs
from collections import deque
from collections import defaultdict

n, l, r = map(int, input().split())
grid = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    grid.append(list(map(int, input().split())))

def bfs(x,y, start):
    visited[x][y] = start
    dic1[start] += 1
    dic2[start] += grid[x][y]
    queue = deque([(x,y)])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>(n-1) or ny<0 or ny>(n-1):
                continue
            # 값의 차가 범위 밖이라면
            elif abs(grid[x][y] - grid[nx][ny]) < l or abs(grid[x][y] - grid[nx][ny]) > r:
                continue
            else:
                if visited[nx][ny] == False:
                    visited[nx][ny] = start
                    queue.append((nx,ny))
                    dic1[start] += 1
                    dic2[start] += grid[nx][ny]

ans = 0
while True:
    visited = [[False for _ in range(n)] for _ in range(n)]
    dic = {}
    dic1 = defaultdict(int)
    dic2 = defaultdict(int)
    c = 0
    for j in range(n):
        for k in range(n):
            c -= 1
            if visited[j][k] == False:
                bfs(j, k, c)
    # print('dic', dic)
    # print('visited',visited)
    # 평균계산
    stop_cnt = 0
    for i in dic1:
        if dic1[i] == 1:
            stop_cnt += 1
        else:
            dic[i] = int(dic2[i]/dic1[i])
    if stop_cnt == n**2:
        break
    # print('dic', dic)
    # 평균으로 바꾸기
    for j in range(n):
        for k in range(n):
            if visited[j][k] in dic:
                grid[j][k] = dic[visited[j][k]]
    # print(grid)
    ans += 1

print(ans)