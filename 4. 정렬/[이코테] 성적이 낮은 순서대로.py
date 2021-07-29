n = int(input())
dic = {}
for _ in range(n):
    name, score = input().split()
    dic[name] = int(score)
for i in sorted(dic, key= lambda x: dic[x]):
    print(i, end=' ')