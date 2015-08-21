
def gcd(u, v):
  """Greatest common denominator by Euclid algorithm"""
  return gcd(v, u % v) if v else abs(u)

def circlularPermutations(n):
  s=str(n)
  l=[]*len(s)
  l.append(n)
  for p in range(1,len(s)):
    u=s[:p]
    v=s[p:]
    l.append(int(v+u))
  return l
