"""
datos de entrada 
    numero de horas-->nh-->int
    precio de hora--> ph-->float 
datos de salida 
    salario neto-->sn-->float 
"""
#entrada 
nh=int(input("digite el numero de horas"))
ph=float(input("digite el precio de la hora"))
#caja negra
sb=nh*ph
ds=sb*0.2
sn=sb-ds
#salida 
print("salario neto",sn)
