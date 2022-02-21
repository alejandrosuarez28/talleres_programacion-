

a=0
g=0
d=0
while True:
    x=int(input())
    if (x==1):
        a=a+1
        continue
    elif(x==2):
        g=g+1
        continue
    elif(x==3):
        d=d+1
        continue
    elif(x==4):
        break
    elif(x>4):
        print("ingrese nuevo codigo")
        continue
print("alcohol",a,"\ngasolina",g,"\ndiesel",d) 
