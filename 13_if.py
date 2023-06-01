if  True:
    print('Hello word')

if False:
    print("Tienes un error en el código, porque esta linea no se debe ejecutar")

pet=input("¿Cual es el nombre de tu mascota?")

if pet == "perro":
    print("Genial, tienes un perro")
elif pet == "gato":
    print("espero tengas suerte")
else:
    print("No tienes ninguna mascota interesante")


stock = int(input('Digita el stock => '))

if stock >=100 and stock <=1000:
  print('El stock es correcto')
else: 
  print('El stock es incorrecto')

