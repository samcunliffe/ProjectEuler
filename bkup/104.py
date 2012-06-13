# don't worry, python will cope with massive integers

def first9(n):
  s=str(n)
  if len(s)<9:
    return n
  else:
    return int( s[:9] )

def last9(n):
  s=str(n)
  if len(s)<9:
    return n
  else:
    return int( s[-9:] )

def isPandigital(n):
  s=str(n)
  t=[False]*9
  for digit in s:
    if digit in map(str,range(9)):
      t[int(digit)]=True
  if t==[True]*9:
    return True
  else:
    return False






n,fnminus1,fnminus2=3,1,1

while 1:
  #generate nth Fibonacci
  fn=fnminus1+fnminus2

  #analyse digits
  if isPandigital(first9(fn)) and isPandigital(last9(fn)):
    print n
    break

  #move the Fibonaccis
  n+=1
  fnminus2=fnminus1
  fnminus1=fn
  
