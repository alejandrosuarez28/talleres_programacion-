"""
datos de entrada
    chelines austriacos-->ca-->float
    dracmas griegos-->dg-->float 
    pesetas-->pe-->float 
datos de salida 
    pesetas-->ps-->float
    francos franceses-->ff-->float 
    dolares EEUU-->de-->float 
    liras ialianas-->li-->float 
"""
#entradas
ca=float(input("digite los chelines austriacos: "))
dg=float(input("digite los dracmas griegos: "))
pe=float(input("digite las pesetas: "))
#caja negra
ps=(ca*956_871)/100
ff=(dg*886.07)/20_110
de=(pe/122_499)
li=(pe*100)/9_289
#salidas 
print("pesetas: ",ps)
print("francos: ",ff)
print("dolares: ",de)
print("liras: ",li)