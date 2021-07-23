n, m, k = map(int, input().split())
lst= list(map(int, input().split()))

lst.sort(reverse=True)

first = lst[0]
second = lst[1]

# 가장큰수는 전체길이를 k+1 로 나눈 몫*k + 나머지 만큼, 두번째큰수는 전체길이를 k+1 로 나눈 몫만큼
result = first*((m//(k+1))*k + m%(k+1)) + second*(m//(k+1))
print(result)