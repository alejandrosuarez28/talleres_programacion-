"""
datos de entrada 
    lectua anterior-->la-->float 
    lectura actual-->lA-->float 
datos de salida
    precio de factura-->p-->float 
"""
#entradas
la=float(input("diguite la lectura actual"))
lA=float(input("diguite la lectura anterior"))
#caja negra
l=lA-la
pkw=""
if(0<l<=100):
    pkw=4600
elif(100<l<=300):
    pkw=80000
elif(300<l<=500):
    pkw=10000
elif(500<l):
    pkw=120000
p=l*pkw
#salidas
print("el precio total es: ",p)
