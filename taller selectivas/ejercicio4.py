"""
datos de entrada
    monto de compra-->mc-->float
datos de salida 
    invercion empresa-->ie-->float
    cantidad a credito-->cc-->float
    intereses-->i-->float
    prestamo banco-->pb-->float
"""
#55 empresa 
#30 banco 
#15 fabricante (+20%)

#70 empres 
#30 fabricante (+20%)

#entradas 
mc=float(input("diguite el monto de la compra"))
#caja negra 
ie=""
cc=""
i=""
pb=""
if(mc>=5_000_000):
    ie=mc*0.55
    pb=mc*0.3
    cc=mc*0.15
    i=cc*0.2
else:
    ie=mc*0.7
    cc=mc*0.3
    i=cc*0.2
#salidas 
print("invercion de la empresa: ",ie)
print("cacntidad de credito: ",cc)
print("intereses: ",i)
print("prestamo de banco:",pb)
