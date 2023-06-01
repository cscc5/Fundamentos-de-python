"""
Diferencias entre listas y tuplas:

Las tuplas se diferencian de las listas porque una vez se
realiza la declaración no se pueden modificar dado que son inmutables.

Las tuplas se definen entre parentesis
Listas = []
Tuple = []
"""

numbers = (1,2,3,4,5)
Strings = ('nico', 'zule', 'santi')
print(numbers)
print(Strings)

print(type(Strings))
print(type(numbers))

print('0 =>', numbers[0]) #Primera posición
print('-1 =>',Strings[-1]) #Última posición

print(Strings)
print(type(Strings))

#Retorna un error si el valor no se encuentra en la tupla
print(Strings.index('ale')) 

#COUNT. Para saber cuántas veces aparece un elemento en una lista o tupla
print(Strings.count('ale'))

# Si se requiere realizar modificaciones podriamos hacer uso de las listas y convertir la tuple a tipo list, realizar la modificación y devolverla a su tipo inicial

#Transformar una tupla en lista
myList = list(Strings)
print(myList)

myList[1] = 'juli'

#Transformar una lista en tupla
Strings = tuple(myList)
print(Strings)