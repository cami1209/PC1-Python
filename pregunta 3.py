peso_payaso = 112
peso_muñeca = 75
cantidad_payasos = int(input("¿Cuántos payasos fueron vendidos?"))
cantidad_muñecas = int (input("¿Cuántas muñecas fueron vendidas?"))
Total_payasos = peso_payaso*cantidad_payasos
Total_muñecas = peso_muñeca*cantidad_muñecas
Total_paquete = Total_payasos + Total_muñecas
print("El peso total del paquete es de",Total_paquete,"kg")