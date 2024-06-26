def mensagem(nome):
    print("Executando mensagem")
    return f'Oi {nome}'

def mensagem_longa(nome):
    print("Executando mensagem longa")
    return f'Olá, tudo bem com você {nome}?'

def executar(funcao, nome):
    print("Executando executar")
    return funcao(nome)

print(executar(mensagem, 'Maria'))
print(executar(mensagem_longa, 'Maria'))