"""
    Una cadena de caracteres, no es más que varios caracteres 
    encerrado entre comillas simples ('cadena') o dobles ("cadena").
"""

# Comillas simples
cadena1 = 'Texto entre comillas simples,'
print (cadena1, type(cadena1))

# Comillas dobles
cadena2 = "Texto entre comillas dobles,"
print (cadena2, type(cadena2))

# Cadena con código escapes
cadena3 = 'Texto entre \n\t comillas simples,'
print (cadena3, type(cadena3))

# Cadena varias lineas
cadena35= "INSERT"
cadena4 = f"""Texto linea 1
linea 2
linea 3
linea 4
.
.
{cadena35}.
.
.
linea N"""
print (cadena4 + ",", type(cadena4))

# Repetición de cadena con el operador de multiplicación
cadena5 = "Cadena" * 5
print (cadena5 + ",", type(cadena5))

# Concatenación de cadena
nombre, apellido = "Leonardo", "Caballero"
nombre_completo = nombre + " Favio " + apellido
print (nombre_completo + ",", type(nombre_completo))

# Función len() devuelve el tamaño de la cadena
nombre_completo = "Coincidir"
print(nombre_completo)
print ("El tamaño de la cadena es:", len(nombre_completo))

# Acceder a rango de cadena
cadnueva = "salp050607uu0@pablo@unuyushuajary@123"#rfc 13 carac@nombre???caract@apodo???carac@3digitos
cadsplit = cadnueva.split()
print(cadsplit)
print(cadnueva)
rfc = cadnueva[:12]#Slicing
partemiddle = cadnueva[13:20]
print("rfc ",rfc)
print("parte middle",partemiddle)

print(nombre_completo)
print ("Acceso a rango de cadena: ", nombre_completo[3:13])
print ("A partir de los primeros 5: ", nombre_completo[4:])#checar 0,4 
print ("Acceso a todo: ", nombre_completo[:])
# Formato de impresión de cadena usando la función format()
print ("El nombre es '{nombre}', con un tamaño de: {tamano} ".format(
	nombre=nombre_completo, tamano=len(nombre_completo)))

