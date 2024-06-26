#class Iterador:
    #def __iter__(self):
     #   pass

    #def __next__(self):
     #   raise StopIteration

#for i in Iterador():
 #   print(i)

class Iterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in Iterador(numeros=[38, 13, 11]):
    print(i)