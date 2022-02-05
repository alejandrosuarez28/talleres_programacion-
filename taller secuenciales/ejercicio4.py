"""
datos de entrada 
    precio del producto-->pi-->float
datos de salida 
    precio con descuento-->pf-->float
"""
#entrada 
pi=float(input("digite el precio del producto:"))
#caja negra 
d=(pi*0.15)
pf=pi-d
#salidas 
print("el precio con descuento es de: ",pf)
