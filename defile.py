from os import name
import xml.etree.ElementTree as ET

tree = ET.parse('carros.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter('owner')])
print([elem.attrib for elem in root.iter('owner')])

print("#############################")

for lr in root.findall("./carro/owner[@name='salvador']"):
    print(lr.tag, lr.attrib, lr.text)
    print(type(lr.tag), type(lr.attrib), type(lr.text))


vo = root.find("./carro/owner[@name='equis']")
print(vo)#Objeto

vo.attrib["name"] = "whatever"
print("el otro",vo)
print(type(vo.attrib))
ono = vo
print("el otro",ono)
print(type(ono.attrib))
ono.attrib["name"] = "equis"
print("el otro que no es ono ",vo.attrib)

tree.write("carrosss.xml")