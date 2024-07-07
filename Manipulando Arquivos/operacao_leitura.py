arquivo = open(
    "/home/yuri/Documentos/GitHub/python_DIO_annotations/manipulando_arquivos/lorem.txt", "r"
    )
print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

#tip
#while len(linha := arquivo.readline()):
#    print(linha)
arquivo.close()