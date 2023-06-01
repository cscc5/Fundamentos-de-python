x=3.3
print(x)

y=1.1+2.2
print(y)

print(x==y)

## Podemos acortar decimales de dos formas: 

# Convirtiendo el valor en string
y_str = format(y,".2g")
print('str =>', y_str)
print(y_str == str(x))

# Forma matematica (restando los dos valores y retornando el valor absoluto)
print(y,x)
tolerance = 0.00001
print(abs(x-y) <tolerance)

## formas de comparar floats
x = 7.7
print("x =", x)

y = 3.4 + 4.3
print("y = 3.4 + 4.3 =", y)

print(f"x == y: {x == y}")

# Haciendo uso de strings
print("x =", x)
y_str = format(y, ".2g")
print("y_str =", y_str)
print(f"x == y: {str(x) == y_str}")

# Comparando por margen de error
print("x =", x)
print("y =", y)
error = 0.001
print(f"x == y, considerando un margen de error de {error} : {abs(x - y) < error}")

