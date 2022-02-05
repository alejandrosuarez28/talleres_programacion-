"""
datos de entrada 
    numero de galones-->ng-->float 
datos de salidas 
    precio de la gasolina-->pg-->float 
"""
#entradas 
ng=float(input("digite la cantidad en galones:"))
#caja negra 
l=ng*3.785
pg=l*50000
#salidas 
print ("el precio de la gasolina es:",pg)
