"""
datos de entrada 
    dia de nacimiento-->dn
    mes de nacimiento-->mn
    año de nacimiento-->an
datos de salida
    signo zodiacal 
"""
#entradas
dn=int(input("diguite el dia de nacimiento "))
mn=int(input("diguite el mes de nacimiento "))
an=int(input("diguite el año de nacimiento "))
#caja negra
import datetime
x = datetime.datetime.now()
da=int(x.strftime("%d"))
ma=int(x.strftime("%m"))
aa=int(x.strftime("%Y"))

edad=""
if (da>=dn and ma>=mn):
    edad=aa-an
else:
    edad=aa-an-1


z=""
if mn==1:
    if dn>=21:
        z="acuario"
    else:
        z="capricornio"
elif mn==2:
    if dn>20:
        z="picis"
    else:
        z="acuario"
elif mn==3:
    if dn>21:
        z="aries"
    else:
        z="picis"
elif mn==4:
    if dn>21:
        z="tauro"
    else:
        z="aries"
elif mn==5:
    if dn>22:
        z="geminis"
    else:
        z="tauro"
elif mn==6:
    if dn>22:
        z="cancer"
    else:
        z="geminis"
elif mn==7:
    if dn>23:
        z="leo"
    else:
        z="cancer"
elif mn==8:
    if dn>24:
        z="virgo"
    else:
        z="leo"
elif mn==9:
    if dn>23:
        z="libra"
    else:
        z="virgo"
elif mn==10:
    if dn>23:
        z="escorpio"
    else:
        z="libra"
elif mn==11:
    if dn>22:
        z="sagitario"
    else:
        z="escorpio"
elif mn==12:
    if dn>22:
        z="capricornio"
#salidas
print("signo del sodiaco",z)
print("edad: ",edad)