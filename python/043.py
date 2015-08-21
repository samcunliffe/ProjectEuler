## SOLVED

from time import clock
st=clock()

def ssdp(p):
    p=str(p)
    if int(p[1:4])%  2==0 and\
       int(p[2:5])%  3==0 and\  # should have ordered 
       int(p[3:6])%  5==0 and\  # other way up for speed
       int(p[4:7])%  7==0 and\
       int(p[5:8])% 11==0 and\
       int(p[6:9])% 13==0 and\
       int(p[7:10])%17==0 :
        return True
    else:
        return False

from itertools import permutations

print 'Searching for 0-9 Pandigitals'
pandigitals=[]

for perm in permutations(range(10)):

    s=''
    for digit in perm:
        s+=str(digit)
            
    pandigital=int(s)
    pandigitals.append(pandigital)

t=0
print 'Summing numbers with property'
for pand in pandigitals:

    if ssdp(pand):
        t+=pand

print t

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
