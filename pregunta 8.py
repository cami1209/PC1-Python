hora = input("Ingresa la hora en formato de 24 horas:")
horas_minutos = hora.split(":")
horas = int(horas_minutos[0])
minutos = int(horas_minutos[1])
if 7<= horas <=8 and 0<=minutos<=59:
    print("Hora del desayuno")
elif 12<=horas<=13 and 0<=minutos<=59:
    print ("Hora  de almuerzo")
elif 18<= horas <=19 and 0<=minutos<=59:
    print ("Hora de la cena")
else:
    print("")