nl=[]
for x in range(700, 3000):
    if (x%7==0) and (x%5==0):
        nl.append(str(x))
print (','.join(nl))
