Classe: define as características e comportametos de um objeto, porém não conseguimos usá-las diretamente.

Objetos: podemos usá-los e eles possuem as características e comportametos que foram definidos nas classes.

### Classe

class Cachorro:
    def init(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzzz...")


### Objeto

cao_1 = Cachorro("chappie", "amarelo", False)
cao_2 = Cachorro("Aladim", "branco e preto")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)