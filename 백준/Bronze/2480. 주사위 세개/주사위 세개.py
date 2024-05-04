num1, num2, num3 = map(int, input().split())
dice = [num1, num2, num3]

for i in set(dice):
    if dice.count(i) == 3:
        prize = 10000 + 1000*i
        break
    elif dice.count(i) == 2:
        prize = 1000 + 100*i
    
    else:
        if len(set(dice)) == 3:
            prize = max(set(dice))*100
        else:
            pass
print(prize)