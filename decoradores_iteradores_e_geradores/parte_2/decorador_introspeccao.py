import functools

def meu_decorador(funcao):
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f"Olá {nome}!")
    return nome.upper()

print(ola_mundo.__name__)