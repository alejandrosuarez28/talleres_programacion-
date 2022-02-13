"""
datos de entrada
    a-->a-->int
    b-->b-->int
    c-->c-->int
    d-->d-->int
datos de salida
    respuesta-->r-->float
"""
#entrada
a=float("digite a")
b=float("digite b")
c=float("digite c")
d=float("digite d")
#caja negra
r=""
if(d>0):
    r=((a-b)**3)/d
elif(d>=0 and d<0):
    r=((a-c)**2)
#salidas
print("el resultado es:",r)