from itertools import combinations

n, m = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

lst_1 = [] # 1인 좌표 리스트
lst_2 = [] # 2인 좌표 리스트
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            lst_2.append((i,j))
        elif grid[i][j] == 1:
            lst_1.append((i, j))

comb = list(combinations(lst_2, m))

dis_lst = []
for g in comb: # 치킨집 조합
    all_distance = 0
    for h in lst_1:
        dis = []
        x, y = h
        for ch in g:
            a, b = ch
            dis.append(abs(x-a)+abs(y-b))
        all_distance += min(dis)
    dis_lst.append(all_distance)

print(min(dis_lst))
