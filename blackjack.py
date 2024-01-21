import random
from replit import clear
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
user_cards = [deal_card(),deal_card()]
computer_cards = [deal_card(),deal_card()]
def calculate_score(L):
  if L==21 and len(L)==2:
    return 0
  
  if 11 in L and sum(L)>21:
    L.remove(11)
    L.append(1)
  return sum(L)

def compare(user_score,computer_score):
  if user_score==computer_score:
    print("Draw")
  elif computer_score==0:
    print('You Lose, opponent has BlackJack')
  elif user_score==0:
    print("You Win , you have BlackJack")
  elif user_score>21:
    print("You Lose, you went over")
  elif computer_score>21:
    print("You Win,opponent went over")
  elif user_score>computer_score:
    print("You Win")
  else:
    print(" You Lose")

def play_game():
  check=True
  while check==True:
    user_score=calculate_score(user_cards)
    comp_score=calculate_score(computer_cards)
    print("Your cards: ",user_cards)
    print("Your score: ",user_score)
    print("Computer first card: ",computer_cards[0])
    if user_score ==0 or comp_score==0 or user_score>21:
      print('You Lose')
      check=False
    else:
      u_choice=input('Do you want to draw cards?')
      if u_choice=='y':
        user_cards.append(deal_card())
        play_game()
      else:
        print('Game has ended')
        check=False
  while comp_score !=0 and comp_score<17:
    computer_cards.append(deal_card())
  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {comp_score}")
  compare(user_score,comp_score)
while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
  clear()
  play_game()