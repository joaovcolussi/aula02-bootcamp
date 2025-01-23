# Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# def somar(n1,n2):
#   return n1+n2
# inserirNumero1 = int(input("Digite o primeiro número \n"))
# inserirNumero2 = int(input("Digite o segundo número \n"))
# print(f"O resultado é : {somar(inserirNumero1,inserirNumero2)} ")

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# def restoDivisao(numero):
#   return numero / 5
# inserirNumero = float(input("Digite o número: "))
# print(f"O resto do número que digitou :{restoDivisao(inserirNumero)}")


# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# def multiplicacao(numero1, numero2):
#   return numero1 * numero2
# inserirNumero1 = float(input("Digite o primeiro número\n"))
# inserirNumero2 = float(input("Digite o segundo número\n"))
# print(f"A multiplicação de {inserirNumero1} * {inserirNumero2} é {multiplicacao(inserirNumero1,inserirNumero2)}")

# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# def divisaoNumeros(numero1,numero2):
#   return numero1 / numero2
# inserirNumero1 = int(input("Digite o primeiro número: \n"))
# inserirNumero2 = int(input("Digite o segundo número: \n"))
# print(f"A divisão do número {inserirNumero1} / {inserirNumero2} é {divisaoNumeros(inserirNumero1,inserirNumero2)}")

# Escreva um programa que receba dois números flutuantes e realize sua adição.
# def somaAdicao(numero1,numero2):
#   return numero1 +numero2
# num1 = float(input("Digite o primeiro número: \n"))
# num2 = float(input("Digite o segundo número: \n"))
# print(f"A soma de {num1} + {num2} é {somaAdicao(num1,num2)}")

# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# def numeroMedia(n1,n2):
#   return (n1+ n2) / 2
# inserirNumero1 = float(input("Digite o primeiro número: \n"))
# inserirNumero2 = float(input("Digite o segundo número: \n"))
# print(f"A média das notas {inserirNumero1} + {inserirNumero2} é {numeroMedia(inserirNumero1,inserirNumero2)}")
#

# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# def potenciaNumero (base,expoente):
#   return base ** expoente
# base = int(input("Digite o número da base: \n"))
# expoente = int(input("Digite o número do expoente: \n"))
# print(f"O número {base} elevado a potencia {expoente} é {potenciaNumero(base,expoente)}")


# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# def celciusParaFarenheit(celsius):
#   return (celsius * 9/5) + 32
# inserirTemp = int(input("Digite a temperatura em fahrenheit :"))
# print(f"A temperatura em celsius0 é {celciusParaFarenheit(inserirTemp)}")

# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# import math
# raio = float(input("Digite o valor do raio: "))
# area = math.pi * raio ** 2
# print(f"A area do circulo com raio {raio} é {area:.2f}")

# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# EscrevaString = input("Escreva algo que gosta\n")
# ConverterString = EscrevaString.upper()
# print(ConverterString)

# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# EscrevaNome = input("Digite seu nome: \n")
# ConverterNome = EscrevaNome.lower()
# print(ConverterNome)

# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# escrevaFrase = input("Digite uma frase: \n")
# converterFrase =  escrevaFrase.strip(" ")
# print(converterFrase)

# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# escrevaAno = input("Digite o ano em formato dd/mm/aaaa \n")
# converterAno = escrevaAno.split("/")
# print(converterAno)

# Escreva um programa que concatene duas strings fornecidas pelo usuário.
# escrevaString1= input("Digite algo: \n")
# escrevaString2 = input("Digite algo para complementar \n")
# juntarStrings = escrevaString1 +" " +  escrevaString2
# print(juntarStrings)


# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Valor1 = True
# Valor2 = False
# resultado = Valor1 and Valor2
# print(f"Resultado é {resultado}")


# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Valor1 = True
# Valor2 = False
# resultado = Valor1 or Valor2
# print(f"Resultado {resultado}")


# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# valorVerdadeiro = True
# resultado_not = not valorVerdadeiro
# print(resultado_not)

# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Valor1 = 1
# Valor2 = 2
# resultado_igual = (Valor1 == Valor2)
# print(resultado_igual)

# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# valor1= 2
# valor2= 3
# resultadoDiferente = (valor1 != valor2 )
# print(resultadoDiferente)


#Calculo do KPI
CONSTANTE_BONUS = 1000
nomeUsuario = input("Digite seu nome: ")
salarioUsuario = float(input("Digite seu salário: "))
bonusUsuario = float(input("Digite o valor do bonus: "))
valorBonus = CONSTANTE_BONUS + salarioUsuario * bonusUsuario
print(f"O usuário {nomeUsuario} possui o bonus de {valorBonus}")

