"""
datos de entrada
    edad1-->e1-->int
    edad2-->e2-->int
    edad3-->e3-->int
datos de salida 
    promedio edades-->pe-->float 
"""
#entrada
e1=int(input("dijite edad uno:"))
e2=int(input("dijite edad dos:"))
e3=int(input("dijite edad tres:"))
#caja negra 
pe=float(e1+e2+e3)/3  
#salidas 
print(f"el promedio es: {pe}")
