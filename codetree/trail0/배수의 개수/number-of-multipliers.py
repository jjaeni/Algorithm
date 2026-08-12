list = [int(input()) for _ in range(10)]
mul3 = 0
mul5 = 0

for i in list:
    if i%3==0 and i%5==0:
        mul3+=1
        mul5+=1
    elif i%3==0:
        mul3+=1
    elif i%5==0:
        mul5+=1
    else:
        continue

print(mul3, mul5)