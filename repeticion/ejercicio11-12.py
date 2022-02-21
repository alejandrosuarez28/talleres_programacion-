
lec=[]
n=0
pc=0
pw=0
while True:
    print("1 para agregar nueva encusta\n2 para terminar ")
    s=int(input())
    if(s==1):
        c=int(input("¿toma alcohol?\n1:si\n2:no\n"))
        if(c==1):
            t=int(input("1- Aguardiante\n2-Ron\n3-Cerveza\n4-Tequila\n5-Whisky\n6-Otro\n"))
            e=int(input("¿edadd?\n"))
            if(t==3):
                lec.append(e)
                pc=pc+1
            elif(t==5):
                pw=pw+1
            s=int(input("¿sexo?\n1:hombre\n2:mujeres\n"))
            n=n+1
            continue
        elif(c==2):
            e=int(input("¿edadd?\n"))
            lec.append(e)
            s=int(input("¿sexo?\n1:hombre\n2:mujeres\n"))
            n=n+1
            continue 
    elif(s==2):
        break
o1=0
se=sum(lec)
if(s==2 and e<18):
    o1=o1+1
o2=0
if((s==1)and(20<=e<=25)and(t!=1)):
    o2=o2+1
o3=0
if(pc==0):
    o3=0
else:
    o3=se/pc
o4=pw/n


print("numero de encustads ",n)
print("mujeres menor de edad ",o1)
print("Total, de hombres que no consumen aguardiente y que tienen entre 20 y 25 años de edad ",o2)
print("Promedio de edad de las personas que consumen cerveza ",o3)
print("Porcentaje de personas que consumen whisky en relación con el total encuestado ",o4)