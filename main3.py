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


# transacao = {'valor': 12000, 'hora' : 20}

# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#   print("Transação suspeita")
# else:
#   print("Transação normal")

# words = ['cat','windo', 'defemestrate']
# for w in words:
#   print(w, len(w))

# nome = ['Luciano']
# for letra in nome:
#   print(letra)

#   for i in range(5):
#     print(i)

# list(range(5,10))
# [5,6,7,8,9]
# list(range(0,10,3))
# [0,3,6,9]
# list(range(-10,-100,-30))
# [-10,-40,-70]

# a = ['mary','had', 'a', 'little','lamb']
# for i in range(len(a)):
#   print(i, a[i])

# texto = "a raposa marrom salta sobre o cachorro preguiçoso"
# palavras = texto.split()
# contagem_palavras = {}

# for palavra in palavras:
#   if palavra in contagem_palavras:
#     contagem_palavras +=1
#   else:
#     contagem_palavras[palavra] = 1
# print(contagem_palavras)

# numeros = [10,20,30,40,50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

# usuarios = [
#   {"nome" : "alice", "email": "alice@example.com"},
#   {"nome" : "bob" , "email" : ""},
#   {"nome" : "Carol", "email" : "carolexample.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)

# numeros = range(1,11)
# pares = [x for x in numeros if x % 2 ==0]

# print(pares)

# vendas = [
#   {"categoria": "eletrônicos" , "valor" : 1200},
#   {"categoria" : "livros", "valor" : 200},
#   {"categoria" : "eletrônicos" , "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#   categoria = venda["categoria"]
#   valor = venda["valor"]
#   if categoria in total_por_categoria:
#     total_por_categoria[categoria] += valor
#   else:
#     total_por_categoria[categoria] = valor

# print(total_por_categoria)


# import time

# while True:
#   print("Verificando novos dados")

#   time.sleep(10)


# dados = []
# entrada = ""

# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":
#         dados.append(entrada)

# print("Valores digitados:", dados)


pagina_atual = 1
paginas_totais = 5

# while pagina_atual <= paginas_totais:
#   print(f"Processando página {pagina_atual} de {paginas_totais}")
#   pagina_atual +=1

# print("Todas as páginas foram processadas.")

# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#   print(f"Tentativa {tentativa} de {tentativas_maximas}")

#   if True:
#     print("Conexão bem-sucedida!")
#     break
#   tentativa +=1
# else:
#   print("Falha ao conectar após várias tentativas.")

# itens = [1,2,3, "parar", 4, 5]

# i = 0
# while i < len(itens):
#   if itens[i] == "parar":
#     print("Parada encontrada, encerrando o processamento.")
#     break
#   print(f"Processando item:  {itens[i]}")
#   i += 1


nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
  try:
    nome = input("Digite seu nome: ")
    if len(nome) == 0:
      raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
      raise ValueError("O nome não deve conter números.")
    else:
      print("Nome válido", nome)
      nome_valido = True
  except ValueError as e:
      print(e)

  while not salario_valido:
    try:
      salario = float(input("Digite o valor do seu salário: "))
      if salario < 0:
        print("Por favor, digite um valor do seu salário.")
      else:
        salario_valido = True
    except ValueError:
        print("Entrada Inválida para o salário. Por favor, digite um número.")

while not bonus_valido:
  try:
    bonus = float(input("Digite o valor do bônus recebido: "))
    if bonus < 0:
      print("Por favor, digite um valor positivo para o bônus")
    else:
      bonus_valido = True
  except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

bonus_recebido = 1000+ salario * bonus

print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")