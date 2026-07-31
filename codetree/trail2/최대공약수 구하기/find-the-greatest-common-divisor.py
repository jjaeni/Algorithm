N, M = map(int, input().split())

def gcd(n, m):
    while n*m != 0:
        if n>=m:
            n%=m
        else:
            m%=n
    print(n+m)
    
gcd(N, M)