N = int(input())

for x in range(2, 102):
    if sum(list(range(1, x))) >= N:
        print(list(range(1, x))[-1])
        break
