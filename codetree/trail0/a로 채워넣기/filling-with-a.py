string = input()


for idx in range(len(string)):
    if idx == 1 or idx == (len(string)-2):
        print('a', end='')
    else:
        print(string[idx], end='')