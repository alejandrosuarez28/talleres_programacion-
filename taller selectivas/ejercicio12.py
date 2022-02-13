"""
datos de entrada 
    cantida de dinero-->cd-->int
datos de salida
    numero de billetes de 100k-->n100k-->int
    numero de billetes de 50k-->n50k-->int
    numero de billetes de 20k-->n-->int
    numero de billetes de 10k-->n-->int
    numero de billetes de 5k-->n-->int
    numero de billetes de 2k-->n-->int
    numero de billetes de 1k-->n-->int
    numero de billetes de 500-->n-->int
    numero de billetes de 200-->n-->int
    numero de billetes de 100-->n-->int
    numero de billetes de 50-->n-->int
"""
#entradas
cd=int(input("diguite la cantidad de dinero "))
#caja negra
lista=[]
for i in[100000,50000,20000,10000,5000,2000,1000,500,200,100,50]:
    if (cd>=i):
        lista.append(int(cd/i)*i)
        cd=cd-int(cd/i)*i
    else:
        cd=cd
lista0=str(lista)[1:-1]
#salidas
print(lista0,cd)