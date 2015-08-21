# pete
# 9 x 4-sided
pete=[]
pyrimidal=[1,2,3,4]
for p1 in pyrimidal:
  for p2 in pyrimidal:
    for p3 in pyrimidal:
      for p4 in pyrimidal:
        for p5 in pyrimidal:
          for p6 in pyrimidal:
            for p7 in pyrimidal:
              for p8 in pyrimidal:
                for p9 in pyrimidal:
                  pete.append(sum([p1,p2,p3,p4,p5,p6,p7,p8,p9]))


# colin
# 6 x 6-sided
colin=[]
cubic=[1,2,3,4,5,6]
for c1 in cubic:
  for c2 in cubic:
    for c3 in cubic:
      for c4 in cubic:
        for c5 in cubic:
          for c6 in cubic:
            colin.append(sum([c1,c2,c3,c4,c5,c6]))

P=0
for c in colin:
  for p in pete:
    if p>c:P+=1

print float(P)/(len(colin)*len(pete))
