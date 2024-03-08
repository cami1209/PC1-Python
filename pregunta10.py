lista=["Rojo","Verde","Blanco","Negro","Rosa","Amarillo"]
elementos_eliminados = []
elementos_que_se_eliminan =[0,4,5]
for indice in sorted(elementos_que_se_eliminan,reverse=True):
    elementos_eliminados.append(lista.pop(indice))
print(lista)