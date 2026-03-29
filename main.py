
# First I imported time, random, and sys (for the third choice).

import time
import random
import sys

# My Global Variables
# My Global Variables
jungle = []
palmerston_north = []
kapiti = []
te_papa = []
player_health = 100
# Using dictionary to store all the values for the specific areas amd items that are in those areas.
jungle = [
    {
        "Type": "Tool",
        "Type": "Tool",
        "Name": "Wooden Pickaxe",
        "Durability": random.randint(50, 100),
        "Durability": random.randint(50, 100),
        "Special Ability": "None",

    },
    {
        "Type": "Object",
        "Type": "Object",
        "Name": "Tree",
        "Durability": random.randint(1, 5),
        "Durability": random.randint(1, 5),
        "Special Ability": "None",
    },

    {
        "Type": "Tool",
        "Type": "Tool",
        "Name": "Machete",
        "Durability": random.randint(250, 400),
        "Special Ability": "Destroy All",
        "Durability": random.randint(250, 400),
        "Special Ability": "Destroy All",

    },

    {
        "Type": "Object",
        "Name": "Bush",
        "Durability": random.randint(10, 25),
        "Type": "Object",
        "Name": "Bush",
        "Durability": random.randint(10, 25),
        "Special Ability": "None",

    },

    {
        "Type": "Animal",
        "Type": "Animal",
        "Name": "Parrot",
        "Health": random.randint(25, 30),
        "Health": random.randint(25, 30),
        "Special Ability": "Gust",
        "Spawnrate_Safe": random.randint(5, 30),
        "Spawnrate_Dangerous":random.randint(50, 75),
    },

    {
        "Type": "Animal",
        "Type": "Animal",
        "Name": "Bear",
        'Health': random.randint(90, 100),
        'Health': random.randint(90, 100),
        "Special Ability": "Roar",
        "Spawnrate_Safe": random.randint(1, 5),
        "Spawnrate_Dangerous":random.randint(40, 60),
    },

        {
        "Type": "Human",
        "Name": "John",
        "Health": random.randint(80, 100),
        "Special Ability": "Guide",
    },

]
palmerston_north = [
    {
        "Type": "Tool",
        "Name": "Car",
        "Durability": random.randint(500, 1000),
        "Special Ability": "None",
        "Type": "Tool",
        "Name": "Car",
        "Durability": random.randint(500, 1000),
        "Special Ability": "None",
    },

    {
        "Type": "Human",
        "Type": "Human",
        "Name": "Ren",
        "Health": random.randint(100, 120),
        "Health": random.randint(100, 120),
        "Special Ability": "Guide",
    },

]

