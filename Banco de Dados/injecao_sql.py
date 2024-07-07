import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")
#demonstração de um vazamento de dados e erro grave de segurança se id={id_cliente}

clientes = cursor.fetchall()

for cliente in clientes:    
    print(dict(cliente))
