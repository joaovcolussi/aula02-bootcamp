# x = int(input("Please enter an Integer: "))

# if x <0:
#   x = 0
#   print("Negative changed to zero")
# elif x ==0:
#   print("Zero")
# elif x ==1:
#   print("Single")
# else:
#   print("More")


# quantidade = 10
# preco = 20

# if quantidade> 0 and preco > 0:
#   print("Dados válidos")
# else:
#   print("Dados Inválidos")

# temperatura = 22

# if temperatura < 18:
#   print("baixa")
# elif 18<= temperatura <= 26:
#   print("normal")
# else:
#   print("Alta")

# log = {'timestamp' : '2021-06-23 10:00:00', 'level' : 'ERROR', 'message' : 'Falha na conexão' }

# if log['level'] == 'ERROR':
#   print(log['message'])

# idade = 25
# email = "usuario@exemplo.com"

# if not 18 <= idade <=65:
#   print("Idade fora do intervalo permitido")
# elif "@" not in email or "." not in email:
#   print("Email Inválido")
# else:
#   print("Dados de usuários válidos")


transacao = {'valor': 12000, 'hora' : 20}

if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
  print("Transação suspeita")
else:
  print("Transação normal")