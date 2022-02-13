"""
datos de entrada 
    ventas totales-->vt-->float
    ventas individuales-->-->float
    salario base-->sb-->float
datos de salida
    salario final-->sf-->float
"""
#entradas 
vt=float(input("diguite las ventas totales "))
vi=float(input("diguite las ventas individuales "))
sb=float(input("diguite el salasio bruto "))
#caja negra
p=(100*vi)/vt
a=sb*0.2
sf=""
if(p>=33):
    sf=sb+a
else:
    sf=sb
#salidas
print("el salario es:",sf )
