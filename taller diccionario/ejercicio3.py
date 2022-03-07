usuarios = {
"iperurena": {
"nombre": "Iñaki",
"apellido": "Perurena",
"password": "123123"
},
"fmuguruza": {
"nombre": "Fermín",
"apellido": "Muguruza",
"password": "654321"
},
"aolaizola": {
"nombre": "Aimar",
"apellido": "Olaizola",
"password": "123456"
}
}
contador=0
while True:
    if(contador<=3):
        u=str(input("usuario:"))
        c=int(input("digite la contraseña: "))
        if (u=="iperurena" and c==123123):
            print("NOMBRE:Iñaki\nAPELLIDO:Perurena")
            break
        if (u=="fmuguruza" and c==654321):
            print("NOMBRE:Fermín\nAPELIDO:Muguruza")
            break
        if (u=="aolaizola" and c==123456):
            print("NOMBRE:Aimar\nAPELLIDO:Olaizola")
            break
        else:
            contador+=1
            continue
    else:
        print("cuenta bloqueada")
        break