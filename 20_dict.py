person={
    'name': 'Cristian ',
    'last_name':'Colorado',
    'age': 22,
    'langs': ['Python', 'JavaScript'],
    'reloj': 'casio',
    'zapatos': 'Arturo Calle'
}
print(person)

#Actualizar o agregar llave
person['name'] = 'Elver'

#se puede sumar, restar, etc a los int
person['age'] += 1

#agregar elementos(clave/valor) a la lista de una llave
person['langs'].append('C#')

#Eliminar atributo (clave/valor) de la llave
# Opción con "DEL"
del person['reloj']

#En los diccionarios 'pop' necesita un argumento entre los paréntesis. En las listas elimina por defecto el último elemento si no se especifica cuál queremos eliminar
person.pop('zapatos')

print(person)

#devuelve los pares key-valor en forma de tupple
print('item')
print(person.items())

#devuelve una lista de las key
print('keys')
print(person.keys())

#devuelve un array de los values
print('values')
print(person.values())