from time import clock
st=clock()

def sqDigitSum(n):
    t=0
    n=str(n)
    for digit in n:
        t+=int(digit)**2
    return t

print 'Calculating number chains'

terminations=[0]*10000000
for i in range(len(terminations)):
    if i%100000==0:print ' '+`i`
    n=i
    go=True
    while go==True:
        n=sqDigitSum(n)
        #print `i`+'  '+`n`
        if n < i:
            terminations[i]=terminations[n]
            go=False
        elif n in [1,10,100,1000,10000,1000000]:
            terminations[i]=1
            go=False
        elif n in [89,145,42,20,4,16,37,58]:
            terminations[i]=89
            go=False
        elif n==0:
            terminations[i]==0
            go=False

print 'Counting 89\'s'
t=0
for val in terminations:
    if val==89:
        t+=1
print t

fn=clock()
print('Time to run %0.3f seconds' % (fn-st))
