def rev(n):
    if not n%10: return False
    a = n
    b = 0
    while a:
        b *= 10
        b += a%10
        a /= 10
    s = b+n
    while s:
        if not s%2: return False
        s /= 10
    return True
    

    
from time import clock
start = clock()
print 2*sum(rev(i) for i in range(1,100000000,2)) #608720
stop = clock()
print stop-start
