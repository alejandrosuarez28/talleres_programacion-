"""
datos de entrada 
    numero de naranjas-->nn-->int
    precio por docena-->pd-->float
    ventas finales-->vf-->float
datos de salida 
    porcentaje de ganancias-->pg-->float
"""
#entradas
nn=int(input("digite el numero de naranjas:"))
pd=float(input("digite el precio por docena:"))
vf=float(input("digite las ventas totales:"))
#caja negra 
cn=(nn/12)*6
g=(vf-cn)
pg=(g*100)/cn
#salidas
print("el porcentaje de ganancias es de:",pg,"%")
