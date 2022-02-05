"""
datos de entrada
    lectura actual-->l1-->foalt
    lectura anterior-->l2-->float
    precio por kilovatio-->pk-->float
datos de salida 
    precio del recibo-->pr-->float 
"""
#entradas
l1=float(input("digite la lectura actual:"))
l2=float(input("digite la lectura anterior:"))
pk=float(input("digite el precio por kilovatio:"))
#caja negra 
pr=(l2-l1)*pk
#salidas 
print ("el costo del recibo es: ", pr)