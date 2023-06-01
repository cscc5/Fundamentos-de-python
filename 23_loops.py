matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]]

#Devuelve la lista ubicada en esa posición
print(matriz[0])

#Devuelve los elementos de la lista ubicada en esa posición. Primero posición de la lista, luego del elemento
print(matriz[0][1])

#ciclo anidado
for row in matriz:
    print(row)
    for column in row:
        print(column)