"""
datos de entrada 
    a-->a-->float 
    b-->b-->float
    c-->c-->float
datos de salida
    corte en x1-->x1-->float
    corte en x2-->x2-->float
"""
#entradas
a=float(input("diguite a "))
b=float(input("diguite b "))
c=float(input("diguite c "))
#caja negra
d=(b**2)-(4*a*c)
x1=""
x2=""
if d==0:
    x1=x2=b/(2*a)
elif d>0:
    x1=(-b+(((b**2)-(4*a*c))**(1/2)))/(2*a)
    x2=(-b-(((b**2)-(4*a*c))**(1/2)))/(2*a)
else:
    x1=x2="no tiene solucion"
#salidas
print("el corte 1 es:",x1)
print("el corte 2 es:",x2)
