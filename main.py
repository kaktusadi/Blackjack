import random
from replit import clear
from art import logo

def deal_card():
  """returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, cpu_score):
  if user_score == cpu_score:
    return "Draw "
  elif cpu_score == 0:
    return "You lost, CPU has a Blackjack!"
  elif user_score > 21:
    return "You went over. You lose"
  elif cpu_score > 21:
    return "Oponnent went over. You win"
  elif user_score > cpu_score:
    return "You win"
  else:
    return "You lose"

def play_game():

  print(logo)


  cpu_cards = []
  user_cards = []
  game_over_flag = False


  for i in range(2):
    #new_card = deal_rard()
    #user_cards.append(new_card)
    user_cards.append(deal_card())
    cpu_cards.append(deal_card())


  while not game_over_flag:

    user_score = calculate_score(user_cards)
    cpu_score = calculate_score(cpu_cards)
    print(f"Your Cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {cpu_cards[0]}")

    if user_score == 0 or cpu_score == 0 or user_score > 21:
      game_over_flag = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        game_over_flag = True

  while cpu_score != 0 and cpu_score < 17:
    cpu_cards.append(deal_card())
    cpu_score = calculate_score


  print(f"      Your final hand: {user_cards}, final score: {user_score}")
  print(f"      CPU's final hand: {cpu_cards}, final score: {cpu_score}")
  print(compare(user_score, cpu_score))

  while input("Do you want to play a game of Blackjack? 'y' or 'n': ") == "y":
    clear()
    play_game()
# import random

# def game():
#   cards = [11, 2 ,3 ,4 ,5 ,6 ,7 ,8, 9, 10, 10, 10, 10]

#   cpu_cards = []
#   user_cards = []
#   user_score = []
#   cpu_score = []

#   def take_cards(player, amount):
#     for card in range(0, amount):
#       return random.choice(cards)
#       # cpu_choice = random.choice(cards)
#       # user_choice = random.choice(cards)
#       # cpu_cards.append(cpu_choice)
#       # user_cards.append(user_choice)

#   def sum_scores(chosen_list):
#     total = 0
#     for i in range(len(chosen_list)):
#       total += chosen_list[i]
#       return total

#   def check_ace(player_cards):
#     for card in player_cards:
#         if card == "11":
#           card == "1"
#           return True

#   def compare():
#     if user_score_sum == cpu_score_sum:
#       print("Draw")
#     elif user_score_sum > cpu_score_sum:
#       print("You win.")
#     else:
#       print(" CPU has more points, you lose.")

#   user_cards = take_cards(user_cards, amount = 2)
#   cpu_cards = take_cards(cpu_cards, amount = 2)

#   game_continue = True

#   while game_continue:
#     user_score_sum = sum_scores(user_score)
#     cpu_score_sum = sum_scores(cpu_score)

#     if cpu_score_sum or user_score_sum == 21:
#       if cpu_score_sum == 21:
#         print("CPU has a blackjack, CPU wins.")
#         game_continue = False
#       else:
#         print("User has a blackjack, User wins.")
#         game_continue = False
#     elif user_score_sum > 21:
#       check_ace(user_cards)
#       if False:
#         print("You lose.")
#       else:
#         if input("Do you want to take another card? 'y' or 'n'\n") == "y":
#           take_cards(user_cards, 1)
#           game_continue = True
#         elif cpu_score_sum < 17:
#           take_cards(cpu_cards, 1)
#           if cpu_score_sum > 21:
#             print("CPU lose, You win.")
#           else:
#             compare()
#   else:
#     if input("Game Over, restart? 'y' or 'no'\n") == "y":
#           game()

# game()


