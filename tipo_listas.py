"""
    La lista son variables que almacenan arrays, internamente 
    cada posición puede ser un tipo de datos distinto.
"""

# Colección ordenada / arreglos o vectores
lista = [2, "CMS", True, 5, "C", 50, "Caso",["Plone", 10]]
print (lista, type(lista))
lista2 = [2, "CMS", True]
listaR = lista + lista2
lista.append(lista2)
print(len(listaR))
print(listaR.count(True))
#print(lista*10)
print(lista)
# Acceder a un elemento especifico
l2 = lista[1]#elem en posicion 1
print (l2)



print("Wuuut? ",lista[-1][-1])
# Acceder a un elemento a una lista anidada
#l3 = lista[3][1]#La primera posicion es de la lista, y luego la posicion de la lista interior
#print (l3)

# Establecer nuevo valor de un elemento de lista
lista[1] = 4
print (lista)
lista[1] = "CMS"

# Obtener un rango de elemento especifico
l3 = lista[0:3]
print (l3)

l1 = [10,2,13,40]
l2 = [6,70,8,9]
l1.extend(l2)
print(l1)

l1.sort()
print(l1)

#el1 = l1.pop()
#print(el1)
#el1 = l1.pop()
#print(el1)
print(l1)

l1.remove(2)
print(l1)

#del l1#Tambien aplica para funciones

def funcionUno():
    print("hola funcion uno")
funcionUno()
#del funcionUno
#funcionUno

print(l1)

# Obtener un rango con saltos de elementos específicos
'''

l4 = lista[0:7:3]
print (l4)
l5 = lista[1::2]
print (l5)
l5 = lista[::2]
print (l5)
'''