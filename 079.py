## SOLVED
## Combination of this code and pen+paper inspection
## of text file. Written logic is in file 'problem79.jpg'
#
#
# Project Euler Problem 79
# ========================
# A common security method used for online banking
# is to ask the user for three random characters
# from a passcode. For example, if the passcode was
# 531278, they may ask for the 2nd, 3rd, and 5th
# characters; the expected reply would be: 317.
# 
# The text file, keylog.txt, contains fifty
# successful login attempts.
# 
# Given that the three characters are always asked
# for in order, analyse the file so as to determine
# the shortest possible secret passcode of unknown
# length.

data=open('problem79data.txt','r')
datalist=[]

# find all possible digits
possibleDigits=set()
for line in data:
    datalist.append(line)
    for digit in line:
        possibleDigits.add(digit)

possibleDigits=list(possibleDigits)
possibleDigits.sort()
possibleDigits.remove('\n')
print possibleDigits

# assume all digits are used once and only once
shortestCodeLength=len(possibleDigits)

# list all digits that appear in second or third place
# the digit that is never second or third must come first
# and the digit that is never third must come second
secondAndThird=set()
thirdOnly=set()
for line in datalist:
    secondAndThird.add(line[1])
    secondAndThird.add(line[2])
    thirdOnly.add(line[2])

secondAndThird=list(secondAndThird)
secondAndThird.sort()

thirdOnly=list(thirdOnly)
thirdOnly.sort()

print secondAndThird
print thirdOnly
passcode=['*']*shortestCodeLength

for entry in possibleDigits:
    if (entry not in secondAndThird):
        passcode[0]=entry
        print 'First character is ', entry
for entry in possibleDigits:        
    if (entry not in thirdOnly) and (entry not in passcode):
        passcode[1]=entry
        print 'Second character is ',entry

# the character only ever in third place must be
# the last
firstAndSecond=set()
for line in datalist:
    firstAndSecond.add(line[0])
    firstAndSecond.add(line[1])

firstAndSecond=list(firstAndSecond)
firstAndSecond.sort()

print firstAndSecond

for entry in possibleDigits:
    if (entry not in firstAndSecond) and (entry not in passcode):
        passcode[-1]=entry
        print 'Last character is ',entry  


# report final code as a string to paste into Project Euler
s=''
for digit in passcode:
    s+=digit
print ''
print s
