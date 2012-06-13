data=open('problem59data.txt','r')
for line in data:
    l=eval('['+str(line)+']')

c=range(ord('a'),ord('z')+1)

atoz=map(chr,c)

def searchFor(l,word):
    i=0
    t=0
    for ascii in l:
        if chr(ascii)==word[i]:
            i+=1
            if i==len(word):
                t+=1
                i=0
        elif i>0:
            i=0
    return t

def readable(l):
    '''Converts a list of ascii integers to prose'''
    s=''
    for entry in l:
        s+=chr(entry)
    return s
    


from time import clock
st=clock()

for first in c:
    for second in c:
        for third in c:
            key=[first,second,third]
            keyPlace=0
            g=[]
            for coded in l:
                uncoded=coded^key[keyPlace]
                g.append(uncoded)
                keyPlace+=1

                # resets position in key

                if keyPlace==3:keyPlace=0

            if searchFor(g,'and')>4:
                if searchFor(g,'the')>4:
                    if searchFor(g,'of')>2:
                        ##if searchFor(g,'that')>2:
                            ##if searchFor(g,'from')>2:
                               ##if searchFor(g, 'Project Euler')>0:
                                    print readable(g)
                                    print key
                                    KEY=key

fn=clock()
print('Time to run brute force decoder: %0.3f seconds' % (fn-st))

keyPlace=0
g=[]
for coded in l:
    uncoded=coded^KEY[keyPlace]
    g.append(uncoded)
    keyPlace+=1

    # resets position in key
    if keyPlace==3:keyPlace=0
  
t=0
for entry in g:
    t+=entry
print t
fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
