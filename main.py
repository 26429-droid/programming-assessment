#First I imported time and random.

import time
import random

#My Global Variables
jungle = []
palmerston_north = []
kapiti = []
te_papa = []

# Using dictionary to store all the values for the specific areas amd items that are in those areas.
jungle = [
    {
        "Type":"Tool",
        "Name": "Wooden Pickaxe",
        "Durability": random.randint(50,100),
        "Special Ability": "None",

    },
    {
        "Type":"Object",
        "Name": "Tree",
       "Durability": random.randint(1,5),
        "Special Ability": "None",
    },

    {
        "Type":"Tool",
        "Name": "Machete",
        "Durability":random.randint(250,400),
        "Special Ability":"Destroy All",

    },

    {
        "Type":"Object",
        "Name":"Bush",
        "Durability":random.randint(10,25),
        "Special Ability": "None",


    },

    {
        "Type":"Animal",
        "Name": "Parrot",
        "Health":random.randint(25,30),
        "Special Abilty": "Gust",
        "Spawnrate":random.randint(20,50)
    },

    {
        "Type":"Animal",
        "Name": "Bear",
        'Health':random.randint(90,100),
        "Special Abilty": "Roar",
        "Spawnrate":random.randint(1,2)
    },
]
palmerston_north = [
    {
        "Type":"Tool",
        "Name":"Car",
        "Durability":random.randint(500,1000),
        "Special Ability":"None",
    },

    {
        "Type":"Human",
        "Name": "Ren",
        "Health":random.randint(100,120),
        "Special Ability": "Guide",
    },

]

kapiti= [
    {
        "Type":"Tool",
        "Name":"Fishing Rod",
        "Durability":random.randint(500,700),
        "Special Ability": "None",

    },

    {
        "Type":"Animal",
        "Name":"Long Finned Eel",
        "Health":random.randint(25,40),
        "Special Ability":"Splash",
        "Spawnrate":random.randint(14,100),

    },

    {
        "Type":"Tool",
        "Name": "Money",
        "Special Ability": "None",
        "Durability":random.randint(5,20),
        "Value": random.randint(5,100),

        
    },

    {
        "Type": "Animal",
        "Name": "Eagle", 
        "Health": random.randint(100,200),
        "Spawnrate":random.randint(5,6),
        "Special Ability":"Windwisp",
    },

    {
        "Type":"Object",
        "Name": "Bus",
        "Durability":random.randint(100,200),
        "Spawnrate":random.randint(25,50),
        "Special Ability":"Route taker",

    },


]

te_papa = [
    {

    }
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
        "Spawnrate":random.randint(10,100),

    },



]

