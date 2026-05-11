
 #First I imported time, random, and sys (for the third choice).

import time
import random
import sys

#My Global Variables
jungle_area = []
palmerston_north = []
kapiti = []
te_papa = []
player_health = 100
# Using dictionary allows multiple properties is to be stored for each item.
jungle_area = [
    {
        "Type":"Tool",
        "Name": "Wooden Pickaxe",
        "Durability": random.randint(50,100),
    },
    {
        "Type":"Object",
        "Name": "Tree",
        "Durability": random.randint(1,5),
  
    },

    {
        "Type":"Tool",
        "Name": "Machete",
        "Durability":random.randint(250,400),

    },
    {
        "Type":"Object",
        "Name":"Bush",
        "Durability": random.randint(10, 25),

    },
    {
        "Type":"Animal",
        "Name": "Parrot",
        "Health": random.randint(25, 30),
        "Spawnrate_Safe": random.randint(10, 75),
        "Spawnrate_Dangerous":random.randint(75, 100),
    },
    {
        "Type":"Animal",
        "Name": "Bear",
        'Health':random.randint(90,100),
        "Spawnrate_Safe": random.randint(1, 5),
        "Spawnrate_Dangerous":random.randint(40, 60),
    },
    {
        "Type": "Human",
        "Name": "John",
        "Health": random.randint(80, 100),
    }
]

palmerston_north = [
{
        "Type":"Tool",
        "Name":"Car",
        "Special Ability":"None",
        "Durability": random.randint(500, 1000),
},

{
        "Type": "Human",
        "Name": "Ren",
        "Health":random.randint(100,120),
},

]

kapiti_items= [
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
        "Spawnrate":random.randint(60,100),
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
        "Spawnrate":random.randint(50,90),
      },



      {
        "Type":"Object",
        "Name": "Bus",
        "Special Ability":"Route taker",
        "Durability": random.randint(100, 200),
        "Spawnrate": random.randint(25, 50),
      },


]

te_papa = [
   {
       "Type": "Human",
       "Name": "Quiz Master",


   },


   {
       "Type": "Quiz",
       "Name": "Quiz of Wellington",
       "Duration": random.randint(2, 5),
   },


   {
       "Type": "Quiz",
       "Name": "Quiz of Pokemon",
   },
   {
       "Type": "Quiz",
       "Name": "Quiz of Countries",
   },
]

wellington_quiz =[
    {
            "Question": "What is the captial of New Zealand?",
            "Option1":"A. Wellington",
            "Option2":"B. Auckland",
            "Option3":"C. Hamilton",
            "Option4":"D. Christchurch",
            "Answer":"A",
      

      },
      {
            "Question": "What is one word that people use to descibe Wellington?",
            "Option1":"A. Windy",
            "Option2":"B. Gusty",
            "Option3":"C. Flashy",
            "Option4":"D. Dashy",
            "Answer":"A",
            
      },

      {
            "Question":"What is the best school in Wellington?",
            "Option1":"A. Saint Patricks College",
            "Option2":"B. Samuel Marsden Collegiate ",
            "Option3":"C. Wellington College",
            "Option4":"D. Heretaunga College",
            "Answer":"C",

      },
      {
            "Question":"Whats the most famous job sector in Wellington?",
            "Option1":"A. Construction",
            "Option2":"B. Technolgy",
            "Option3":"C. Healthcare",
            "Option4":"D. Government",
            "Answer":"D",
      },

      {
            "Question":"True or False, Does Wellington have trains?",
            "Option1":"A. True",
            "Option2":"B. False",
            "Option3":"C. N/A",
            "Option4":"D. N/A",
            "Answer":"A",
      },
      
]

pokemon_quiz = [
        {
            "Question": "What is the god of Pokemon?",
            "Option1":"A. Arceus",
            "Option2":"B. Pikachu",
            "Option3":"C. Charizard",
            "Option4":"D. Dragonite",
            "Answer":"A",

      },
      {
            "Question": "Who is the most popular Pokemonm according to a research in 2016??",
            "Option1":"A. Pikachu",
            "Option2":"B. Greninja",
            "Option3":"C. Charizard ",
            "Option4":"D. MewTwo",
            "Answer":"B",
      },
      {
            "Question": "When is the first region in Pokemon?",
            "Option1":"A. Johto",
            "Option2":"B. Hoenn",
            "Option3":"C. Alola",
            "Option4":"D. Kanto",
            "Answer":"D",
            
      },

      {
            "Question":"Whch month did Pokemon come out in??",
            "Option1":"A. March ",
            "Option2":"B. December ",
            "Option3":"C. April",
            "Option4":"D. February ",
            "Answer":"D",

      },
      {
            "Question":"Who is the main character of the Pokemon now?",
            "Option1":"A. Ash",
            "Option2":"B. Goh",
            "Option3":"C. Liko",
            "Option4":"D. Roy",
            "Answer":"C",
      },

      {
            "Question":"True or False, Does Pokmeon have 10 regions?",
            "Option1":"A. True",
            "Option2":"B. False",
            "Option3":"C. N/A",
            "Option4":"D. N/A",
            "Answer":"A",
      }
      ]

