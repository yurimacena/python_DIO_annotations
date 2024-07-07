import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

#OUTRA ESTRUTURA:
#with sqlite3.connect(ROOT_PATH / "meu_banco.db") as conexao:
#    conexao.commit()

try:
    cursor.execute("DELETE FROM clientes WHERE id=8;")
    conexao.commit()

    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)", ("Teste 3", "teste3@gmail.com"))
    cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)", (2, "Teste 4", "teste4@gmail.com"))
    conexao.commit()
except Exception as exc:
    print(f"Ops! Um erro ocorreu! {exc}")
    conexao.rollback()