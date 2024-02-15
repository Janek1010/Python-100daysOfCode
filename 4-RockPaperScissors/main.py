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
options = ['rock', 'paper', 'scissors']
drawings = [rock, paper, scissors]
player = input("What is your choice? rock,paper or scissors?").lower()
computer = options[random.randint(0,2)]

print("You chose")
print(drawings[options.index(player)])
print("Computer chose")
print(drawings[options.index(computer)])

if player == computer:
    print("It's a draw!")
elif (player == 'rock' and computer == 'paper') or (player == 'scissors' and computer == 'rock'):
    print("You lost!")
else:
    print("You won!")