countries_quiz = [
        {
            "Question": "Which country has the biggest population?",
            "Option1":"A. India",
            "Option2":"B. China",
            "Option3":"C. USA",
            "Option4":"D. Brazil",
            "Answer":"A",

      },
      {
            "Question": "How many continents in the world?",
            "Option1":"A.3",
            "Option2":"B.10",
            "Option3":"C.12 ",
            "Option4":"D.7",
            "Answer":"D",   
      },
      {
            "Question": "Which country has the higest HDI (Human devlopment index)?",
            "Option1":"A.Burundi",
            "Option2":"B.New Zealand",
            "Option3":"C.Denmark",
            "Option4":"D.Singapore",
            "Answer":"C",
            
      },

      {
            "Question":"When did India get independence?",
            "Option1":"A.  1947",
            "Option2":"B. 1950 ",
            "Option3":"C. 1867",
            "Option4":"D. 1922 ",
            "Answer":"A",

      },
      {
            "Question":"What country has the highest GDP?",
            "Option1":"A. China",
            "Option2":"B. USA",
            "Option3":"C. Singapore",
            "Option4":"D. Japan",
            "Answer":"B",
      },

      {
            "Question":"True or False, the UN recongises over 200 countries?",
            "Option1":"A. True",
            "Option2":"B. False",
            "Option3":"C. N/A",
            "Option4":"D. N/A",
            "Answer":"B",
      }
      ]

# This function gets input from the user.
# If the user types "quit", the program ens sfaely using sys.exit().
# Otherwise, it returnns the users input.
def get_input(prompt):
      choice = input (prompt)
      if choice.lower() == "quit":
            print("Goodbye!")
            sys.exit()
      return choice

#This function prints text slowly tp create dramatic diialogue
def slow_text (text):
       for character in text:
              print(character, end='', flush = True)
              time.sleep (0.03)
       print()

def game_over(name): # Displays the game over screen and resets player health.
      global player_health
      player_health = 100
      slow_text("Oh no! You have run out of health!")
      slow_text("GAME OVER!")
      slow_text("Going to the main menuu ...")
      
#Checks if player loses all health
#Returns True if dead, otherwise False
def check_dead(name):
      if player_health <=0:
            game_over(name)
            return True
      return False

#Controls the Palmerston North area and transitions the player to Kapiti.
def palmerston_north_area(name):
      global player_health
      slow_text("You have finally arrived in Palmerston North!")
      slow_text("Suddenly a person approaches you...")
      slow_text("His name is Ren!")
      slow_text(f"Ren: Welcome {name} to the second area Palmerston North!")
      slow_text("Ren: Come in the car and enjoy the ride down to the Kapiti region!")

      slow_text("The road steches ahead as the city fades away...")
      slow_text("You drive through open fields and winding roads...")
      slow_text("3 hours later...")
      slow_text("Ren said: Welcome to the Kapiti region, your next goal is to get to Te Papa, best of luck!")

      kapiti(name)

# This function controls the jumgle area gameplay
# The player chooses between a safe route or dangerous route.
# Different animals and obstacles affect health and durabililty

def jungle(name):
       global player_health # tells python to use the global variable and also can change the the health.
       player_health = 100
       pickaxe_durability = 0
       for item in jungle_area:
             if item["Name"] == "Wooden Pickaxe":
                   pickaxe_durability = item["Durability"]
       slow_text("You find yourself in a wide jungle with no clue on whats going on.")
       slow_text("Suddenly a man appears from the bushes *John*.")
       slow_text(f"Hello {name} welcome to the jungle")
       slow_text(f"Your goal is to reach to Te Papa in 20 Minutes")
       slow_text("Beware, you will go through many areas, which can hurt you.")
       slow_text("So its up to you, do you want to go to the side which is longer which is safer but with worse  in tools or short route with more animals but better tools!")
       slow_text("1. Safe route, Wooden Pickaxe")
       slow_text("2. The shorter route, Machete ")
       while True:
        route = input("Choose your route: ")
