# The n^(th) term of the sequence of triangle numbers is given by,
#                    t_(n) = 1/2n(n+1);
# so the first ten triangle numbers are: 
#            1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...  
# By converting each letter in a word to a number corresponding to its
# alphabetical position and # adding these values we form a word value. For 
# example, the word value for SKY is: 19 + 11 + 25 = 55 = t_(10).  If the word
# value is a triangle number then we # shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
# containing nearly two-thousand common English words, how many are triangle
# words?


def tN(n): 
   return int((0.5)*n*(n+1))



f=open("inputs/words.txt","r") 
w=f.read() # puts the file contents as a string 
w=eval(w)  # makes the file contents into a list

# calculate a big old list of triangle numbers
triNums=map(tN,range(1,10001))

# a negative number to be added to ord(letter)
# to make A==1, B==2 etc
offset=1-ord('A') 

# counters
nTriWords=0

# loop over words
for i in range(0,len(w)):
   word=w[i]
   t=0
   
   # calculate current word total==t
   for j in range(0,len(word)):
      t+=(ord(word[j])+offset)

   # is t a triangle number?
   if triNums.count(t)==1:
      nTriWords+=1

print nTriWords
