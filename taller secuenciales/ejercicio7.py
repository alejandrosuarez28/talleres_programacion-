"""
datos de entrada 
    metros-->m-->float 
datos de salida 
    pulgadas-->In-->float
    pies-->ft-->float 
"""
#entradas 
m=float(input("digite la longitud en metros: "))
#caja negra 
In=(m*39.27)
ft=In/12
#salida 
print("pulgadas: ",In,"in")
print("pies",ft,"ft")
