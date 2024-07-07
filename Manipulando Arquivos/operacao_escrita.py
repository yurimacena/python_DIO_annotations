arquivo = open("/home/yuri/Documentos/GitHub/python_DIO_annotations/manipulando_arquivos/teste.txt", "w"
)
arquivo.write('Escrevendo dados em um novo arquivo.')
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()