def print_square(n):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(n):
        for idx in range(n*i, n*(i+1)):
            print(lst[idx%9], end = " ")
        print()

N = int(input())
print_square(N)