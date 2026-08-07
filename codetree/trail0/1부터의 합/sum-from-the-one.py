N = int(input())
num = 0

for x in range(1, 101):
    num += x
    if num >= N:
        print(x)
        break