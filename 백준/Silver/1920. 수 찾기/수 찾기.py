import sys

N = int(input())
A = set(map(int, sys.stdin.readline().split()))
M = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

for num in num_list:
    print(1 if num in A else 0)