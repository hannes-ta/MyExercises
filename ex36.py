from sys import exit
import time



def plant_room():
    print "This is your final challenge."
    print "How old is Arnold Schwarzenegger?"
    print "Type a number of course..."
    choice = raw_input("> ")
    if choice >10:
        print "I don't know if thats right but I guess he's pretty old."
        print "You made it!!! Here is your reward:"
        time.sleep(3)
        print "Sorry, but I can't afford a reward."


    else:
        dead("He must be older then 10 God Damn...")

def waiting_room():
    print "You've reached the waiting room, here is another riddle to pass the time:"
    print "What has cities, but no houses; forests, but no trees; and water, but no fish?"

    choice = raw_input("> ")

    if choice == "Map" or choice == "map" or choice == "a map" or choice == "A Map":
        plant_room()
    else:
        print "No thats just so wrong"
        print "But you have infite tries, to pass the time ;)"
        waiting_room()


def fight_room():
    print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"
    print "You enterd the arena and so has Darth Vader"
    print "Now everything depends on your weapon and your moves..."
    print "-+-+-+-+-+-+-+-+-+-+-+-+-+-+-"

    if weapon == 1:
        time.sleep(5)
        print "You have a wooden spoon, that is so cool, inspired by your actions Santa Claus appears"
        print "Santa convinces Vader to let you go, because even that guy likes Christmas."
        plant_room()
    else:
        print "Vader comes running at you, do you try to hit him od do you run to the other side of the arena?"
        print "Type: run or hit"
        choice = raw_input("> ")

        if choice == "run":
            print "You run to another side of the arena"
            print "Vader runs into a wall and tumbles"
            print "Do you use that opportunity?"
            print "Type Yes or No"
            choice_2 = raw_input("> ")
            if choice_2 == "Yes" and weapon == 3:
                print "You run after Vader and hit him multiple times, he falls down and you can flee"
                plant.room()
            if choice_2 == "Yes" and weapon == 2:
                print "You run after Vader but your obvious Lightsaber fails and he kills you"
                dead("Obvious Choice remeber...")
            if choice_2 == "No":
                print "Vader recovers and charges at you, he kills you."
                print "But it's okay I'll let you start again."
                fight_room()
            else:
                print "What, how did we end up here?"
                fight_room()

        if choice == "hit" and weapon == 2:
            print "You take out your lightsaber and try to hit Vader, but it doesn't even light up."
            print "Do you throw it at him?"
            print "Yes or No"
            choice_3 = raw_input("> ")
            if choice_3 == "Yes":
                print "It hits him in the face and you can run away."
                plant_room()
            if choice_3 == "No":
                print "Why not, everybody likes throwing!"
                print "But don't cry you can start again"
                fight_room()
        if choice == "hit" and weapon == 3:
            print "Baam right on the head. Vader falls to the Ground."
            print "You finally got that bastard!"
            plant_room()
            

        else:
            print "No, wrong wrong wrong wrong wrong wrong"
            time.sleep(2)
            print "Still WRONG!"
            time.sleep(1)
            print "But Okay..."
            fight_room()



def vader_awake():
    global weapon
    print "Nice, with all that girly screaming you woke up Vader again"
    print "You'll have to fight him again. "
    print "Choose your weapon:"
    print "a wooden spoon"
    print "a lightsaber"
    print "my fists"

    while True:
        choice = raw_input("> ")

        if choice == "a wooden spoon":
            print "Very brave, I would not have picked a spoon, but sure, your choice."
            weapon=1
            fight_room()
        elif choice == "a lightsaber":
            print "Obvious choice I guess"
            weapon=2
            fight_room()
        elif choice == "my fists":
            print "Who do you think you are? But okay, it's a free country."
            weapon=3
            fight_room()
        else:
            print "Only the wepons I suggested you cheater."




