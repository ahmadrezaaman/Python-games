import time
import random
print('''\n\t*** welcome to our casino ***\n
\t............................
\t...                      ...
\t..  A                     ..
\t.            .             .
\t.           ...            .
\t.          .....           .
\t.         .......          .
\t.        .........         .
\t.         .......          .
\t.          .....           .
\t.           ...            .
\t.            .             .
\t..                     A  ..
\t...                      ...
\t............................
''')
time.sleep(2)
class Card:
    def __init__(self, num,suit,score='0'):
        self.score = score
        if num in ["1","2","3","4","5","6","7","8","9","10"]:
            self.score = int(num)
        elif num in ["Jack", "Queen", "King"]:
            self.score = 10
        else:
            self.score = 11
        self.num = num
        self.suit = suit

player_cards = []
father_cards = []
cards=[]
for i in ["heart", "diamond", "club", "spade"]:
    for j in ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']:
        cards.append(Card(j,i))
random.shuffle(cards)
for i in range(2):
    player_cards.append(cards.pop())
    print(f'your {i+1}th card is: {player_cards[i].num} {player_cards[i].suit}')
    father_cards.append(cards.pop())
    time.sleep(1)
print(f'the father card is: {father_cards[0].num} {father_cards[0].suit}')
time.sleep(1)
c_d=input("do you want to continue?(y/n)")
i=2
sum_player_cards = 0
while c_d in ['y','Y']:
    player_cards.append(cards.pop())
    print(f"your {i+1}th card is: {cards[i].num} {cards[i].suit}")
    c_d = input("do you want to continue?(y/n)")
    sum_player_cards += player_cards[i].score
    i=i+1
print(f'sum of your scores is: {sum_player_cards}')
if sum_player_cards > 21:
    print("sorry my frined you lose")
    exit()
sum_father_cards = father_cards[0].score+father_cards[1].score
i=2
while sum_father_cards <17:
    father_cards.append(cards.pop())
    sum_father_cards += father_cards[i].score
    i=i+1
if sum_father_cards > 21:
    print("you win")
    print(sum_father_cards)
    exit()
if sum_father_cards > sum_player_cards:
    print("sorry my frined you lose")
    print(sum_father_cards)
    exit()
if sum_father_cards < sum_player_cards:
    print("you win")
    print(sum_father_cards)
    exit()
if sum_father_cards == sum_player_cards:
    print("sorry my frined you lose")
    print(sum_father_cards)
    exit()









