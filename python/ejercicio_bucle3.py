email=input("Introduce email: ")

contadorArroba=0
contadorPunto=0

for i in range(len(email)):
    if email[i]=="@":
        contadorArroba=contadorPunto+1

    if email[i]==".":
        contadorPunto=1

if contadorPunto==0 or contadorArroba!=1:

    print("email incorrecto")

else:
    print("email correcto")