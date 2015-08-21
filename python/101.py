
def isreversable(n):
  s=str(n)
  

  #### some shortcuts ####

  if s[-1]=='0':
    # if the number ends in zero
    return False
  if s[0]==s[-1]:
    # if the first and last digits are equal
    # will produce an even digit
    return False
  if int(s[0])%2==0 and int(s[-1])%2==0:
    # if the first and last digits are even
    # will produce an even digit
    return False
  if int(s[-1])<int(s[0]):
    # have already counted the pair of this
    # number... will need to double the counted
    return False

  if len(s)==9:
    # no nine-digit numbers are reversable
    return False

  #### actual reversable test ####

  # add number to its reverse
  t=n + int(s[::-1])

  # check each digit
  for i in str(t):
    if i in ['0','2','4','6','8']:
      return False

  return True



count=0
i=10 # there are no single digit reversables

while 1:

  if isreversable(i):
    count+=1
  
  if i%10000000==0: print i  
  
  if i==1000000000:
    break

  i+=1

print 2*count
