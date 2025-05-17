import sys

N, M = map(int, sys.stdin.readline().split())
N_list = [sys.stdin.readline().strip() for i in range(N)]
M_list = [sys.stdin.readline().strip() for i in range(M)]

intersection = sorted(set(N_list).intersection(set(M_list)))
print(len(intersection))
for name in intersection:
    print(name)