kapiti = [
kapiti = [
    {
        "Type": "Tool",
        "Name": "Fishing Rod",
        "Durability": random.randint(500, 700),
        "Type": "Tool",
        "Name": "Fishing Rod",
        "Durability": random.randint(500, 700),
        "Special Ability": "None",

    },

    {
        "Type": "Animal",
        "Name": "Long Finned Eel",
        "Health": random.randint(25, 40),
        "Special Ability": "Splash",
        "Spawnrate": random.randint(14, 100),
        "Type": "Animal",
        "Name": "Long Finned Eel",
        "Health": random.randint(25, 40),
        "Special Ability": "Splash",
        "Spawnrate": random.randint(14, 100),

    },

    {
        "Type": "Tool",
        "Type": "Tool",
        "Name": "Money",
        "Special Ability": "None",
        "Durability": random.randint(5, 20),
        "Value": random.randint(5, 100),

        "Durability": random.randint(5, 20),
        "Value": random.randint(5, 100),

    },

    {
        "Type": "Animal",
        "Name": "Eagle",
        "Health": random.randint(100, 200),
        "Spawnrate": random.randint(5, 6),
        "Special Ability": "Windwisp",
        "Name": "Eagle",
        "Health": random.randint(100, 200),
        "Spawnrate": random.randint(5, 6),
        "Special Ability": "Windwisp",
    },

    {
        "Type": "Object",
        "Type": "Object",
        "Name": "Bus",
        "Durability": random.randint(100, 200),
        "Spawnrate": random.randint(25, 50),
        "Special Ability": "Route taker",
        "Durability": random.randint(100, 200),
        "Spawnrate": random.randint(25, 50),
        "Special Ability": "Route taker",

    },

]

te_papa = [
    {
        "Type": "Human",
        "Name": "Quiz Master",
        "Special Ability": "None",
    {
        "Type": "Human",
        "Name": "Quiz Master",
        "Special Ability": "None",

    },
    },

    {
        "Type": "Quiz",
        "Name": "Quiz of Wellington",
        "Duration": random.randint(2, 5),
        "Number of questions": (5),
        "Special Ability": "None",
    },
    {
        "Type": "Quiz",
        "Name": "Quiz of Wellington",
        "Duration": random.randint(2, 5),
        "Number of questions": (5),
        "Special Ability": "None",
    },

    {
        "Type": "Quiz",
        "Name": "Quiz of Pokemon",
        "Duration": random.randint(1, 2),
        "Number of questions": (3),
        "Special Ability": "None",
    },
    {
        "Type": "Quiz",
        "Name": "Quiz of Countries",
        "Duration": random.randint(1, 2),
        "Number of questions": (3),
        "Special Ability": "None",
    },
    {
        "Type": "Quiz",
        "Name": "Quiz of Pokemon",
        "Duration": random.randint(1, 2),
        "Number of questions": (3),
        "Special Ability": "None",
    },
    {
        "Type": "Quiz",
        "Name": "Quiz of Countries",
        "Duration": random.randint(1, 2),
        "Number of questions": (3),
        "Special Ability": "None",
    },
]

#Added slow text for a more dramatic text navigation between John and the user.
def slow_text (text):
       for character in text:
              print(character, end='', flush = True)
              time.sleep (0.07)
       print()
#This function is to describe the Jungle route and the instructiosn and routes untill they reach the second route.
def jungle(name):
       global player_health # tells python to use the global variable and also can change the the health.
       slow_text("You find yourself in a wide jungle with no clue on whats going on.")
       slow_text("Suddenly a man appears from the bushes *John*.")
       slow_text(f"Hello {name} welcome to the jungle")
       slow_text(f"Your goal is to reach to Te Papa in 20 Minutes")
       slow_text("Beware, you will go through many areas, which can hurt you.")
       slow_text("So its up to you, do you want to go to the side which is longer which is safer but with worse  in tools or short route with more animals but better tools!")
       slow_text("1. Safe route, Wooden Pickaxe")
       slow_text("2. The shorter route, Machete ")
       route = input("Choose your route: ")

       if route == "1":
            slow_text("Congrats scaredy cat! Welcome to the safer  but looonger route!")
       elif route == '2':
            slow_text("Congrats vicious warrior! Welcome to the *dangerous* but shorter route!")
       else:
            slow_text("Invalid Choice! Please try again!")
    
# I am going to be making my main menu here and creating my first funtion that inputs to the user on what is their name is and age. Also will show the options like play game, exit, and player instructions.
def main_menu():
    while True:
        try: #Added try and except so if a user puts boolean or string instead of integer
                #It won't crash
            name = (input("What is your name?"))
            age = int(input("What is your age?"))
            break  # exists the loop and starts in the menu
        except ValueError:#while True runs continuously untill a valid integer is entered for age. When a valid integer given, it breaks the loop and continues through the next step in a mannerly order. Making it easier for the user to navigate.
            print("Invalid Input!, please enter numbers in age and string in name!")


    while True:
        print("1. Play Game")
        print("2. Player Instructions")
        print("3. Exit")
        choice = input("Enter your choice")


        if choice == '1':
                    print("Welcome to the amazing journey to Te Papa!")
                    jungle(name)
        elif choice == '2':
                    print("---PLAYER INSTRUCTIONS---")
                    print("1. You will start in a jungle and your goal is to reach Te Papa but before you do you will over 3 other distinct areas")
                    print("2. Beware as you will encounter different type of animals, objects, tools, quizzes, and humans which will may give you an advantage or disadvantage")
                    print("3. Also, when you reach Te Papa you can do 2 out of 3 of intriguing quizzes which are short in time but big in fun!")
                    print("4. If you lose all your health then you have to restart from the jungle")
                    print("5. GOOD LUCK")
                    print(input("\nPress enter to go back to menu"))
        elif choice == '3':
                    print("Bye, have a nice day!")
                    sys.exit()#helps to close the program entirely
        else:
            print("Invalid input!")

main_menu()


