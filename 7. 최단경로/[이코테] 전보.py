import heapq

n, m, s = map(int, input().split())

graph = [[] for _ in range(n+1)]

inf = int(1e9)

distance = [inf for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dst(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dst(s)

cnt = 0
max_time = -1
for i in range(1, n+1):
    if i != s:
        if distance[i] != inf:
            cnt += 1
            if max_time < distance[i]:
                max_time = distance[i]

print(cnt, max_time)