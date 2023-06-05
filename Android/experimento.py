import xml.etree.ElementTree as ET


filename = "strings.xml"
xmlTree = ET.parse(filename)
rootElement = xmlTree.getroot()

for element in rootElement.findall("string"):
    if element.get('name') == 'AppName':
        element.text = 'Mudei aqui mô'

xmlTree.write(filename,encoding='UTF-8',xml_declaration=True) 