"""
datos de entrada 
    inversion-->i-->float
    interes-->g-->float
datos de salida 
    monto-->m-->float
"""
#entradas 
i=float(input("diguite la inversion inicial:"))
g=float(input("diguite el porcentaje de interes:"))
#caja negra 
gb=(i*g)/100
m=""
if(gb>100_000):
    m=(i+gb)
else:
    m=i
#salidas
print("el monto final es: $",m)