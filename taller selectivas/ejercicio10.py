"""
datos de entrada 
    categoria-->c-->int
    sueldo base-->sb-->float 
datos de salida
    categoria-->c-->int
    sueldo nuevo-->sn-->float 
"""
#entradas
c=int(input("diguite la categoria "))
sb=(input("diguite el sueldo base "))
#caja negra
sn=""
if(sb==5000000)and (c==1):
    sn=sb+(sb*0.1)
elif(sb==4300000)and (c==2):
    sn=sb+(sb*0.15)
elif(sb==3600000) and (c==3):
    sn=sb+(sb*0.2)
elif(sb==2000000) and (c==4):
    sn=sb+(sb*0.4)
elif(sb==900000)and(c==5):
    sn=sb+(sb*0.6)
#salidas
print("la categoria es:",c)
print("el nuevo sueldo es:",sn)
