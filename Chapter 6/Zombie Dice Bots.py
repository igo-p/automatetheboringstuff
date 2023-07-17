import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        shotguns = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']

            if self.name == 'My Zombie Bot':
                if brains < 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    #print(self.name)
                    break
            elif self.name == 'Roll and maybe stop': # Bot that after first roll randomly decides if it will continue or stop
                if random.randint(0,1) == 1:
                    diceRollResults = zombiedice.roll()
                else:
                    #print(self.name)
                    break
            elif self.name == 'Two brains and stop': # Bot that stops rolling after it has rolled two brains
                if brains >= 2:
                    #print(self.name)
                    break
                else:
                    diceRollResults = zombiedice.roll()
            elif self.name == 'Two shotguns and stop': # Bot thta stops rolling after it has rolled two shotguns
                if shotguns >= 2:
                    #print(self.name)
                    break
                else:
                    diceRollResults = zombiedice.roll()
            elif self.name == 'One to four rolls but chicken if two shotguns':
                rolls = random.randint(1,4)
                for i in range(rolls):
                    if shotguns >= 2:
                        #print(self.name)
                        break
                    else:
                        diceRollResults = zombiedice.roll()
                break
            elif self.name == 'Stop when more shotguns than brains':
                if shotguns > brains:
                    #print(self.name)
                    break
                else:
                    diceRollResults = zombiedice.roll()

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    MyZombie(name='Roll and maybe stop'),
    MyZombie(name='Two brains and stop'),
    MyZombie(name='Two shotguns and stop'),
    MyZombie(name='One to four rolls but chicken if two shotguns'),
    MyZombie(name='Stop when more shotguns than brains')
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)