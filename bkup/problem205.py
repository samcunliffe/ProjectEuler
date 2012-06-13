from fractions import Fraction

peterfrequencies=[0]*17
petercombinations=0
peter=[]
for a in range(1,5):
    for b in range(1,5):
        for c in range(1,5):
            for d in range(1,5):
                peterfrequencies[a+b+c+d]+=1
                peter.append(a+b+c+d)
                petercombinations+=1
                

colinfrequencies=[0]*37
colincombinations=0
colin=[]
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            for d in range(1,7):
                for e in range(1,7):
                    for f in range(1,7):
                        colinfrequencies[a+b+c+d+e+f]+=1
                        colin.append(a+b+c+d+e+f)
                        colincombinations+=1

print 'Counting games'
peterWins=0
totalGames=0
for c in colin:
    for p in peter:
        totalGames+=1
        if (p>c):peterWins+=1

print Fraction(peterWins,totalGames)

print 'Done'
##from random import randint
##
##peterWins=0
##totalGames=0
##
##while True:
##
##    totalGames+=1
##
##    # roll 6 independent 6-sided dice
##    colin=0
##    for i in range(6):
##        colin+=randint(1,6)
##
##    # roll 4 independent 4-sided dice
##    peter=0
##    for i in range(6):
##        peter+=randint(1,6)
##
##    # count winner
##    if (peter>colin):
##        peterWins+=1
##    #elif (colin>peter):
##    #    colinWins+=1
##
##    # calculate peter's probability
##    prob = float(peterWins)/float(totalGames)
##    if totalGames%100000==0:print prob
##
##    
##