#This if statement checks if a parrot encounter is what its suppose to be for the safe route and if it is then a parrot appears and lowers health. It does this by rolling a random number from 1 to 100 . The user has a chance to defend but lose durabilty or let the parrot attack and lose health.
        if route == "1":
                slow_text("Congrats scaredy cat! Welcome to the safer  but looonger route!")
                for animal in jungle_area:
                    if animal["Name"] == "Parrot":
                            roll = random.randint(1,100) #Random chance for parrot encounter
                            if roll < animal ["Spawnrate_Safe"]:
                                slow_text("A parrot attacks you!")
                                slow_text("You have a choice!")
                                slow_text("1. Fight with your wooden pickaxe.")
                                slow_text("2. Let it attack you.")
                                slow_text(" Or type quit to exit!")
                                parrot_choice = get_input("What do you want?")
                                if parrot_choice == "1":
                                      pickaxe_durability -= random.randint(4,10)
                                      slow_text("You swung your pickaxe at the parrot and it scared it off!")
                                      slow_text(f"Pickaxe durability: {pickaxe_durability} ")
                                elif parrot_choice == "2":
                                      player_health -= random.randint(3,10) # Reduce player healh if attacked
                                      slow_text("The parrot used gust on you!")
                                      slow_text(f"You have {player_health} left, be careful!")
                                      if check_dead(name): return
                                else:
                                      slow_text("Invalid choice!")  
                #This is the second challenge. First the user will have to decide if they want to chop the tree or stay stuck. If they do chop the tree they lose durabilty but if they don't they stay stuck.
                while True:
                      slow_text("A tree is blocking your way!")
                      slow_text("What will you do?")
                      slow_text("1. Chop it with your Wooden Pickaxe")
                      slow_text("2. Try to go around")
                      slow_text(" Or type quit to exit!")
                      action = input("What do you choose?")
                      if action == "1":
                            pickaxe_durability -= 20
                            slow_text(f"You chopped the tree, you may proceed! Pickaxe durability: {pickaxe_durability}")
                            slow_text("You continue across the jungle into the thick undergrowth.")
                            slow_text("Even if the jungle seems endless in its space.")
                            for animal in jungle_area:
                                  if animal ["Name"] == "Parrot":
                                              slow_text("The pesky parrot is back!")
                                              slow_text("1. Fight with your Wooden Pickaxe")
                                              slow_text("2. Let it attack you with gust!")
                                              slow_text(" Or type quit to exit!")
                                              parrot_choice2 = get_input("What do you choose?")
                                              if parrot_choice2 == "1":
                                                    pickaxe_durability -= random.randint(4,10)
                                                    slow_text("You swung the pickaxe and it killed it!")
                                                    slow_text(f"Pickaxe durablilty: {pickaxe_durability}")
                                                    
                                              elif parrot_choice2 == "2":
                                                    player_health -= random.randint(3,10)
                                                    slow_text("The parrot used gust on you!")
                                                    slow_text(f"You have {player_health}")
                                                    if check_dead(name): return
                                                    
                                              else:
                                                    slow_text("Invalid Choice!")
                                                    
                                              slow_text("You go through the undergrowth...")
                                              while True:
                                                    slow_text("A thick bush has been discovered and its blocking your path!")
                                                    slow_text("1. Chop it with your wooden pickaxe.")
                                                    slow_text("2. Try to go around.")
                                                    slow_text(" Or type quit to exit!")
                                                    action2 = input("What do you choose?")
                                                    if action2 =="1":
                                                          pickaxe_durability -= 10
                                                          slow_text(f"Pickaxe Durabilty {pickaxe_durability}")
                                                          break
                                                    elif action2 == "2":
                                                          slow_text("Hmmm that won't work sorry!")
                                                    else:
                                                          slow_text("Invalid input!")
                                              for animal in jungle_area:
                                                      if animal ["Name"] == "Parrot":
                                                                  slow_text("Another parrot has appeared!")
                                                                  slow_text("1. Fight with your Wooden Pickaxe.")
                                                                  slow_text("2. Let it attack you with gust!")
                                                                  slow_text(" Or type quit to exit!")
                                                                  parrot_choice3 = get_input("What will you choose?")
                                                                  if parrot_choice3 == "1":
                                                                        pickaxe_durability -= random.randint (4,10)
                                                                        slow_text("You swung the Pickaxe and it ran away!")
                                                                        slow_text(f"Pickaxe durability: {pickaxe_durability}") 
                                                                        break
                                                                  elif parrot_choice3 == "2":
                                                                        player_health -= 10
                                                                        slow_text("The parrot used gust on you!")
                                                                        slow_text(f"You have {player_health} left be careful!")
                                                                        slow_text("You have finally made it through the jungle!")
                                                                        slow_text("Palmerston North is just ahead!")
                                                                        
                                                                        if check_dead(name):return
                                              palmerston_north_area(name)
                                              break
                            break
                      elif action == "2":
                            slow_text("Hmm try again...")
                      else:
                            slow_text("Invalid choice!")
                
                break 
        elif route == '2':
                slow_text("Congrats vicious warrior! Welcome to the *dangerous* but shorter route!")
                machete_durability = 0
                for item in jungle_area:
                      if item ["Name"] == "Machete":
                            machete_durability = item["Durability"]
                slow_text("The machete has destoyed all the bushes and trees for you thanks to its special ability *destroy all*")
                slow_text("But there is dangerous creatures who can dismantle you, be careful!")
                for animal in jungle_area:
                      if animal["Name"] == "Bear":
                            bear_health = animal["Health"]
                            bear_health -= random.randint(40,50)
                            slow_text("A bear has appeared!")
                            slow_text("1. Attack the bear ")
                            slow_text("2. let the bear attack you")
                            slow_text(" Or type quit to exit!")
                            bear_choice = get_input("What will you choose?")
                            if bear_choice == "1":
                                  slow_text("You sliced the skin of the bear with the sheer force and sharpness of the blade")
                                  slow_text(f"The bear health goes down by 50!")
                                  machete_durability -= random.randint(15,50)
                                  slow_text(f"Machete durability: {machete_durability} ")
                            elif bear_choice == "2":
                                  player_health -= random.randint(20,30) 
                                  slow_text("The bear used Roar and mauled you!")
                                  slow_text(f"You have {player_health} health left!")
                                  if check_dead(name): return 
                            else:
                             slow_text("Invalid choice!")
                for animal in jungle_area:
                      if animal["Name"] == "Bear":
                            slow_text("The bear is ready to fight again!")
                            slow_text("1. Attack the bear")
                            slow_text("2. Let the bear attack you")
                            slow_text(" Or type quit to exit!")
                            bear_choice2 = get_input("What will you choose?")
                            if bear_choice2 == "1":
                                  slow_text("You have finally killed the bear!")
                                  machete_durability -= random.randint(15,50)
                                  slow_text(f"MAchete durability : {machete_durability}")
                            elif bear_choice2 == "2":
                                  player_health -= random.randint(20,30)
                                  slow_text("The bear attacked you again!")
                                  slow_text(f"You have {player_health} health left! ")
                                  if check_dead(name): return
                            else:
                                  slow_text("Invalid input!")
                for animal in jungle_area:
                      if animal ["Name"] == "Parrot":
                            slow_text("A peaky parrot has appeared to attack you!")
                            slow_text("1. Let it attack you")
                            slow_text("2. You attack with Machete")
                            slow_text(" Or type quit to exit!")
                            parrot_choice4 = get_input("What will choose?")
                            if parrot_choice4 == "1":
                                  machete_durability -= random.randint(15,50)
                                  slow_text("The Machete destroyed the parrot")
                                  slow_text(f"Machete Durability: {machete_durability}")
                            elif parrot_choice4 == "2":
                                  player_health -= random.randint(2,3)
                                  slow_text("The parrot used gust!")
                                  slow_text(f"You have {player_health} health left")
                                  if check_dead(name): return
                            else:
                                  slow_text("Invalid choice!")
                for animal in jungle_area:
                      if animal ["Name"] == "Bear":
                            slow_text("Another bear appears!")
                            slow_text("1. Attack the bear")
                            slow_text("2. Let the bear attack you!")
                            slow_text(" Or type quit to exit!")
                            bear_choice3 = get_input("What do you choose?")
                            if bear_choice3 == "1":
                                  slow_text("You hit the bear for 50 health!")
                                  machete_durability -= random.randint(15,50)
                                  slow_text(f"Machete durability: {machete_durability}")
                            elif bear_choice3 == "2":
                                  player_health -= random.randint(20,30)
                                  slow_text("The bear nauled you one more time!")
                                  slow_text(f"You have {player_health} health left!")
                                  if check_dead(name): return
                            else:
                                  slow_text("Invalid choice!")
                for animal in jungle_area:
                      if animal ["Name"]  == "Bear":
                        slow_text("The bear hasnn't given up!")
                        slow_text("1. Attack the bear")
                        slow_text("2. Let the bear attack you!")
                        slow_text(" Or type quit to exit!")
                        bear_choice4 = get_input("What do you choose?")
                        if bear_choice4 == "1":
                            slow_text("You hit the bear for 50 health")
                            machete_durability -= random.randint(15,50)
                            slow_text("The bear is finally dead!")
                            slow_text(f"Machete durability: {machete_durability}.")
                        elif bear_choice4 == "2":
                            player_health -= random.randint(20,30)
                            slow_text("The bear hurt you again!")
                            slow_text(f"You have {player_health} health left")
                            if check_dead(name): return
                        else:
                            slow_text("Invalid Input!")
                        
                            break 
                            
                slow_text("You have survived the dangerous route! Congrats!")
                slow_text("You are ready to move on to Palmerston North")
                palmerston_north_area(name)
                  
                            

                                  
                                  
                break
        else:
            slow_text("Invalid Choice! Please try again!")
            
