import zipfile
from zipfile import ZipFile
with zipfile.ZipFile('archivo.zip', 'w') as fzip:
    fzip.write('Python.docx')
    fzip.write('Archivo.docx')
    fzip.write('python_logo.png')
    fzip.printdir()
    fzip.extractall()
