# A litle age game 
import random 
import time
import pyfiglet 

def play_game_level_1():
    games_value = random.randint(1,10)
    users_value = int(input("I have a number in my memory between 1 and 10, can you try and gues it? "))
    if users_value == games_value:
        return "Awesome, thats Great!! You found it"
    else:
        return "Thats not the one I had chosen  " + str(games_value)
    
def play_game_level_2():
    games_value = random.randint(1,100)
    users_value = int(input("I have a number in my memory between 1 and 100, can you try and gues it? "))
    if users_value == games_value:
        return "Awesome, thats Great!! You found it"
    else:
        return "Thats not the one I had chosen  " + str(games_value)
    
def play_game_level_3():
    games_value = random.randint(1,150)
    users_value = int(input("I have a number in my memory between 1 and 150, can you try and gues it? "))
    if users_value == games_value:
        return "Awesome, thats Great!! You found it"
    else:
        return "Thats not the one I had chosen  " + str(games_value)
    
def banner():
    print("Guesing Game ")
    time.sleep(0.2)
    print("Which level would you like to play ")
    time.sleep(0.2)
    print("\n[1]. Easy \n[2]. Medium \n[3]. Hard ")
    level = int(input("Chose from the list above "))
    
    if level == 1:
        print(play_game_level_1())
    elif level == 2 :
        print(play_game_level_2())
        
    elif level == 3:
        print(play_game_level_3())
    else:     
        print("You did not follow the instructions, lets try again ")
        banner()
    
if __name__ == "__main__":
    print(pyfiglet.figlet_format("Guesing Game"))
    age = int(input("Hello, welcome to my guesing game, how old are you?"))
    if age > 56:
        print(" That too old for this game, try candy crush instead :V ")
    elif age < 5:
        print(" Shouldn't you be watching Anime instead ^_^")
    else:    
        banner()
    