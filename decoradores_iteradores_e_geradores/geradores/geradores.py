def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

#quando usar gerador?
# quando o código for mais simples

#quando usar iterador?
# quando o código for mais complexo, usando de classes e estruturas extensivas