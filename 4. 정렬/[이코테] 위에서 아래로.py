n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

for i in sorted(lst, reverse=True):
    print(i, end=' ')