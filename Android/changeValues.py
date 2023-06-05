from xml.dom import minidom
import xml.etree.ElementTree as ET
import random
from googletrans import Translator

translator = Translator()

number_of_variables = 20
ids_values = {}
random_values_list = []
strings_to_translate = []
values_list = []

# parse an xml file by name
file = minidom.parse('strings.xml')

#a linha seguinte é lendo o arquivo para modificar o valor das strings no xml
filename = "strings.xml"
xmlTree = ET.parse(filename)
rootElement = xmlTree.getroot()

#use getElementsByTagName() to get tag
strings = file.getElementsByTagName('string')



for elem in strings:

#    ids_values[elem.attributes['name'].value] = elem.firstChild.data
    values_list.append([elem.attributes['name'].value, elem.firstChild.data])

for i in range(number_of_variables):
    random_values_list.append(random.choice(values_list ))

#print(random_values_list)

#print(random_values_list[1].append('pipipopo'))

for elem in random_values_list:
    translated_string = translator.translate(elem[1], dest='en')
    print(translated_string.text)
    elem.append(translated_string.text)

print(random_values_list)

for element in rootElement.findall("string"):
    for list in random_values_list:
        if element.get('name') == list[0]:
            element.text = list[2]

xmlTree.write(filename,encoding='UTF-8',xml_declaration=True) 


    

    


