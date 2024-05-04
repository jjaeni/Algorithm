T = int(input())
A = []
B = []
for i in range(T):
    while True:
        a, b = map(int, input().split())
        if 0<a<10 and 0<b<10:
            A.append(a)
            B.append(b)
            break
        else:
            print('A와 B는 1~9 사이의 정수이어야 함')
            continue

for i in range(T):
    print(f"Case #{i+1}: {A[i]+B[i]}")