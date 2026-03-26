# First I imported time and random.

import time
import random

# My Global Variables
jungle = []
palmerston_north = []
kapiti = []
te_papa = []

# Using dictionary to store all the values for the specific areas amd items that are in those areas.
jungle = [
    {
        "Type": "Tool",
        "Name": "Wooden Pickaxe",
        "Durability": random.randint(50, 100),
        "Special Ability": "None",

    },
    {
        "Type": "Object",
        "Name": "Tree",
        "Durability": random.randint(1, 5),
        "Special Ability": "None",
    },

    {
        "Type": "Tool",
        "Name": "Machete",
        "Durability": random.randint(250, 400),
        "Special Ability": "Destroy All",

    },

    {
        "Type": "Object",
        "Name": "Bush",
        "Durability": random.randint(10, 25),
        "Special Ability": "None",

    },

    {
        "Type": "Animal",
        "Name": "Parrot",
        "Health": random.randint(25, 30),
        "Special Ability": "Gust",
        "Spawnrate": random.randint(20, 50)
    },

    {
        "Type": "Animal",
        "Name": "Bear",
        'Health': random.randint(90, 100),
        "Special Ability": "Roar",
        "Spawnrate": random.randint(1, 2)
    },
]
palmerston_north = [
    {
        "Type": "Tool",
        "Name": "Car",
        "Durability": random.randint(500, 1000),
        "Special Ability": "None",
    },

    {
        "Type": "Human",
        "Name": "Ren",
        "Health": random.randint(100, 120),
        "Special Ability": "Guide",
    },

]

kapiti = [
    {
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

    },

    {
        "Type": "Tool",
        "Name": "Money",
        "Special Ability": "None",
        "Durability": random.randint(5, 20),
        "Value": random.randint(5, 100),

    },

    {
        "Type": "Animal",
        "Name": "Eagle",
        "Health": random.randint(100, 200),
        "Spawnrate": random.randint(5, 6),
        "Special Ability": "Windwisp",
    },

    {
        "Type": "Object",
        "Name": "Bus",
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
]


# I am going to be making my main menu here and creating my first funtion that inputs to the user on what is their name is and age. Also will show the options like play game, exit, and player instructions.
def main_menu():
    while True:
        try:
            name = (input("What is your name?"))
            age = int(input("WHat is your age?"))
            break  # exists the loop and starts in the menu
        except ValueError:
            print("Invalid Input!, please enter numbers in age and string in name!")


    while True:
        print("1. Play Game")
        print("2. Player Instructions")
        print("3. Exit")
        choice = input("Enter your choice")


        if choice == '1':
                    print("Welcome to the amazing journey to Te Papa!")
        elif choice == '2':
                    print("---PLAYER INSTRUCTIONS---")
                    print("1. You will start in a jungle and your goal is to reach Te Papa but before you do you will over 3 other distinct areas")
                    print("2. Beware as you will encouter different type of animals, objects, tools, quizez, amd humans which will may give you an advantage or disadvantage")
                    print("3. Also, when you reach Te Papa you can do 2 out of 3 of intriguing quizes which are short in time but big in fun!")
                    print("4. If you lose all your health then you have to restart from the jungle")
                    print("5. GOOD LUCk")
                    print(input("\nPress enter to go back to menu"))
        elif choice == '3':
                    print("Bye, have a nice day!lol")
        else:
            print("Invalid input!")

main_menu()
