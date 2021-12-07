import xml.etree.ElementTree as ET

tree = ET.parse('carrosss.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)


print(root[0][2].text)

algo = root.find("./carro/owner[@name='salvador']")
print(algo.attrib)
algoDos = root.find("./carro/owner[@name='equis']")
print(algoDos.attrib)
algoDos.append(algo)

nuevo = ET.SubElement(algo,'color')
nuevo.attrib["densidad"] = "muy denso"

print(ET.tostring(algo))

#tree.write("mod.xml")