N = int(input())
cnt = 0

for x in range(1, N+1):
    if x%2==0 or x%3==0 or x%5==0:
        continue
    cnt +=1

print(cnt)