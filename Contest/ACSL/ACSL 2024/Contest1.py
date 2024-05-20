row = str(input())
row = row.zfill(4)
row = [row[i] for i in range(len(row))]
hand = list(input().split())
pile = list(input().split())

last = 3
double_card = False
while True:
  flag = False
  if (len(hand)==0):
    break
  for card in hand:
    for i in range(4):
      if (double_card==False):
        index = (last+1+i)%4
      else:
        index = last
      if (row[index] == card[0] or row[index] == card[1]):
        last = index
        double_card = False
        if (row[index] == card[0]):
          row[index] = card[1]
        else:
          row[index] = card[0]
        hand.remove(card)
        flag = True
        if (card[0] == card[1]):
          double_card = True
        break
      if double_card:
        break
    if flag:
      break
  if flag==False:
    if (len(pile)==0):
      break
    hand.append(pile[0])
    pile.pop(0)
ans = 0
for card in hand:
  ans += int(card[0]) + int(card[1])
print(ans)
