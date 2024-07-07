**Evite isto:**
id = 1
cursor.execute("SELECT * FROM minha_tabela WHERE id = " + str(id))

**Faça isto:**
id = 1
cursor.execute("SELECT * FROM minha_tabela WHERE id = ?", (id,))

**NOTA:**evite concatenação do primeiro tipo para evitar sql injection