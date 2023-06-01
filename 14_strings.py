text = 'Ella sabe programar en Python'

print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
  print('elegiste bien')
else:
  print('te recomiendo estudiar Python')

size = len('amor')
print(size) #cuenta los caracteres

print(text) 
print(text.upper()) #coloca mayúscula en todo el texto
print(text.lower()) #coloca minúscula en todo el texto
print(text.count('a')) #cuenta la cantidad de veces que aparece la letra

print(text.swapcase()) #cambia las mayúsculas por minúsculas y viceversa
print(text.startswith('Ella')) #binario, comprueba si se cumple la condición con la que empieza la oración
print(text.endswith ('JavaScript')) #binario, comprueba si se cumple la condición con la que termina la oración
print(text.replace('Python', 'PHP')) #reemplaza una por otra

text_2 = 'esto es un título' 
print(text_2)
print(text_2.capitalize()) #coloca la primera lertra en mayúsculas
print (text_2.title()) #coloca mayúscula al inicio de cada palabra
print(text_2.isdigit()) # Binario. Nos dice si el texto es un dígito
print('654'.isdigit())