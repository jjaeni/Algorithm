import sys
input=sys.stdin.readline

N = int(input())
stack = []

for n in range(N):
    order = input().strip().split()
    if order[0].lower() == 'push':
        stack.append(int(order[1]))

    elif order[0].lower() == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif order[0].lower() == 'size':
        print(len(stack))

    elif order[0].lower() == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order[0].lower() == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])