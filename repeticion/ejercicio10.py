l=[]
while True:
    a=float(input("altura:"))
    print("0 para terminar")
    if(a!=0):
        l.append(a)
        l.sort(reverse=True)
        continue
    elif (a==0):
        break
print(l[0])