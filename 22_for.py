#en los ciclos for los datos ya se encuentran definidos, mientras que en los while no tenemos necesariamente, esta definición

#RANGE sirve para lo mismo que while pero con menos líneas de código y para recorrer ciertas estructuras
for element in range(1,21):
    print(element)

my_list =[23,45,67,89,43]
for element in my_list:
    print(element)

my_tuple = ('andres', 'esteban', 'pedro', 'hernan')
for element in my_tuple:
    print(element)

product ={
    'name': 'Jordan',
    'modelo': 'reto 1',
    'year': 2016
}

#Devolverá las llaves con sus respectivos valores
for element in product:
    print(element, '-> ', product[element])

for key, value in product.items():
  print(key, '=>', value)

people = [
    {
    'name':"nico",
    'last_name':'rendon',
    'age':24
    },
    {
    'name':"carlos",
    'last_name':'urrutia',
    'age':25   
    },
    {
    'name':"juan",
    'last_name':'cano',
    'age':26
    }
]

for person in people:
    print(person)

for person in people:
    print('name: ', person['name'])