"""
datos de entrada
    capital-->c-->int
datos de salida 
    ganancia mensual-->g-->float
    capital final-->cf-->float
"""
#entradas 
c=int(input("digite su capital:"))
#caja negra 
g=float(c*0.02)
cf=float(g+c)
#salidas 
print("las ganancias son:", g)
print("el capital final es: ", cf)
