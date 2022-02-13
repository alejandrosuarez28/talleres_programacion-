"""
datos de entrada 
    cantidad de km-->km-->float 
datos de salida
    precio-->p-->int
"""
#entradas
km=float(input("diguite la cantidad de kilometros recorridosn "))
#caja negra 
p=""
if(km<=300):
    p=50000
elif(300<km<=1000):
    p=70000+(30000*(km-300))
else:
    p=150000+(9000*(km-1000))
#salidas
print("el precio es:", p)
