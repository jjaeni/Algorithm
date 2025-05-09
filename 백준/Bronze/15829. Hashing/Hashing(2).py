# Clean ver.
M = 1234567891
r = 31
H = 0

while True:
    L = int(input())
    string = input()
    if len(string) == L:
        break
    else:
        print('범위 오류')

for i in range(L):
    ai = ord(string[i])-96 # a:97
    H += ai * pow(r, i, M)
    H %= M # %: 나머지 연산자

print(H)
