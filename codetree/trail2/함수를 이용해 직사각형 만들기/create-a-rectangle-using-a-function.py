def print_square(n, m):
    for _ in range(n):
        print("1" * m)

N, M = map(int, input().split())
print_square(N, M)