"""
datos de entrada
    numero de billetes de 50000-->nb5000-->int
    numero de billetes de 20000-->nb200-->int
    numero de billetes de 10000-->nb100-->int
    numero de billetes de 5000-->nb50-->int
    numero de billetes de 2000-->nb20-->int
    numero de billetes de 1000-->nb10-->int
    numero de billetes de 500-->nb5-->int
    numero de billetes de 100-->nb1-->int
datos de saida 
    dinero total-->dt-->int
"""
#entradas
nb500=int(input("digite el numero de billetes de 50000:"))
nb200=int(input("digite el numero de billetes de 20000:"))
nb100=int(input("digite el numero de billetes de 10000:"))
nb50=int(input("digite el numero de billetes de 5000:"))
nb20=int(input("digite el numero de billetes de 2000:"))
nb10=int(input("digite el numero de billetes de 1000:"))
nb5=int(input("digite el numero de billetes de 500:"))
nb1=int(input("digite el numero de billetes de 100:"))
#caja negra
dt=(nb500*50000)+(nb200*20000)+(nb100*10000)+(nb50*5000)+(nb20*2000)+(nb10*1000)+(nb5*500)+(nb1*100)
#salidas
print("el dinero total es: ", dt)
