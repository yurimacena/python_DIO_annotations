É a capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai (base).

### Benefícios da herança

- Representa os relacionamentos do mundo real.
- Fornece reutilização de código, não precisamos escrever o mesmo código repetidamente.
- É de natureza transitiva.

### Sintaxe

class A:
    pass

class B(A):
    pass


### Herança simples e múltipla

Simples: Quando uma classe filha de apenas um classe base.

Múltiplas: Quando uma classe filha herda de várias classes base.
EX:

class A:
    pass

class B:
    pass

class C(A, B):
    pass