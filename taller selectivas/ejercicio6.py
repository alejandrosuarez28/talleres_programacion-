"""
datos de entrada 
    numero de 4 dijitos-->n-->int
datos de salida
    numero redondeado-->N-->int
"""
#entrada 
n=int(input("diguite un numero de 4 dijitos "))
#caja negra 
a=n%100
b=100-a
N=""
if (n%100>=50):
    N=n+b
else:
    N=n-a
#salidas
print(N)
