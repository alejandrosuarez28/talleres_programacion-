est={}
est.update({
        "1":{
            "nombre":"Lorea",
            "nota": 8
    },
        "2": {
            "nombre":"Markel",
            "nota": 4.2
    }, 
        "3": {
            "nombre":"Julien",
            "nota": 6.5
    }
})
l_susp=[]
l_apro=[]
media=[]
for i in range(0,10):
    num=int(input("Numero de estudiante: "))
    prof=input("Nombre del estudiante: ")
    nota=float(input("Nota del estudiante: "))
    est.update({num:{"nombre":prof, "nota":nota}})
for key in est.keys():
    if (est[key]["nota"]<5):
        l_susp.append(est[key]["nombre"])
    else:
        l_apro.append(est[key]["nombre"])
    media.append(est[key]["nota"])
    s=sum(media)/(len(l_susp)+len(l_apro))
print(l_susp)
print(l_apro)
print("{:.1f}".format(s))

