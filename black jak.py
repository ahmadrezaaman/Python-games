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
    def __init__(self, num,suit):
        self.score = num
        if num in ["Jack", "Queen", "King"]:
            self.score = 10
        elif num in ["Ace"]:
            self.score = 11
        self.num = num
        self.suit = suit

player_cards = []
father_cards = []
cards=[]
for i in ["heart", "diamond", "club", "spade"]:
    for j in range(1,11):
        cards.append(Card(j,i))
random.shuffle(cards)
for i in range(2):
    player_cards.append(cards.pop())
    print(f'your {i+1}th card is: {player_cards[i].num} {player_cards[i].suit}')
    father_cards.append(cards.pop())
    time.sleep(1)
print(f'the father card is: {father_cards[0].num} {father_cards[0].suit}')
time.sleep(1)
sum_player_cards = player_cards[0].score + player_cards[1].score
while input('do you want to continue? (y/n)')[0].lower() == 'y':
    x=cards.pop()
    player_cards.append(x)
    sum_player_cards +=x.score
    print(f'your last card is: {x.num} {x.suit}')
print(player_cards[0].score, player_cards[1].score, player_cards[2].score)
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

