# try:
#   numero01= int(input("Inserir um número inteiro: "))
#   numero02= int(input("Inserir outro número inteiro: "))
#   resultado = numero01 // numero02
#   print(f"O valor que inseriu é {resultado}")
# except ZeroDivisionError:
#   print("Não da para dividir por zero!")
# except KeyboardInterrupt:
#   print("Código Interrompido!")
# except ValueError:
#   print("Acho que você não quis inserir um número!")

nome = "joão"

try:
  resultado = len(nome)
  print(resultado)
except TypeError as e:
  print(e)
else:
  print("Tudo ocorreu bem")