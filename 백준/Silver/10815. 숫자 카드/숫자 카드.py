import sys

N = int(input())
car_num = set(map(int, sys.stdin.readline().split()))
M = int(input())
M_list = list(map(int, sys.stdin.readline().split()))

for i in M_list:
    print(1 if i in car_num else 0, end=' ')