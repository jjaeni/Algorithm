N, M = map(int, input().split())

def lcm(n, m):
    mul = n*m

    while n*m != 0:
        if n>=m:
            n%=m
        else:
            m%=n
    
    print(int((mul)/(n+m)))

lcm(N, M)