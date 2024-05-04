input_int = []
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        input_int.append([a, b])
for i in input_int:
    print(sum(i))