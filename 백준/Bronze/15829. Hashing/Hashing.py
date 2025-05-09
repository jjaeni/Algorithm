M = 1234567891; r=31

from string import ascii_lowercase
alphabet_list = list(ascii_lowercase) # 알파벳 리스트 생성
alphabet_dict = {v:k for k, v in dict(enumerate(alphabet_list)).items()}

while True:
    l = int(input())
    if l < 1 or l > 50:
        continue
    else:
        string = input()
        if len(string) == l and string.isalpha():
            string = list(string.lower())
            break
        else:
            continue

H = 0
for i in range(len(string)):
    ai = alphabet_dict.get(string[i])+1
    H += ai * pow(r, i, M) % M
print(H)