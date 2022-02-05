"""
datos de entrada 
    sueldo base-->sb-->float 
    valor de las ventas totales-->vt-->float 
datos de salida 
    comicion-->c-->float
    sueldo total-->st-->float
"""
#entrada
sb=float(input("digite el sueldo base:"))
vt=float(input("gigite el valor de las ventas totales:"))
#caja negra
c=(vt*0.1)
st=c+sb
#salidas 
print("la comicion es: ", c)
print("el sueldo total es: ", st)
