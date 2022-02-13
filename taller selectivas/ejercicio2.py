"""
datos de entrada
    salario-->s-->float 
datos de salida
    salario con aumento-->sa-->float
"""
#entrada 
s=float(input("digite su salario"))
#caja negra 
sa=""
if(s<900_000):
    sa=s*0.15
else:
    sa=s*0.12
#salidas 
print("el salario total es:",sa)
