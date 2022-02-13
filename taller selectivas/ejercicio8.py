"""
datos de entrada 
    p-->p-->int
    q-->q-->int
datos de salida
    P y Q satisfacen la expresión-->s-->str

"""
#entradas
p=int(input("diguite p "))
q=int(input("diguite q "))
#caja negra
s=""
if(((p**3)+(q**4)-(2*(p**2)))>680):
    s="P y Q satisfacen la expresión"
else:
    s="P y Q no Satisfacen la expresión"
#salidas
print(s)
