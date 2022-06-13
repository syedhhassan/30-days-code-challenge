import random as r

def coinflip():
    print('Tossing of a Coin')
    flip=r.randint(0,1)
    if flip==0:
        print('Tails')
    else:
        print('Heads')

def rolling():
    print('Rolling of a Die')
    print(r.randint(1,6))

def decksuits():
    print('Selcetion of a Suit in a Deck')
    suit=r.randint(1,4)
    if suit==1:
        print('Hearts')
    elif suit==2:
        print('Diamonds')
    elif suit==3:
        print('Spades')
    else:
        print('Clubs')

print('Operations on Random Library')
while True:
    print('1.Flip a Coin')
    print('2.Rolling a Die')
    print('3.Selection of a Suit in a Deck')
    print('4.Exit')
    c=int(input('Enter your choice: '))
    if c==1:
        coinflip()
    elif c==2:
        rolling()
    elif c==3:
        decksuits()
    elif c==4:
        break
    else:
        print('Invalid Choice')