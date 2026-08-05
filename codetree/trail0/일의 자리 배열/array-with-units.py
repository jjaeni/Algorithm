lst = list(map(int, input().split()))

for ele in lst:
    print(ele, end=" ")

for i in range(8):
    print((lst[-1]+lst[-2])%10, end=" ")
    lst.append((lst[-1] + lst[-2])%10)
