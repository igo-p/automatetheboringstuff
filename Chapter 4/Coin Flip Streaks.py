import random
numberOfStreaks = 0
scores = []
for experimentNumber in range(10000):
    experiment = []
    for spin in range(100):
        if random.randint(0,1) == 0:
            experiment.append('H')
        else:
            experiment.append('T')
    scores.append(experiment)

    for i in range(0,len(experiment)-7):
        if experiment[i] == experiment[i+1] and experiment[i+1] == experiment[i+2] and experiment[i+2] == experiment[i+3] and experiment[i+3] == experiment[i+4] and experiment[i+4] == experiment[i+5] and experiment[i+5] != experiment[i+6]:
            numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100/10000))
