from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascaraBR = '%d/%m/%Y %a'
mascaraEN = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascaraBR))

data_convertida = datetime.strptime(data_hora_str, mascaraEN)
print(data_convertida)
print(type(data_convertida))