import pandas as pd
print("hola mundo")

# Python 3: Fibonacci series up to n
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
fib(1000)

"""
Reto #1
Impresión de bienvenida a los ejercicios interactivos

En este ejercicio, tu desafío es utilizar la función print para imprimir tres mensajes en la sección Console. Para ello, debes utilizar la función print tres veces en el siguiente orden con los siguientes mensajes:

"Te doy la bienvenida al Coding Playground"
"Mi primer print"
"30"
Recuerda prestar atención a los espacios y mayúsculas en los mensajes, ya que son importantes para que tu respuesta sea correcta. Un ejemplo de cómo utilizar la función print se encuentra a continuación:
"""
print("Te doy la bienvenida al Coding Playground")
print("Mi primer print")
print("30")

"""
Reto #2: 
Modifica la variable text por un número y luego imprímelo

En este desafío, vas a practicar lo que has aprendido acerca de variables en Python. Una variable es un lugar en la memoria donde se puede almacenar un valor, por ejemplo, un número o una cadena de texto. En Python, las variables se declaran utilizando el nombre de la variable, seguido de un signo igual y el valor que se desea asignar a la variable. Por ejemplo:

text = 'My text'
print(text)

Recuerda que las variables pueden ser modificadas a lo largo de un programa, tu reto es modificar el valor de la variable text para que sea un número y luego imprimirlo utilizando la función print.
"""
text = 'My text'
text = 1
print(text)

"""
Reto #3
Imprime el formato adecuado

En este desafío, se te proporcionará un código base encontrarás las variables name y age todas como strings. Tu tarea es crear un formato de string que, como resultado, muestre un mensaje en la sección Terminal. El mensaje deberá tener la siguiente forma:

Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años

Ten en cuenta que debes calcular la edad que tendrás en 10 años a partir de la edad. Por ejemplo, si la edad es 29 años, el mensaje mostrado deberá decir "tengo 29 años y en 10 años tendré 39 años"
"""
name = 'Juana'
print(name)
age = '10'
print(age)


template = f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {age + 10} años"
print(template)

"""
Reto #4:
Validar si un numero ingresado por consola es par o impar

En este desafío, tienes una variable llamada number como string, tu reto es determinar si ese string es un número par o impar. Para hacer esta validación, debes transformar el string a number y luego realizar una condicional que compruebe si el número es divisible por dos. Si lo es, significa que el número es par y debes imprimir el mensaje Es par. Si no lo es, significa que el número es impar y debes imprimir el mensaje Es impar.

A continuación se muestran ejemplos de cómo debería funcionar tu solución:
"""
num = int(input("Ingresa un número: "))

if num%2 == 0:
    print("El número que ingresaste es par")
else:
    print("El número que ingresaste es impar")

"""
Reto #5:
Agrega, modifica y elimina elementos de una lista)

En este desafío, se te proporcionará una lista de letras llamada letters. Tu reto es realizar las siguientes operaciones en orden:

Agregar la letra G al final de la lista.
Reemplazar la letra en la posición 0 con la letra Z.
Eliminar la letra C de la lista.
Imprimir la lista resultante al revés.
"""
letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)

"""
Reto #6
Agrega, modifica y elimina elementos de un diccionario

En este desafío, se te proporcionará un diccionario llamado person que contiene información sobre una persona. Tu reto es realizar las siguientes operaciones en orden:

Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
Eliminar el elemento del diccionario con la llave "age".
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario.
"""
person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person["twitter"] = "@nicobytes"
person["name"] = "Felipe"
del person["age"]
print(list(person.keys()))
print(list(person.values()))

"""
Reto #7
Agrega solo los números positivos de una lista

En este desafío, se te proporcionará una lista de números llamada my_list. Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. Luego, debes agregar estos números a una nueva lista llamada new_list. Al final del ciclo, debes imprimir los valores contenidos en new_list utilizando la función print.

Por ejemplo, si la lista es [1, -1, 2, -2, 3, -3, 4, -4], después de realizar las operaciones descritas, la lista new_list debería contener solo los números positivos, es decir, [1, 2, 3, 4].
"""

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for number in my_list:
  if number >= 0:
    new_list.append(number)

print(new_list)