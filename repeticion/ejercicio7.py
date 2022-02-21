x=int(input("Ingrese la experencia: "))
m=int(input("Ingrese el valor de la experencia: "))
while True:
    if(m==0 and x==0):
        break
    elif((10<=m<=2**32-1) and ((0<x<=3))):
        z=x*m
    print (z)
    break