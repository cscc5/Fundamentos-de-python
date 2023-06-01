#CRUD: 
# Create 
# Read
# Update
# Delete

##Create
numbers = [1, 2, 3, 4, 5]

##Read
print(numbers[1])

##Update
numbers[-1] = 10
print(numbers)

#agregar al final de la lista
numbers.append(500)
print(numbers)

#agregar un elemento en un lugar específico. Se coloca primero la posición y luego el elemento a agregar
numbers.insert(0, 'Hola')
numbers.insert(3, 'otro ejemplo')
print(numbers)

#fusionar listas
tasks = ['responder emails', 'estudiar en platzi', 'auditoria']
new_list = numbers + tasks
print(new_list)

#para saber la posición de un elemento en la lista
print(new_list.index('responder emails'))
index = new_list.index('responder emails')
new_list[index] = 'enviar correos'
print(new_list)

#Indica la posición de un valor
index = numbers.index(5) 
 
##Delete 

#Elimina un elemento en especifico
new_list.remove('auditoria')
print(new_list)

#Elimina el último elemento de la lista por defecto
new_list.pop()
print(new_list)

#Elimina el valor especificado de la lista
new_list.pop(2)
print(new_list)

#reverse. Invierte el orden de los elementos de la lista 
new_list.reverse()
print(new_list)

#Sort. ordenar de menor a mayor. No permite ordenar int y str. Deben ser datos del mismo tipo
new_list2 = [2, 6 , 5, 8, 1, 7, 6]

#Ordena la lista en orden del abacedario o de menor a mayor (NO funciona en listas con tipos de datos mezclados)

new_list2.sort()
print(new_list2)

tasks.sort()
print(tasks)