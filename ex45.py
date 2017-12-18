from sys import exit
from random import randint
import time

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. Idiot.",
        "Try thinking the next time...",
        "Maybe you should stop playing this",
        "My coffee thinks faster then you"
        "Toast is smarter god damnit"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)


class PlaneCrash(Scene):

    def enter(self):
        print "It's the year 2068"
        print "You're the only survivor of a hyproplane crash."
        print "And as if that wouldnt suck enough by itself, your plane crashed next to Area 52 (abandoned since 2021)."
        print "You remember that there was some kind of nuclear alien accident thingy here in 2019"
        print "With that on your mind you free yourself from your seat in the cockpit of the plane"
        print "Was it you who crashed this plane? You don't remember..."
        print "\n"
        print "As you climb out of the hypros broken skylight you take a first glance at your sorroundings "
        print "The Sun is blocked by thick dark vapor that limits your sight to about 30 feet"
        print "You can make out a moving scheme in the distance, its fairly big and coming towards you"
        print "Do you hide back in the plane, find something to fight with or do you call for help?"

        action = raw_input("> ")

        if action == "hide back in the plane":
            print "You quickly climb back into the cockpit"
            print "Suddenly the world arround you gets darker and darker"
            print "A freakishly high sound starts to surround you"
            print "Your brain explodes"
            print "Like Boom... You're just dead."
            return 'death'

        elif action == "find something to fight with":
            print "You quickly dodge back into the plane to find something to fight with"
            print "You remeber that you were flying this plane for a secret mission"
            print "There should be some kind of weaponary in the cargo bay..."
            print "After about 10min you find a huge quatronblaster, stylishly in silver chrome style"
            print "You run out of the escape hatch in the back ready to fire"
            print "The black scheme is gone"
            return 'outside_plane'

        elif action == "call for help":
            print "Really?"
            print "At a black scheme in the distance? I really dont know what to say"
            print "The scheme launches at you and suddenly teh whole plane is surrounded"
            print "A freakishly high sound starts to surround you"
            print "Your brain explodes"
            print "Slowly you die... without a brain, kinda fits..."
            return 'death'

        else:
            print "Learn how to read and type"
            return 'plane_crash'


class OutsidePlane(Scene):

    def enter(self):
        print "The area arround your plane looks weirdly burned down"
        print "You still cant see a lot"
        print "You notice a weird smell, kind of like rotten fish"
        print "You decide that you'll somehow have to get out of this area"
        print "In the back of the plane is a survival kit that you can take with you"
        print "You also find a comunication device, which is quite heavy."
        print "Sadly you do not have enough strenght to carry both these items and your weapon."
        print "Which one will you leave behind?"
        action = raw_input("> ")

        if action == "comunication device" or action == "weapon":
            print "Well I guess it won't be fun but we all have to make due with what we have."
            print "At least you were smart enough to keep the survival kit."
            print "It's time to go for a hike!"
            return 'the_hike'
        elif action == "survival kit":
            print "No survival without a survival kit."
            return 'death'
        else:
            print "Nope wrong, try again."
            return 'outside_plane'



class Hike(Scene):

    def enter(self):
        print "After going north for three hours you find an abandoned military base."
        print "You can see a hangar and an old landing strip."
        print "Even further in the distance you see a high tower with a green glow at the top"
        print "Because hiking in these conditions is quite tidious"
        print "You'll have to make a decision:"
        print "1. Go check out the hangar"
        print "2. Go check out the tower"
        print "3. Continue hiking north towards the border"



        action = raw_input("> ")

        if action == "1" or action == "hangar" or action == "Go check out the hangar":
            print "You go towards the hangar"
            print "The building looks extremely run down"
            print "Surprisingly the door is still locked with a huge lock"
            print "Amazingly it is a combination lock, you'll have to try to crack it"
            print "It's a two digit lock with numbers between 1 and 5..."
            code = "%d%d" % (randint(1,5), randint(1,5))
            guess = raw_input("[Lock]> ")
            guesses = 0

            while guess != code and guesses < 10:
                print "Nothing happens..."
                guesses += 1
                guess = raw_input("[Lock]> ")

                if guess == code:
                    print "The hangar door opens, its completely dark inside."
                    print "You stumbe through the door and fall down a huge cliff"
                    print "Well no way to survive that..."
                    print "Surprising as it is, you're dead. (Sorry this on was mean...)"
                    print "Nah im not really sorry"
                    return 'death'

                else:
                    print "You give up and decide"
                    print "to check out the tower instead, maybe it's not locked"
                    return 'tower'

        elif action == "2" or action == "tower" or action == "Go check out the tower":
            return 'tower'

        elif action == "3" or action == "hiking" or action == "Continue hiking north towards the border":
            print "You start hiking again towards the north"
            print "1 hour passes..."
            print "..."
            time.sleep(2)
            print "1 hour passes..."
            print "..."
            time.sleep(2)
            print "1 hour passes..."
            print "..."
            time.sleep(2)
            print "1 hour passes..."
            print "..."
            time.sleep(2)
            print "And finally:"
            time.sleep(2)
            print "You die out of exhaustion."
            return 'death'


        else:
            print "WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! WRONG! "
            return "the_hike"



class Tower(Scene):

    def enter(self):
        print "You get closer and closer to the tower"
        print "The green glow gets more and more intese"
        print "The smell of fish also gets stronger and stronger"
        print "Soon you find yourself at the bottom of the tower"
        print "You see a staircase, it leads either up or down"
        print "Which way do you want to go?"

        action = raw_input("> ")

        if action == "up":
            return 'aliens'


        elif action == "down":
            print "Down Down Down we go!"
            print "But the stairs are very slippery"
            print "You slip and break your neck.."
            print "Crack."
            return 'death'

        else:
            print "You stare at the door and die for not deciding"
            return 'death'

class Aliens(Scene):

    def enter(self):
        print "Up Up Up we go!"
        print "The higher up we go the greener everything gets"
        print "You enter the top floor through a green door..."
        print "There are three aliens casualy having coffee at a green table"
        print "They ask you to join them"
        print "do you accept their offer or run away?"

        action = raw_input("> ")

        if action == "accept":
            print "You have green alien coffee with the aliens"
            print "You start to turn green and the aliens accept you as one of their own"
            print "Once the cup is empty they take you to their planet"
            return 'finished'

        elif action == "run away":
            print "The aliens are very offended"
            print "You try to run, but they control your mind and moves"
            print "You jump off the tower and die..."
            return 'death'



class Finished(Scene):

    def enter(self):
        print "I don't know if you like what you got, but at least you got out alive ;)"
        return 'finished'


class Map(object):

    scenes = {
        'plane_crash': PlaneCrash(),
        'outside_plane': OutsidePlane(),
        'the_hike': Hike(),
        'tower': Tower(),
        'aliens': Aliens(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('plane_crash')
a_game = Engine(a_map)
a_game.play()
