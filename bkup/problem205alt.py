# pete : x9 four-sided dice
pete=[]
for p1 in range(1,5):
  for p2 in range(1,5):
    for p3 in range(1,5):
      for p4 in range(1,5):
        for p5 in range(1,5):
          for p6 in range(1,5):
            for p7 in range(1,5):
              for p8 in range(1,5):
                for p9 in range(1,5):
                  pete.append(sum([p1,p2,p3,p4,p5,p6,p7,p8,p9]))


# colin : x6 six-sided dice
colin=[]
for c1 in range(1,7):
  for c2 in range(1,7):
    for c3 in range(1,7):
      for c4 in range(1,7):
        for c5 in range(1,7):
          for c6 in range(1,7):
            colin.append(sum([c1,c2,c3,c4,c5,c6]))

games=0
peteWins=0

for p in pete:
  for c in colin:
    games+=1
    if p>c:peteWins+=1

print float(peteWins)/float(games)
