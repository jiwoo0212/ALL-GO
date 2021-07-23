# 최단거리 미로
'''
이코테 풀이접근방식과 달리 다익스트라이용해서 풀었음
'''
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
grid = []
for i in range(n):
    grid.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(m)] for _ in range(n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        if (x, y) == (n-1, m-1):
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>(n-1) or ny<0 or ny>(m-1): # 지도밖이라면
                continue
            elif grid[nx][ny] == 0: # 벽이라면
                continue
            else:
                if visited[nx][ny] == True: # 처음 방문하는 것이 아니라면
                    if grid[x][y]+1 < grid[nx][ny]: 
                        grid[nx][ny] = grid[x][y]+1

                else: # 처음 방문이라면
                    grid[nx][ny] = grid[x][y]+1
                queue.append((nx, ny))
                visited[nx][ny] = True
bfs(0,0)
print(grid[n-1][m-1])