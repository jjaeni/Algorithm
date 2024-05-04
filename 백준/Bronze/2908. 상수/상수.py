num1, num2 = input().split()

list = []
for i in [num1, num2]:
    reverse_num = []
    for j in i:
        reverse_num.append(j)
    list.append(''.join(reverse_num[::-1]))

if list[0] < list[1]:
    print(list[1])
else:
    print(list[0])