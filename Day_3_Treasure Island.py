print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You are at a crossroad. Which way do you want to go? Type left or right\n\n").lower()

if choice1 == 'left':
  
  choice2 = input("\nYou have discovered a pond. What do you do? Type swim or wait\n\n").lower()
  
  if choice2 == 'wait':
    choice3 = input("\nThree doors arose from the pond, Which door do you wish to enter? Type red, yellow or blue\n\n").lower()
    if choice3 == 'red':
      print ("\nYou have been engulf in flames. Game Over")

    elif choice3 == 'yellow':
      print ("\nYou have discovered the hidden treasure. \n You Win!")

    elif choice3 == 'blue':
      print ("\nYou are assualted by a ferocious beast. \n Game Over")

    else:
      print (" \n Game Over")

  else:
    print ("\nYou have been attack by Trouts. \n Game Over")
else:
   print ("\nYou have fallen into a hole. \n Game Over")
