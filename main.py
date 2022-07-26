import random

class Card:

  def __init__(self, token, suit):
    self.token = token
    self.suit = suit
  
  def __str__(self):
    return "%s-of-%s" %(self.token, self.suit)
  
  def __repr__(self):
    return "%s of %s" %(self.token, self.suit)

  def blackjackValue(self):
    if self.token.isdigit():
      return int(self.token)
    elif self.token == "A":
      return 11
    else:
      return 10
  
class Hand:

  def __init__(self):
    self.cards = []
    self.total = 0
    self.bigAceCount = 0
  
  def __str__(self):
    return "%s | %s" %(self.total, self.cards)
  
  def addCard(self, card):
    self.cards.append(card)
    self.total += card.blackjackValue()
    if card.token == "A":
      self.bigAceCount += 1
    if self.total > 21 and self.bigAceCount >= 1:
      self.total -= 10
      self.bigAceCount -= 1

def getDeck():
  suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
  tokens = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []
  for suit in suits:
    for token in tokens:
      deck.append(Card(token, suit))
  return deck

def shuffle(deck):
  last = len(deck) - 1
  for i in range(0, last, 1):
    r = random.randint(i, last)
    if i < r:
      temp = deck[i]
      deck[i] = deck[r]
      deck[r] = temp

def blackjack():
  deck = getDeck()
  shuffle(deck)
  player = Hand()
  player.addCard(deck.pop())
  player.addCard(deck.pop())
  dealer = Hand()
  dealer.addCard(deck.pop())
  dealer.addCard(deck.pop())
  print("Dealer's shown card:", dealer.cards[0])
  print(player)

  playing = player.total < 21
  while playing:
    answer = input("hit or stay?")
    if answer == "hit":
      player.addCard(deck.pop())
      print(player)
      playing = player.total < 21
    elif answer == "stay":
      playing = False
    else:
      print("really? you had one job...")
  print("Your total was", player.total)

  if player.total > 21:
    print("You bust!")
    return

  while dealer.total < player.total:
    dealer.addCard(deck.pop())
  
  # TODO: fix ending conditions
  if player.total == 21:
    print("You got blackjack!")
  elif player.total >= 17:
    print("You got close!")
  else:
    print("Cowards never prevail!")


blackjack()
