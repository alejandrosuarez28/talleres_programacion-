"""
datos de entrada
    precio total-->vt-->float
    precio con descuento-->vd-->float
datos de salida
    porcentaje de descuento-->PD-->float
"""
#entradas
vt=float(input("digite el valor inicial:"))
vd=float(input("digite el valor con descuento:"))
#caja negra 
PD=((vt-vd)*vt)/100
#salidas
print("el porcentaje de descuento es de:",PD)