def dark_room():
    print "You're in a really dark room and can't see shit."
    print "What do you do?"
    print "Here are your options:"
    print "Turn on the lights"
    print "Keep going in one direction"
    print "Go to sleep"
    print "Call for help again"

    while True:
        choice = raw_input("> ")

        if choice == "Turn on the lights":
            print "That's way to obvious, havent you learned anything?"
            dead("I don't really care what happened, but")
        elif choice == "Keep going in one direction":
            waiting_room()
        elif choice == "Go to sleep":
            print "Always a Good Idea! You wake up 3 days later..."
            print "But why the hell should have anything happend if you sleep?"
            dark_room()
        elif choice == "Call for help again":
            vader_awake()
        else:
            print "I got no idea what that means, is it really that hard?"


def r2d2_room():
    print "R2D2 appears, what do you tell him to do?"
    print "Do you tell him to shock Vader?"
    print "Or do you tell him to set Vader on fire?"

    while True:
        choice = raw_input("> ")

        if choice == "shock Vader":
            print "R2D2 shocks vader and he starts snoring, you can move on"
            riddle_room()
        elif choice == "set Vader on fire":
            dead("R2D2 drops the light and everything explodes.")
        else:
            print "I got no idea what that means, is it really that hard?"



def vader_room():
    print "The door opens in a big burst of smoke!"
    print "The Imperial March makes your ears ring."
    print "Darth Vader steps out and looks real evil."
    print "Will you run away?"
    print "Will you call for help?"
    print "Or will you kick him in the chest"

    while True:
        choice = raw_input("> ")

        if choice == "run away":
            start_again("Running away never helped anybody, unless it's a rhino, then its ok")
        elif choice == "call for help":
            r2d2_room()
        elif choice == "kick him in the chest":
            import random
            if random.random() <= .5:
                dead("Darth Vader lightsabers you to death, so")
            else:
                print "You disable the vader thingy and he runs out of air and falls asleep"
                print "Guess he should have cheked out that asthma at the doctors"
                print "You can move on"
                print "---------------------------"
                riddle_room()
        else:
            print "I got no idea what that means, is it really that hard?"


def riddle_room():
    print "Welcome to the riddle room"
    print "To get through here you have to solve the following riddle:"
    print "Feed me and I live, yet give me a drink and I die. What am I?"

    choice = raw_input("> ")

    if choice == "Fire" or choice == "fire":
        dark_room()
    else:
        print "No thats just so wrong"
        print "You have one more chance"
        riddle_room_2()

def riddle_room_2():
    print "---------------------------"
    print "Welcome to the riddle room again"
    print "To get through here you still have to solve this riddle:"
    print "Feed me and I live, yet give me a drink and I die. What am I?"

    choice = raw_input("> ")

    if choice == "Fire" or choice == "fire":
        dark_room()
    else:
        print "No thats the end now"



def dead(why):
    print why, "You're Dead, Not a God Job."
    exit(0)

def start():
    print "-----------------------------------"
    print "Welcome to the Crazy Doors Game"
    print "One rule: Type all options exactly as I typed them"
    print "Because this is the Terminal and there is no space for fun and that sort of stuff, ok?!"
    print "Now go and have fun, or well whatever."
    print "-----------------------------------"
    print "You are in a room with three doors."
    print "They all look the same."
    print "All doors are unlocked and you can pick either one."
    print "Which one will it be?"

    choice = raw_input("> ")

    if choice == "1":
        dead("Who picks the first door? Idiot.")
    elif choice == "2":
        vader_room()
    elif choice == "3":
        riddle_room()
    else:
        dead("You already failed that part... It's a freakin number between 1-3.")

def start_again(why):
    print why
    print "You are in a room with three doors again."
    print "They all still look the same."
    print "All doors are still unlocked and you can pick either one."
    print "Which one will it be? Don't disappoint now..."

    choice = raw_input("> ")

    if choice == "1":
        dead("Who picks the first door? Idiot.")
    elif choice == "2":
        vader_room()
    elif choice == "3":
        riddle_room()
    else:
        dead("You already failed that part...")

start()
