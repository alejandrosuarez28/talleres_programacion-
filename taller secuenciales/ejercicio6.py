"""
datos de entrada 
    numero de estudaintes-->ne-->int
    numero de hombres-->nh-->int
    numero de mujeres--> nm-->int
datos de salida 
    porcentaje hombres-->ph-->int
    porcentaje mujeres-->pm-->int
"""
#entradas 
ne=int(input("digite el numero de estudiantes "))
nh=int(input("digite el numero de hombres "))
nm=int(input("digite el numero de mujeres "))
#caja negra
ph=(nh*100)/ne
pm=(nm*100)/ne
#salida 
print("hombres: ",ph,"%")
print("mujeres: ",pm,"%")
