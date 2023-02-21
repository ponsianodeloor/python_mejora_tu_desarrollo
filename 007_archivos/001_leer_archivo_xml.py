from xml.dom.minidom import parse, Node

xmltree = parse('note.xml')

for nodo in xmltree.getElementsByTagName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print(nodo_hijo.data)
