N = int(input())
lst = list(map(int, input().split()))
result = []

for x in lst:
    if x % 2 == 0:
        result.append(x)

result.reverse()
print(*result)