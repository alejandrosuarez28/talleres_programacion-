"""
datos de entrada 
    nombre del cliente-->nc-->str
    monto producto-->mp-->float 
datos de salida
    nombre del cliente-->nc-->str
    monto producto-->mp-->float 
    monto final-->mf-->float 
    descuento-->d-->float 
"""
#entradas
nc=str(input("diguite el nombre del cliente "))
mp=float(input("diguite el monto del producto"))
#caja negra
pd=""
if(mp<=50000):
    pd=0
elif(50000<mp<=100000):
    pd=0.05
elif(100000<mp<=700000):
    pd=0.11
elif(700000<mp<=1500000):
    pd=0.18
else:
    pd=0.25
d=mp*pd
mf=mp-d
#salidas
print("el nombre del cliente es:",nc)
print("el monto del producto es:",mp)
print("el monto a pagar es:",mf)
print("el descuento es:",d)
