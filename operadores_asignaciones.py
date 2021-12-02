"""Operadores de asignaciones"""

a, b, c = 21, 10, 0#Opcional

a= 25 
b= 10
c= 0


print ("Valor de variable 'a':", a)
print ("Valor de variable 'b':", b)

c = a + b
print ("Operador = | El valor de variable 'c' es ", c)

c += a #eq1
c = c + a #eq1
print ("Operador += | El valor de variable 'c' es ", c)

c *= a #eq2
c = c * a #eq2
print ("Operador *= | El valor de variable 'c' es ", c)

c /= a #eq3
c = c / a #eq3 #Cualquier division sera flotante
print ("Operador /= | El valor de variable 'c' es ", c)

c = 2
c %= a #Modulo
print ("Operador %= | El valor de variable 'c' es ", c)

c **= a #Exponencial
print ("Operador **= | El valor de variable 'c' es ", c)
c= 100
a= 10
c //= a #Raiz
print ("Operador //= | El valor de variable 'c' es ", c)

