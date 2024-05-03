N = int(input())
password = []
while True:
    pw = input()
    if pw.isalnum() == True:
       password.append(pw)
       if len(password) == N:
          break
for i in password:
    if 5 < len(i) < 10:
        print('yes')
    else:
        print('no')