# Kapiti region gameplay.
# The player must earn at least $55 before travelling to Te Papa.
# Hunting aninals can reward money but may reduce health.
def kapiti(name):
      global player_health
      # Add earned money to total balance
      money = 0
      eagle = next(item for item in kapiti_items if item["Name"] == "Eagle")
      eel = next(item for item in kapiti_items if item["Name"] == "Long Finned Eel")

      slow_text("You arrive in the Kapiti regiom!!!")
      slow_text("Your next goal to get to Te Papa is to earn money!")
      slow_text("To Earn money, you need to try to catch the eagles or the long finned eel which both have random spawnrates!")
      slow_text("If you unable to catch them you lose health!")
      slow_text(" Or type quit to exit!")
      slow_text ("Good Luck!")

      while money <55 and player_health > 0: # Keeps running untill player earns enough money.
                                             # Or loses all health.
             slow_text(f"Current money: ${money}/ $55 needed") #
             slow_text("1. Hunt Long-Finned Eel") # Player chooses to hunt Long-Finned Eel.
                                                  # Random chance determines if eel appears.
             slow_text("2. Hunt Eagle") # Eagle hunting gives more money but is riskier.
             # Because failing can remove more health.
             slow_text("3. Take Bus to Te Papa(only if you got $55+)")

             choice = get_input("What do you choose? ")

             if choice == "1":
                   slow_text("You search for the Long-Finned Eel.")
                   slow_text(" Or type quit to exit!")

                   if random.randint(1,100) < eel ["Spawnrate"]:
                         slow_text("Eel appears")
                         
                         for item in kapiti_items:
                               if item["Name"] == "Long Finned Eel":
                                     base_health = item["Health"]
                         eel = next((item for item in kapiti_items if item["Name"] == "Long Finned Eel"), None)
                         eel_health = random.randint(eel["Health"] -5, eel["Health"] +5)
                         if eel is None:
                              slow_text("No eel data found!")
                              return
                         slow_text("1. Weaken it with a machete!")
                         slow_text("2. Try to catch it directly (risky)")
                         slow_text(" Or type quit to exit!")

                         action = get_input(">")

                         if action == "1":
                               slow_text("You weakened the eel first !")
                               eel_health -= random.randint(10,25)

                               
                               slow_text("Now using the fishing rod!")
                               
                               if eel_health <= 0:
                                     gain = random.randint(5,10)
                                     money += gain
                                     slow_text(f"SUCESS! You earned ${gain}.")
                               else:
                                     if random.randint(1,100) > 50:
                                           gain = random.randint(5,10)
                                           money += gain
                                           slow_text(f"You caught it just in time! +${gain}")
                                     else:
                                           player_health -= 2 
                                           slow_text("It escaped! -2 health!")
                         elif action == "2":
                              if random.randint(1,100) > 70:
                                 gain = random.randint(5,10)
                                 money += gain
                                 slow_text(f"Lucky catch! +${gain}")     
                              else:
                                    player_health -= 2 
                                    slow_text("it slipped away!")                         
                   else:
                        slow_text("No eel found!")


             elif choice =="2":
                   slow_text("You search for the Eagle...")
                   if random.randint(1,100) < next(item for item in kapiti_items if item["Name"] == "Eagle")["Spawnrate"]:
                         slow_text("Eagle appears!")

                         for item in kapiti_items:
                               if item ["Name"] == "Eagle":
                                     base_health = item ["Health"]
                         eagle = next((item for item in kapiti_items if item["Name"] == "Eagle"), None)
                         eagle_health = random.randint(eagle["Health"] -5, eagle["Health"] +5)
                         if eagle is None:
                              slow_text("No eagle data found!")
                              return
                         slow_text("1. Weaken it with Machete!")
                         slow_text("2. Try to catch with fishing rod!")
                         slow_text(" Or type quit to exit!")
                         
                         action = get_input(">")

                         if action == "1":
                               slow_text("You weakened the eagle first !")
                               eagle_health -= random.randint(30,70)

                               
                               slow_text("Now using the fishing rod!")
                               
                               if eagle_health <= 0:
                                     gain = random.randint(15,20)
                                     money += gain
                                     slow_text(f"SUCESS! You earned ${gain}.")
                               else:
                                     if random.randint(1,100) > 60:
                                           gain = random.randint(25,30)
                                           money += gain
                                           slow_text(f"You caught it just in time! +${gain}")
                                     else:
                                           player_health -= 5 
                                           slow_text("It escaped! -5 health!")
                         elif action == "2":
                              if random.randint(1,100) > 40:
                                 gain = random.randint(5,7)
                                 money += gain
                                 slow_text(f"Lucky catch! +${gain}")     
                              else:
                                    player_health -= 2 
                                    slow_text("it slipped away!")                         
                   else:
                        slow_text("No eagle found!")
             elif choice == "3":
                   if money >= 55:
                         slow_text("You have enough money!")   
                         slow_text("You board the bus to Te Papa!")    
                         te_papa(name)
                   else:
                         slow_text(f"You only have ${money}! You need $55!")
      if money >= 55:
        slow_text("You earned enough money!")
        te_papa(name)
      elif player_health <= 0:
        check_dead(name)      
