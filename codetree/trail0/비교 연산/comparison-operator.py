A, B = map(int, input().split())

if A>=B:
    print(1)
    if A>B:
        print(1)
    else:
        print(0)
else:
    print(0, 0, sep='\n')

if A<=B:
    print(1)
    if A<B:
        print(1)
    else:
        print(0)
else:
    print(0, 0, sep='\n')

if A==B:
    print(1, 0, sep='\n')
else:
    print(0, 1, sep='\n')