n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

val = -1
for i in range(n):
    if val < min(grid[i]):
        val = min(grid[i])
print(val)