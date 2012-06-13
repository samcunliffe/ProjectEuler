def reverse(n):
    return int(str(n)[::-1])

def isOddDigits(n):
    for digit in set(str(n)):
        if digit in ['2','4','6','8','0']:
            return False
    else:return True

def isReversable(n):
    if str(n)[-1]=='0':
        return False
    return isOddDigits(n+reverse(n))

t=0
print '1 to 1E6'
for n in range(1,1000000):
    if isReversable(n):t+=1
print t

print '1E6 to 1E7'
for n in range(1000000,10000000):
    if isReversable(n):t+=1
print t

print '1E7 to 1E8'
for n in range(10000000,100000000):
    if isReversable(n):t+=1
print t

print '1E8 to 1E9'
for n in range(100000000,1000000000):
    if isReversable(n):t+=1
print t
