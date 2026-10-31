from database import conexao, cursor

class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats() <=0:
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

# Consultando passageiros já cadastrados
cursor.execute("SELECT nome FROM entrada")

resultado = cursor.fetchall()

# Recuperando os passageiros do banco
for passageiro in resultado:
    flight.passengers.append(passageiro[0])

nome = input("Digite o nome do passageiro: ")


sucesso = flight.add_passenger(nome)

if sucesso:
    cursor.execute(
        "INSERT INTO entrada (nome) VALUES (%s)",
        (nome,)
    )
    conexao.commit()
    print(f"{nome} foi adicionado ao voo com sucesso!")

else:
    print("Não existem vagas disponíveis!")

print("Passageiros:", flight.passengers)
print("Vagas disponíveis:", flight.open_seats())