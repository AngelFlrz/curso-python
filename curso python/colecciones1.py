# Listas

numeros = [9, 6, 1, 3, 5]

# append (agrega un nuevo valor a la lista)
# numeros.append(10)

# Remove (remueve de la lista un valor)
# numeros.remove(6)

# pop (remueve elementos de la lista usando un indice)
# numeros.pop(1)

# Reasignar/editar valores
# numeros[0] = 10
# numeros[0] += 10

# len ( se usa para saber el tamaño de una lista)
# print(len(numeros))

# index(para saber en que posicion esta un elemento en una lista)
# print(numeros.index(6))

# in (para saber si un elemento se encuentra en una lista)
# print(6 in numeros)

# sort (para ordenar una lista de manera ascendente)
# numeros.sort()

# reverse(para ordenar una lista de manera descendente)
# numeros.reverse()

# Recorrer una lista
# for elem in numeros:
#     print(elem)

# Recorrer una lista por indices
# for i in range(len(numeros)):
#     print(i)


# Cadenas de texto

cadena = "Hola Mundo"

# lower(cadena en minusculas)
# cadena.lower()

# upper(cadena en mayusculas)
# cadena.upper()

# capitalize(capitaliza la primera letra)
# cadena.capitalize()


frutas = "Durazno, Manzanas, Papaya"

lista = frutas.split(",")

cadena2 = "-".join(lista)

print(cadena2)

# Tuplas(Listas inmutables)

variable = [1, 5, 9]

print(type(variable))

tupla = tuple(variable)

print(type(tupla))
