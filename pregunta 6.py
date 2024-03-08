edad = int(input("Ingresa tu edad:"))
if edad < 4:
    print("Entrada gratis")
elif edad >= 4 and edad <= 18:
    print ("Entrada $5")
else:
    print("Entrada 10$")