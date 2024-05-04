N = int(input())
card = []
for i in range(N):
    card.append(i+1)
card = card[::-1]
while True:
    if len(card) == 1:
        print(*card)
        break
    else:
        print(card.pop(), end=' ')
        card = [card[len(card)-1]]+card[:len(card)-1]