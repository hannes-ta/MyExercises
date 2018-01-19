class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
plane_crash = Scene("You slowly open your Eyes", "plane_crash",
"""
It's the year 2068
You're the only survivor of a hyproplane crash.
And as if that wouldnt suck enough by itself, your plane crashed next to Area 52 (abandoned since 2021).
You remember that there was some kind of nuclear alien accident thingy here in 2019.
With that on your mind you free yourself from your seat in the cockpit of the plane.
Was it you who crashed this plane? You don't remember...

As you climb out of the hypros broken skylight you take a first glance at your sorroundings.
The Sun is blocked by thick dark vapor that limits your sight to about 30 feet.
You can make out a moving scheme in the distance, its fairly big and coming towards you.
Do you hide back in the plane, find something to fight with or do you call for help?
""")

plane_crash_death = Scene("You slowly open your Eyes", "plane_crash_death",
"""
Really?
At a black scheme in the distance? I really dont know what to say.
The scheme launches at you and suddenly teh whole plane is surrounded.
A freakishly high sound starts to surround you.
Your brain explodes!
Slowly you die... without a brain, kinda fits...
""")

plane_crash_death2 = Scene("You slowly open your Eyes", "plane_crash_death2",
"""
You quickly climb back into the cockpit.
Suddenly the world arround you gets darker and darker.
A freakishly high sound starts to surround you.
Your brain explodes.
Like Boom... You're just dead.
""")

outside_plane = Scene("Outside The Plane", "outside_plane",
"""
You quickly dodge back into the plane to find something to fight with.
You remeber that you were flying this plane for a secret mission.
There should be some kind of weaponary in the cargo bay...
After about 10min you find a huge quatronblaster, stylishly in silver chrome style.
You run out of the escape hatch in the back ready to fire.
The black scheme is gone.

The area arround your plane looks weirdly burned down.
You still cant see a lot.
You notice a weird smell, kind of like rotten fish.
You decide that you'll somehow have to get out of this area.
In the back of the plane is a survival kit that you can take with you.
You also find a comunication device, which is quite heavy.
Sadly you do not have enough strenght to carry both these items and your weapon.
Which one will you leave behind?
""")

outside_plane_death = Scene("Outside The Plane", "outside_plane_death",
"""
No survival without a survival kit.
You'll die.
""")

the_hike = Scene("Good Choice!", "the_hike",
"""
Well I guess it won't be fun but we all have to make due with what we have.
At least you were smart enough to keep the survival kit.
It's time to go for a hike!

After going north for three hours you find an abandoned military base.
You can see a hangar and an old landing strip.
Even further in the distance you see a high tower with a green glow at the top
Because hiking in these conditions is quite tidious
You'll have to make a decision:
1. Go check out the hangar
2. Go check out the tower
3. Continue hiking north towards the border
""")

the_hike_death = Scene("No No No No", "the_hike_death",
"""
The hike is so long that YOU DIE OUT OF EXHASUTION.
""")

hangar = Scene("The Hangar", "hangar",
"""
You go towards the hangar
The building looks extremely run down
Surprisingly the door is still locked with a huge lock
Amazingly it is a combination lock, you'll have to try to crack it
It's a two digit lock with numbers between 1 and 5...
""")
inside_hangar = Scene("Inside the Hangar","inside_hangar",
"""
The hangar door opens, its completely dark inside.
You stumbe through the door and fall down a huge cliff
Well no way to survive that...
Surprising as it is, you're dead. (Sorry this one was mean...)
Nah im not really sorry
""")

tower = Scene("The Tower", "tower",
"""
You get closer and closer to the tower.
The green glow gets more and more intese.
The smell of fish also gets stronger and stronger.
Soon you find yourself at the bottom of the tower.
You see a staircase, it leads either up or down.
Which way do you want to go?
""")

aliens = Scene("Up in the Tower", "aliens",
"""
Up Up Up we go!
The higher up we go the greener everything gets.
You enter the top floor through a green door...
There are three aliens casualy having coffee at a green table.
They ask you to join them.
Do you accept their offer or run away?
""")

win = Scene("You won at life!", "win",
"""
You have green alien coffee with the aliens.
You start to turn green and the aliens accept you as one of their own.
Once the cup is empty they take you to their planet.
I hope thats kinda a cool ending for you. Cause its the end.
""")

the_end_loser2 = Scene("...", "the_end_loser2",
"""
The aliens are very offended.
You try to run, but they control your mind and moves.
You jump off the tower and die...
Painfully.
""")

the_end_loser = Scene("...", "the_end_loser",
"""
Down Down Down we go!
But the stairs are very slippery.
You slip and break your neck..
Crack.
""")

generic_death = Scene("Death...", "death", "You died. You idiot.")

# Define the action commands available in each scene
tower.add_paths({
    'up': aliens,
    'down': the_end_loser
})

the_hike.add_paths({
    'Go check out the hangar': hangar,
    'Go check out the tower': tower,
    'Continue hiking north towards the border': the_hike_death
})

outside_plane.add_paths({
    'comunication device'or 'weapon': the_hike,
    'survival kit': outside_plane_death,

})

plane_crash.add_paths({
    'hide back in the plane':plane_crash_death2,
    'find something to fight with':outside_plane,
    'call for help': plane_crash_death
})

hangar.add_paths({
    '15'or'69'or'34':inside_hangar,
    '*':generic_death,
})
inside_hangar.add_paths({
    '*':generic_death,
})

aliens.add_paths({
    'accept':win,
    'run away':the_end_loser,
})

# Make some useful variables to be used in the web application
SCENES = {
    plane_crash.urlname : plane_crash,
    outside_plane.urlname : outside_plane,
    the_hike.urlname : the_hike,
    inside_hangar.urlname : inside_hangar,
    tower.urlname : tower,
    win.urlname : win,
    hangar.urlname : hangar,
    the_end_loser.urlname : the_end_loser,
    the_end_loser2.urlname : the_end_loser2,
    generic_death.urlname : generic_death,
    plane_crash_death.urlname: plane_crash_death,
    plane_crash_death2.urlname: plane_crash_death2,
    the_hike_death.urlname: the_hike_death
}
START = plane_crash