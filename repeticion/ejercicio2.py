"""
entradas 

salidas

"""
i=0
l=[]
for i in range(1,101,2):
    if(i%7!=0):
        l.append(i)
        continue
print(l)
