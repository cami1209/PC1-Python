consumo = float(input("¿Cuánto fue tu consumo?"))
propina = float(input("¿Qué porcentaje deseas dejar de propina (Solo el número)?"))
monto_propina = float(consumo*propina/100)
print("Debes dejar de propina",monto_propina,"soles")