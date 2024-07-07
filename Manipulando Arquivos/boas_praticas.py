# BLOCO WITH PERMITE TRABALHAR COM ARQUIVOS DE FORMA SEGURA, GARANTINDO QUE ELES SEJAM FECHADOS CORRETAMENTO, MESMO EM CASO DE EXCEÇÕES
#from pathlib import Path

#ROOT_PATH = Path(__file__).parent

#with open(ROOT_PATH / "lorem.txt", "r") as arquivo:
#    1 / 0

#print(arquivo.read())


# VERIFIQUE SE O ARQUIVO FOI ABERTO COM SUCESSO

from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "Ilorem.txt", "r") as arquivo:
        print(arquivo.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


# USE A CODIFIAÇÃO CORRETA

#try:
#    with open(ROOT_PATH/'arquivo-utf-8.txt', encoding='utf-8') as arquivo:
#        arquivo.write("Aprendendo a manipular arquivos utilizando Python")
#except IOError as exc:
#        print(f"Erro ao abrir o arquivo. {exc}")

try:
    with open(ROOT_PATH/'arquivo-utf-8.txt', encoding='utf-8') as arquivo:
        print(arquivo.read())
except IOError as exc:
        print(f"Erro ao abrir o arquivo. {exc}")
except UnicodeDecodeError as exc:
        print(exc)
