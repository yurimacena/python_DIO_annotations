class Pessoa:
    def __init__(self, nome, ano_nasc):
        self.nome = nome
        self._ano_nasc = ano_nasc

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nasc
    
    #def get_nome(self):
        #return self._nome
    
    #def get_idade(self):
        #return 2024 - self._ano_nasc
    

pessoa = Pessoa("Azammed", 2010)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
#print(f"Nome: {pessoa.get_nome()} \tIdade: {pessoa.get_idade()}")