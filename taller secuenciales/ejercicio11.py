"""
datos de entrada 
    numero de horas-->nh-->int
    numero de horas extra-->nhe-->int
    sueldo por hora-->sh--> float 
    numero de hijos-->ni-->int
datos de salida 
    asignaciones-->a-->float
    deducciones-->d-->float
    sueldo neto-->sn-->float
"""
#entradas 
nh=int(input("digite el numero de horas"))
nhe=int(input("digite el numero de horas extras"))
sh=float(input("digite el sueldo por hora"))
ni=int(input("digite el numero de hijos "))
#caja negra 
sb=nh*sh
she=(sh*0.25)+sh
se=she*nhe
a=se+430_000+(173_000*ni)
d=sb*0.14
sn=sb+a-d 
#salida 
print("asignaciones: ",a)
print("deducciones: ", d)
print("sueldo neto: ", sn)