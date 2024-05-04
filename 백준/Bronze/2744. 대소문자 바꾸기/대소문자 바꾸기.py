word = input("")

for w in word:
    if w.isupper() == True:
        print(w.lower(), end='') # end옵션: 뒤의 출력값 이어서 출력(줄바꿈 X)
    else:
        print(w.upper(), end='')