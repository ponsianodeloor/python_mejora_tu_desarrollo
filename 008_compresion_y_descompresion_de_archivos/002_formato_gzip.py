import gzip
with open('Python.docx', 'rb') as original:
    with gzip.open('archivo.txt.gz', 'wb') as archivo_1:
        archivo_1.writelines(original)
