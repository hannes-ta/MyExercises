from random import randint
import time

class Enemy():
    def __init__(self,health):
        self.health = health

class SithTrooper(Enemy):
    def strike(self,other):
        other.health -= randint(0,12)

sith1 = SithTrooper(1000)
sith2 = SithTrooper(1000)

while sith1.health > 0 and sith2.health > 0:
    sith1.strike(sith2)
    print "--------------------------"
    print "Angela Merkel health: %d" %sith2.health
    sith2.strike(sith1)
    print "Horst Seehofer health: %d" %sith1.health
    time.sleep(0.5)



if sith1.health > sith2.health:
    print "Sadly Horst Seehofer won!"
else: print "Angela Merkel won!"
