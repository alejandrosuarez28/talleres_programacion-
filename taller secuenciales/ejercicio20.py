"""
datos de entrada
    precio total-->pt-->float
    precio de cuota-->pc-->float
datos de salida 
    porcentaje extra-->pe-->float
"""
#entrada
pt=float(input("digite el precio total:"))
pc=float(input("digite el precio de la cuota"))
#caja negra 
pe=pc-(pt/12)
#salidas
print("el porcentaje extra es;",pe,"%")
