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
sign=[rock,paper,scissors]
you=int(input("enter the 0 for rock , 1 for paper, 2 for scissors"))
computer=random.randint(0,2)
if you==0 and computer==2:
  print("you win")
elif you==1 and computer==0:
  print("you win")
elif you==2 and computer==1:
  print("you win")
elif you==computer:
  print("draw")    
else:
  print(" you lost")      
