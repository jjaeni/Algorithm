while True:
    word = input()
    if 1 <= len(word) <= 100:
        print(len([x for x in word if x in ['a', 'e', 'i', 'o', 'u']]))
        break
    else:
        continue