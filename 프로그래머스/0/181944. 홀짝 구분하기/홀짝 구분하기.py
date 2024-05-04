while True:
    n = int(input())
    if 0 < n < 1001:
        break
    else:
        continue
if n%2 == 0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')