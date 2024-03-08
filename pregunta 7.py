primer_numero = float(input("Ingresa el primer numero:"))
segundo_numero = float(input("Ingresa el segundo numero:"))
print("Elige una opción: Marca 1 para sumar los dos numeros. Marca 2 para restar los dos numeros. Marca 3 para multiplicar los dos numeros")
opcion = int(input("Marca tu opción"))
sumar = primer_numero + segundo_numero
restar = primer_numero - segundo_numero
multiplicar = primer_numero*segundo_numero

if opcion == 1:
    print("La suma es", sumar)
elif opcion ==2:
    print ("La resta es",restar)
elif opcion ==3:
    print ("La multiplicación es", multiplicar)
else:
    print("La opcion no es correcta")