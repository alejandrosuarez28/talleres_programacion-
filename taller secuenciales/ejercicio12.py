"""
datos de entrada 
    examen mate-->em-->int
    tarea1 mate-->t1m-->int
    tarea2 mate-->t2m-->int
    tarea3 mate-->t3m-->int
    examen fisica-->ef-->int
    tarea1 fisica-->t1f-->int
    tarea2 fisica-->t1f-->int
    examen quimica-->eq-->int
    tarea1 quimica-->t1q-->int
    tarea2 quimica-->t2q-->int
    tarea3 quimica-->t3q-->int
datos de salida 
    promedio general-->pg-->float
    promedio mate-->pm-->float
    promedio fisica-->pf-->float
    promedio quimica-->pq-->float
"""
#entradas
em=int(input("digite examen de mate"))
t1m=int(input("digite tarea 1 de mate"))
t2m=int(input("digite tarea 2 de mate"))
t3m=int(input("digite tarea 1 de mate"))
ef=int(input("digite examen de fisica"))
t1f=int(input("digite tarea 1 de fisica"))
t2f=int(input("digite tarea 2 de fisica"))
eq=int(input("digite examen de quimica"))
t1q=int(input("digite tarea 1 de quimica"))
t2q=int(input("digite tarea 2 de quimica"))
t3q=int(input("digite tarea 3 de quimica"))
#caja negra 
ptm=((t1m+t2m+t3m)/3)*0.1
pem=em*0.9
pgm=ptm+pem
ptf=((t1f+t2f)/2)*0.2
pef=ef*0.8
pgf=ptf+pef
ptq=((t1q+t2q+t3q)/3)*0.15
peq=eq*0.85
pgq=ptq+peq
pg=pgm+pgf+pgq
#salidas
print("mate: ",pgm)
print("fisica: ",pgf)
print("quimica: ",pgq)
print("general: ",pg)