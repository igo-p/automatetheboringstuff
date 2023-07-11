import random
# I decided to move 'numberOfStreaks' variable inside the loop to prevent stacking across experimentNumbers
singleFlipGameChance = []
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    flips = random.choices(['H','T'],k=100)
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    counter = 0 #counter of consecutive same flips
    previousResult = None 
    numberOfStreaks = 0 #number of streaks in a given game with 100 flips
    for result in flips:
        if result == previousResult:
            counter += 1
        else:
            counter = 1

        if counter == 6:
            numberOfStreaks += 1
        
        previousResult = result
    singleFlipGameChance.append(numberOfStreaks/100) # share of streaks in a single game with 100 flips

averageStreakChace = (sum(singleFlipGameChance) / len(singleFlipGameChance))*100

print('Chance of streak: {:.2f}%'.format(averageStreakChace))