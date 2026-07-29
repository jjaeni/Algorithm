A, B, C = map(int, input().split())

cond = (11*24*60) + (11*60) + 11
cal = (A*24*60) + (B*60) + C

if A<11 or (A==11 and B<11) or (A==11 and B==11 and C<11):
    print(-1)
else:
    print(cal-cond)