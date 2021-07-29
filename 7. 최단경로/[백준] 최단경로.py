# 이코테 코드 참고

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
s = int(input())

# 노드의 연결들
graph = [[] for i in range(n+1)]
# 확정된 최단거리 저장
distance = [INF]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    # 해당노드와 (연결노드, 비용)
    graph[a].append((b, c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s)) # 우선순위큐로 만들고 (비용, 노드번호) append
    distance[s] = 0
    while q:
        dist, now = heapq.heappop(q) # 가장 비용이 적은 노드가 뽑힌다
        if distance[now] < dist:
            continue
        for i in graph[now]: # now(현재노드)와 연결된 노드들을 순서대로 본다
            cost = dist + i[1]
            if cost < distance[i[0]]: # 만약 i를 거쳐서 가는 비용이 더 적다면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # (새로 갱신된 비용, 노드번호)

dijkstra(s)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])