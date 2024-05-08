numseq=[]
for x in range(1, 1000):
    if len(numseq) != 1000:
        if x ==1:
            numseq.append(x)
        else:
            for i in range(x):
                numseq.append(x)
                if len(numseq)==1000:
                    break
    else:
        break

while True:
    A, B = map(int, input().split())
    if 1 <= A <= B <= 1000:
        print(sum(numseq[A-1:B]))
        break
    else:
        continue