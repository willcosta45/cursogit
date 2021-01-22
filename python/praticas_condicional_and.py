print("Programa de Becas agno 2019")
distancia_escuela=int(input("Introduce la distancia a la escuela en km "))
print(distancia_escuela)

numero_hermanos=int(input("introduce numero de hermanos "))
print(numero_hermanos)

sueldo_minimo=int(input("introduce sueldo anual "))
print(sueldo_minimo)

if distancia_escuela>40 and numero_hermanos>2 or sueldo_minimo<=20000:
    print("Tienes derecho a beca")

else:
    print("No tienes derecho a beca")