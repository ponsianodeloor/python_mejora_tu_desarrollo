from xml.etree.ElementTree import parse

xml_doc = parse('note.xml')
for etiqueta in xml_doc.findall('pro'):
    print(etiqueta.text)