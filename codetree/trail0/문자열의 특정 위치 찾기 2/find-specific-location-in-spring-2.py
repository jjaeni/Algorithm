list = ['apple', 'banana', 'grape', 'blueberry', 'orange']
str = input()
cnt = 0

for idx in list:
    if idx[2] == str or idx[3] == str:
        print(idx)
        cnt+=1
        continue
print(cnt)