score = []
while True:
    solve = int(input())
    if solve<0:
        continue
    else:
        score.append(solve)
        if len(score) == 8:
            break
total = 0
num = []
for j in list(reversed(sorted(score)))[:5]:
    total += j
    num.append(score.index(j)+1)

print(total)
for i in sorted(num):
    print(i, end = ' ')