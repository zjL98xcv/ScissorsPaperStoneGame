rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


#can call index randomly
#when user wins, score will update +1
#screen to refresh and 

import random
list = [rock, paper, scissors]

score = 0
high_score = 0

is_on = True
while is_on:
  
  user = input("What do you want to move? Rock, paper or scissors?\n")
  
  if user.lower() == "rock":
    user = rock
    print(rock)
  elif user.lower() == "paper":
    user = paper
    print(paper)
  elif user.lower() == "scissors":
    user = scissors
    print(scissors)
  else:
    print("Invalid answer. Please type again.")
    continue
  computer = random.choice(list)
  print(f"\nComputer chooses to play\n{computer}")
  
  
  if user == rock and computer == scissors:
    score += 1
    print(f"You win. Your score : {score}")
  elif user == paper and computer == rock:
    score += 1
    print(f"You win. Your score : {score}")
  elif user == scissors and computer == paper:
    score += 1
    print(f"You win. Your score : {score}")
  elif user == computer:
    print("Its a draw")
  else:
    print("You lose")
    if score > high_score:
      high_score = score
      print(f"Your high score is {high_score}")
    score = 0

  
  
  while True:
    play_again = input("Do you want to play again? Type 'yes' or 'no' ")
    if play_again.lower() == "yes":
      break
    elif play_again.lower() == "no": 
      is_on = False
    else:
      print("Invalid answer. Please type again. ")
      continue
  
    break
    
    

