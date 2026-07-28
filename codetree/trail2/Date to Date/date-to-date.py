m1, d1, m2, d2 = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 is m2:
    date = (d2-d1)+1
else:
    date = month[m1-1]-(d1-1) + d2
    if m2-m1 >=2:
        for i in range(m1, m2-1):
            date += month[i]
print(date)