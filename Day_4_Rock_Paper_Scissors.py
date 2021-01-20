import random
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
picture = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print("User: ")
print(picture[user])

print("\n\n")

computer = random.randint (0,2)
print("Computer: ")
print(picture[computer])

if user >= 3 or user < 0: 
  print("invalid number") 

elif user == 0 and computer == 2:
  print("You win")

elif computer == 0 and user == 2:
  print("You lose")

elif user < computer:
  print("You lose")

elif computer < user:
  print("You win")

elif computer == user:
  print("It's a draw")
