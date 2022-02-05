"""
datos de entrada 
    parcial1-->p1-->int
    parcial2-->p2-->int
    parcial3-->p3-->int
    examen final-->ef-->int
    trabajo final-->tf-->int
datos de salida 
    calificacion final-->cf-->float
"""
#entrada 
p1=int(input("digite el parcial uno:"))
p2=int(input("digite el parcial dos:"))
p3=int(input("digite el parcial tres:"))
ef=int(input("digite el examen final:"))
tf=int(input("digite el trabajo final:"))
#caja negra 
pt=((p1+p2+p3)/3)*0.55
pe=(ef*0.3)
tf=(tf*0.15)
cf=pt+pe+tf
#salida 
print("la calificacion final es: ",cf)
