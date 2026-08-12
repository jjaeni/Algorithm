A, B = map(int, input().split())
total = 0

for num in range(A, B+1):
    if num%2 != 0:
        continue
    total += num
print(total)