N = int(input())
sumnum = 0
for i in range(1, N+1):
    num_list = list(map(int, list(str(i))))
    seq = []
    for j in range(len(num_list)):
        if j>0:
            seq.append(num_list[j]-num_list[j-1])
        elif j==0 and len(num_list)==1:
            seq.append(num_list[j])
    if len(set(seq)) == 1:
        sumnum +=1
print(sumnum)