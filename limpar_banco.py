from database import conexao, cursor

cursor.execute("DELETE FROM entrada")
conexao.commit()

cursor.execute("ALTER TABLE entrada AUTO_INCREMENT = 1")

print("Tabela entrada limpa com sucesso!")