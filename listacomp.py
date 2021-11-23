#La forma general de la definición de una lista por comprensión es:

#[expresion for item in iterable]

#Opcionalmente, se puede incluir un condicional en la expresión:

#[expresion for item in iterable if condicion]
numbers = [1, 2, 3, 4]
results = []

for n in numbers:
    results.append(n + 1)
    
print(results)

numbers = [1, 2, 3, 4]
results = [n + 1 for n in numbers]

print(results)

lista = []
for letra in 'palabra':
    lista.append(letra)
print(lista)

lista = [letra for letra in 'palabra']
print(lista)

names = ['Ch','Dh','Eh','cb','Tb','Td','Chb','Tdb']
final_names = [name for name in names if name.lower().endswith('b') and len(name) > 2]
print(final_names)

list_of_tuples = [(n, n*n) for n in numbers]
print(list_of_tuples)

names_1 = ['Oralie' ,'Imojean' ,'Michele', 'Ailbert', 'Stevy']
names_2 = ['Jayson', 'Oralie' ,'Michele', 'Stevy', 'Alwyn']


common = []
for a in names_1:
    for b in names_2:
        if a == b:
            common.append(a)

common = [a for a in names_1 for b in names_2 if a == b]
print(common)

lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)

lista = [numero**2 for numero in  range(0,11)]
print(lista)

lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

lista = [numero for numero in range(0,11) if numero % 2 == 0 ]
print(lista)


lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

lista = [numero for numero in 
            [numero**2 for numero in range(0,11)] 
                if numero % 2 == 0 ]
print(lista)

#[f(x) if condition else g(x) for x in list]

my_list = ['Ali','Mark', None, 'Sara', None, 'Rahul']

new_list = [str(x.strip()) if x is not None else '' for x in my_list]
print(new_list)

my_list = ['Ali','Mark', None, 'Sara', None, 'Rahul']

new_list = [x.upper() if x is not None else '' for x in my_list]
print(new_list)

points = []
for x in range(0, 5 + 1):
    for y in range(0, 10 + 1):
        points.append((x, y))
print(points)

points = [(x, y) for y in range(0, 5 + 1) for x in range(0, 10 + 1)]
print(points)

#map(function, iterable[, iterable1, iterable2,..., iterableN])

letters = list(map(lambda y: y, 'analytics'))
print(letters)

doubles = {n: n * 2 for n in range(1, 11)}
print(doubles)

# Return double 
def addition(n):
    return n + n

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

l = ['sat', 'bat', 'cat', 'mat']

test = list(map(list, l))
print(test)