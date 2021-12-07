import xml.etree.ElementTree as ET

#XML JSON
cadxml = '''
<carros>
<carro>
    <dispositivo> Nissan </dispositivo>
    <numserie> u2h34u859ole </numserie>
    <owner name="salvador">yo</owner>
</carro>
<carro>
    <dispositivo> Dispositivo Dos </dispositivo>
    <numserie> ipoi54i464o </numserie>
    <owner name="salvador"> yo dos </owner>
</carro>
<carro>
    <dispositivo> Dispositivo Tres </dispositivo>
    <numserie> 1234125454dgf </numserie>
    <owner name="pablo" otro="equis"> yo tres</owner>
</carro>
</carros>
'''

tree = ET.fromstring(cadxml)  #json.loads(cadjson)
lista = tree.findall('carros/carro') #Lectura por Keys y Items, directamente en un For
print(len(lista))

listados = tree.findall('carro')
print(len(listados))


for item in listados:
    print('Dispositivo: ', item.find('dispositivo').text) #item['dispositivo']
    print('Num serie: ', item.find('numserie').text)
    print('Owner: ', item.find('owner').text)
    print('Owner Atributte: ', item.find('owner').attrib)

#print('Marca: ', tree.find('dispositivo').text)
#print('Owner: ',tree.find('owner').text)

#root = tree.getroot()