# Runs a quiz ny askign questions and checking answers.
# Returns the players final score.
def run_quiz(questions):
      score = 0
      for question in questions:
            slow_text(question["Question"])
            slow_text(question["Option1"])
            slow_text(question["Option2"])
            slow_text(question["Option3"])
            slow_text(question["Option4"])
            answer = input("Your answer (A/B/C/D):").upper()      
            if answer == question["Answer"]:
                  slow_text("Correct!")
                  score += 1
            else:
                  slow_text(f"Wromg! Answer was {question['Answer']}")
      slow_text(f"You scored {score}/{len(questions)}")      
      return score

# Final area of the game where the player completes the quizes.
# Adds all quiz scores together for a final score.

def te_papa(name): 
      slow_text("Welcome to the final location to the final area of the game!")
      total_score = 0 
      quizzes_done = []

      for round in range (2):
            slow_text(f"Pick quiz {round + 1 } of 2:")
            if "1" not in quizzes_done:
                  slow_text("1. Quiz of Wellington")
            if "2" not in quizzes_done:
                  slow_text("2. Quiz of Pokemon")
            if "3" not in quizzes_done:
                  slow_text("3. Quiz of countries")


            choice = get_input ("Choose:")
            if choice == "1" and "1" not in quizzes_done:
                  total_score += run_quiz(wellington_quiz)
                  quizzes_done.append("1")
            elif choice == "2" and "2" not in quizzes_done:
                  total_score += run_quiz(pokemon_quiz)
                  quizzes_done.append("2")
            elif choice =="3" and "3" not in quizzes_done:
                  total_score += run_quiz(countries_quiz)
                  quizzes_done.append("3")
      
      slow_text(f"Total score: {total_score}/10!")
      slow_text("Congrats! You completed the adventure of Te Papa!")
         
      

 

    
# Main menu of the game.
# Allows player to:
# 1. Start game
# 2. Read instructions
# 3. Exit the program
def main_menu():
    while True: # While True keeps asking until valid input is entered.
        try:
            while True:
                         #Added try and except so if a user puts boolean or string instead of integer
                #It won't crash
               name = (input("What is your name?"))
               if name.isalpha(): # .isaplpha() ensures the user only enters letters.
                   break
               else:
                  slow_text("Please enter letters only!")
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
                    print("\nPress enter to go back to menu")
        elif choice == '3':
                    print("Bye, have a nice day!")
                    sys.exit()#helps to close the program entirely
        else:
            print("Invalid input!")

main_menu()

