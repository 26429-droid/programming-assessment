#First I imported time and random.

import time
import random


# Using dictionary to store all the values for the specific areas amd items that are in those areas.
jungle = [
    {
        "Type":"Tool",
        "Name": "Wooden Pickaxe",
        "Durabilty": random.randint(50,100),
        "Special Abilty": "None",

    },
    {
        "Type":"Object",
        "Name": "Tree",
        "Durabilty": random.randint(1,5),
        "Special Abilty": "None",
    },

    {
        "Type":"Tool",
        "Name": "Machete",
        "Durabilty":random.randint(250,400),
        "Special Abilty":"Destroy All",

    },

    {
        "Type":"Object",
        "Name":"Bush",
        "Durabilty":random.randint(10,25),
        "Special Abilty": "None",


    },

    {
        "Type":"Animal",
        "Name": "Parrot",
        "Health":random.randint(25,30),
        "Special Abilty": "Gust",
        "Spawnrate":random.randint(20,50),
    },

    {
        "Type":"Animal",
        "Name": "Bear",
        'Health':random.randint(90,100),
        "Special Abilty": "Roar",
        "Spawnrate":random.randint(1,2),
    },
]
palmerston_north = [
    {
        "Type":"Tool",
        "Name":"Car",
        "Durabilty":random.randint(500,1000),
        "Special Abilty":"None",
    },

]

kapiti= [
    {
        "Type":"Tool",
        "Name":"Fishing Rod",
        "Durabilty":random.randint(500,700),
        "Special Abilty": "None",

    },

    {
        "Type":"Animal",
        "Name":"Long Finned Eel",
        "Health":random.randint(25,40),
        "Special Abilty":"Splash",
        "Spawnrate":random.randint(75.100),

    },



]

