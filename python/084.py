# list names of all squares
# on the monopoly board
names=['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL',
   'C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP',
   'E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J',
   'G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

probs=[]

# match naive probabilities
# to name of each square
for squareName in names:
    probs.append([squareName, 100./len(names)])



# account for the 'Go to Jail'

# move this probability to Jail
probs[10][1]+=probs[30][1]
# clear the G2J probability
probs[30][1]=0


# account for the 3 rolls double rule

n=6
# chance of roling any pair on
# two n-sided dice
rollPair=1./n
# roll three pairs in a row
rollThreePair=1./(n**3)
# move the roll three pair probabilities
# from all squares onto Jail
for i in range(len(probs)):
    probs[10][1]+=probs[i][1]*rollThreePair
    probs[i][1]-=probs[i][1]*rollThreePair


# account for Community Chest cards

# one 'Advance to Go' card /16
probs[0][1]+=probs[2][1]/16.
probs[0][1]+=probs[17][1]/16.
probs[0][1]+=probs[33][1]/16.
# one 'Go to Jail' card /16
probs[10][1]+=probs[2][1]/16.
probs[10][1]+=probs[17][1]/16.
probs[10][1]+=probs[33][1]/16.
# remove the leftover Comunity
# Chest probabilities
probs[2][1]-=probs[2][1]*2./16
probs[17][1]-=probs[17][1]*2./16
probs[33][1]-=probs[33][1]*2./16


