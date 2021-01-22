num1=(int(input("introduce el primer numero")))
num2=(int(input("introduce el segundo numero")))

def Devuelvemax (n1,n2):
    if n1 < n2:
        print(n2)
    elif n2 < n1:
        print(n1)
    else:
        print("son iguales")

print("El numero mas alto es ")
Devuelvemax(num1,num2)

