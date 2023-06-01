numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['Study at Platzi', 'print forms', 'take id photo']
print(tasks)
types = ['Hello', 1, True]
print(types)

print(numbers[0]) #imprime el elemento de la lista, no sus caracteres
print(tasks[0])
print(numbers)

#coloca o actualiza el elemento de la lista en ese lugar
tasks[0] = 'Make the dishes' 
print(tasks)
tasks[0] = 'wash the dishes'

#muestra los elementos hasta la posición elegida
print(numbers[:3]) 
#muestra si el elemento se encuentra en la lista
print(True in types)
print('Hello' in types)

