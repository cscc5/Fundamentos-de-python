text = 'Ella sabe programar en Python'
#indexing. Retorna la posición indicada. Siempre comienza por 0. Se coloca entre []
print(text[0])
print(text[1])

#para calcular el último caracter
#opción 1
size = len(text)
print('size => ', size)
print(text[size-1])
#opción 2
print(text[-1])

#slicing, permite sacar partes del texto
print(text[0:16])
print(text[:16]) #por defecto entiende que es desde la posición 0
print(text[23:29])
print(text[20:]) #por defecto entiende que debe ir hasta el final
print(text[:]) #por defecto entiende que va desde el inicio hasta el final
print(text[10:16:1]) #el tercer número(1) es el número de saltos
print(text[10:16:2])
print(text[::2]) #para ir desde el inicio al final, indicando nro de saltos
print(text[::-1]) #para tener los caracteres al revés, empiezando desde el final al inicio