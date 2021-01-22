clave=input("Introduce contrasena: ")

contador=0

for i in range(len(clave)):
    if clave[i]==" ":
        
        contador=1

if len(clave)<8 or contador>0:

    print("contrasena erronea")

else:
    print("contrasena correcta")