my_dict = {}
print(type(my_dict))

my_dict = {
  'platzi': "plataforma de aprendizaje  online",
  'python': "lenguaje de programación",
  'tupla': "estructura de datos inmutable"
}
print(my_dict)
#LEN. Para contar los elementos/llaves del diccionario/lista/tupla
print(len(my_dict))
#GET. leer una de las opciones del diccionario. Si el valor no existe arroja 'NONE'
  #option a
print(my_dict['python'])
  #option b. con GET
print(my_dict.get('tupla'))
print(my_dict.get('tabla'))
  #con IF podemos saber si está o no la llave en el diccionario para evitar que arroje error si no está al usar la opción a. Arroja True si está, False si no está
print('platzi' in my_dict)
print('opción que no está' in my_dict)