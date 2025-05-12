from collections import defaultdict

N = int(input())
round = defaultdict(int)

for i in range(N):
    S, X = map(str, input().split())
    round[S] += int(X)

if 5 in round.values():
    print('YES')
else:
    print('NO')