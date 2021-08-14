n = int(input())

d = list(map(int, input().split()))

d[1] = max(d[0], d[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+d[i])

print(d[n-1])

