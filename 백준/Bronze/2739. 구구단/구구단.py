while True:
    N = int(input())
    if 0 < N < 10:
        break
    else:
        continue

for i in range(9):
    print(f'{N} * {i+1} = {N*(i+1)}')