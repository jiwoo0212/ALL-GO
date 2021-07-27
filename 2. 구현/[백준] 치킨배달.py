n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 2인 좌표 리스트
lst_1 = []
lst_2 = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            lst_2.append((i,j))
        elif grid[i][j] == 1:
            lst_1.append((i, j))

from itertools import combinations

comb = list(combinations(lst_2, m))

# visited = [[False for _ in range(n)] for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

from collections import deque

def bfs(x, y, notlst):
    visited[x][y] = True
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>(n-1) or ny<0 or ny>(n-1):
                continue
            if visited[nx][ny] == False:
                if grid[nx][ny] == 2 and (nx, ny) in notlst:
                        return (nx, ny)
                visited[nx][ny] = True
                queue.append((nx, ny))
dis_lst = []
for g in comb: # 치킨집 조합
    all_distance = 0
    for i in lst_1: # 각 치킨집 조합의 치킨거리총합 계산
        visited = [[False for _ in range(n)] for _ in range(n)]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        x, y = i
        a, b = bfs(x, y, g) # 가장 가까운 치킨집 좌표
        all_distance += abs(x-a)+abs(y-b)
    dis_lst.append(all_distance)

print(min(dis_lst))


