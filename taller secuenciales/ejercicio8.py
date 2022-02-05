"""
datos de entrada
    lado1-->l1-->float
    lado2-->l2-->float
    lado3-->l3-->float 
datos de salida 
    area-->a-->float 
"""
#entrada
l1=float(input("digite el lado 1: "))
l2=float(input("digite el lado 2: "))
l3=float(input("digite el lado 3: "))
#caja negra 
s=(l1+l2+l3)/2
a=(s*(s-l1)*(s-l2)*(s-l3))**(1/2)
#salida
print("el area es: ",a)
