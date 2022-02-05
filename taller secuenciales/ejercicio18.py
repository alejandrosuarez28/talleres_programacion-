"""
datos de entrada 
    prestamo inicial-->vi-->float
    prestamo con intereces-->vf-->float
datos de salida 
    porcentaje anual-->pa-->float
"""
#entradas
vi=float(input("digite el capital del prestamo"))
#caja negra 
pa=100/(vi*4)
#salidad
print("el porcentaje anuel es:",pa)
