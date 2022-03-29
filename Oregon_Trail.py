# Oregon Trail Game
from audioop import add
import random

# Introduction

name = input("What is your name? ")
print(f"Hello {name}, it is March 1st which means it's time to start your journey to Oregon City! You must reach the city before December 31 or else you will face the ravages of winter.")
print("Understand that in most scenarios little to no help will be available however you can type 'help' to see if there is any hints on what to do if you are stuck.")

# Player stats/ global variables

health = 5
food = 500
miles_left = 2000
days_left = 305
# Defined functions

def status():
    print(f"You have {health} health left, {food} pounds of food left,  {days_left} days and {miles_left} miles left to go.")

def travel():
    global miles_left
    global food
    global days_left

    days_this_travel = random.randint(3,7)
    miles_traveled = random.randint(30,60)


    print(f"You traveled {miles_traveled} miles in {days_this_travel} days")
    miles_left -= miles_traveled
    food -= days_this_travel * 5
    days_left -= days_this_travel

def rest():
    global food
    global days_left

    days_this_rest = random.randit(2,5)
    days_left -= days_this_rest
    food -= days_this_rest * 5

def hunt():
    global food
    global days_left

    food += 100
    days_this_hunt = random.randint(2,5)
    food -= days_this_hunt * 5
    days_left -= days_this_hunt
    print(f"Successful hunt! You've gained 100 pounds of food but the hunt took {days_this_hunt} days.")

def help():
    print("Need some help? Type these commands to figure out the basics:  \n"
    "status: Tells you your game stats. \n" 
    "travel: You and your group move towards Oregan for 30-60 miles and takes 3-7 days. \n"
    "rest: Resting increases your health by one and requires 2-5 days. \n"
    "hunt: Hunting brings your group 100lbs of food and requires 2-5 days to complete. \n"
    "quit: Typing 'quit' sends your group home in defeat and ends the game.")

def quit():
    global game_over

    print("Your group raises the white flag and heads home, surrendering to the Oregon Trail.")
    game_over = True



# Game loop

game_over = False

while not game_over:
    user_choice = input("What is your next move? (status, travel, rest, hunt, help, quit)")

    if user_choice == 'status':
        status()
    
    elif user_choice == 'travel':
        travel()

    elif user_choice == 'rest':
        rest()

    elif user_choice == 'hunt':
        hunt()

    elif user_choice == 'help':
        help()
    
    elif user_choice == 'quit':
        quit()
    
    # Game over scenarios 
    elif miles_left == 0:
        print("Congratulations on making it to Oregon City! Your group can finally rest after such a long journey!")
        game_over = True
    
    elif days_left == 0:
        print("Unfortunately your group didn't make it to Oregon City before winter intensified. Your group is now stuck in the snow to die.")
        game_over = True
    
    elif food == 0:
        print("Your groups food supply has been used up and now you will starve to death.")
        game_over = True
    
    elif health == 0:
        print("Your health has been depleted resulting in death.")
        game_over = True
