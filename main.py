import random

def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissors) : ")
  options = ['rock','paper','scissors']
  computer_choice = random.choice(options)
  choices = {"player": player_choice,"computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player} and computer chose {computer}")
  if player == computer:
    return "It's a tie!"  
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "Paper covers Rock! You lose."
  elif player == "paper":
    if computer == "rock":
      return "Paper covers Rock! You win!."
    else:
      return "Scissors cuts paper! You lose."  
  elif player == "scissors":
    if computer == "rock":
      return "Rock smashes scissors! You lose."
    else:
      return "Scissors cuts paper! You win!"

choices = get_choices()
player = choices["player"]
computer  = choices["computer"]
result=check_win(player,computer)
print(result)