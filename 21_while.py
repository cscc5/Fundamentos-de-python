"""
Ciclo infinito:

while True:
    print("¿Lo ejecutaste aunque sabias que no se iba a detener?....... se sigue imprmiendo?..... ¿Que parte de infinito no entiendes?")
"""

counter = 0

while counter < 10:
  counter += 1
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)


counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue # Salta automaticamente a la siguiente iteracion o ciclo obviando todo lo que hay de esas linea para abajo; lo que quiere decir que solo se ejecutará el siguiente print, si y solo si el contador es igual o mayor que 15
  print(counter)