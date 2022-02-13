"""
datos de entrada 
    temperatura-->t-->float
datos de salida
    deporte-->d-->str
"""
#entradas
t=float(input("dguiteue la temperatura "))
#caja negra
d=""
if(t>85):
    d="natacion"
elif(70<t<=85):
    d="tenis"
elif(32<t<=70):
    d="golf"
elif(10<t<=32):
    d="esquí"
elif(t<=10):
    d="marcha" 
#salidas
print("el deporte es:",d)

