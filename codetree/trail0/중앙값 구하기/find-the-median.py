A, B, C = map(int, input().split())
lst = [A, B, C]

for e in lst:
    if e != min(lst) and e != max(lst):
        print(e)