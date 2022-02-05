"""
datos de entrada
    presupuesto-->p-->float 
datos de salida 
    presupuesto ginecologia-->pg-->float
    presupuesto traumatologia-->pt-->float
    presupuesto pediatria-->pp-->foat 
"""
#entradas 
p=float(input("digite el presupuesto total:"))
#caja negra 
pg=p*0.4
pt=p*0.3
pp=p*0.3
#salidas 
print("el presupuesto de ginecologia:",pg)
print("el presupuesto de traumatologia:",pt)
print("el presupuesto de pediatria:",pp)