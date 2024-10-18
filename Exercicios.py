print("hello world!")

valorA = float(input("insira um valor de 1 - 20: "))
valorB = float(input("insira um valor de 1 - 20: "))
print(valorA+valorB)
média = (valorA+valorB)
soma = (média/2)
print(soma) 
tf = float(input("insira a temperatura em fahrenheit: "))
tc = (tf-32)*5/9)
print(tc)
if tc > 30:
  print("está quente")
-------------------------------------------------------------------------------------
#EX0.1
"""
Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade = input("insira a sua idade: ")
nome = input("insira o seu nome: ")
print(f"o meu é {nome} e tenho {idade} anos. "); 
-------------------------------------------------------------------------------------
#EX0.2
""" 
Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print("olá mundo!");
fruta = "banana"; 
print(f"eu gosto de {fruta}");
-------------------------------------------------------------------------------------
#EX0.3
"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número.
"""
nome = input("digite o seu nome: ")
print(f"Como é que tamos oh irmoum, {nome}, é tass bem!")
valor = int(input("insira um número: ")
dobro = valor * 2 
print(f"o dobro de {valor} é {dobro}")
-------------------------------------------------------------------------------------
#EX1.1
"""
Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco
"""

a = "\n"
print("\nBem-vindos ao Python!")
-------------------------------------------------------------------------------------
#EX1.2 
"""
Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco
"""
a = "\n"
print("\nJosé, bem-vindo ao Python!")
-------------------------------------------------------------------------------------
#EX1.3
"""
Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável.
"""
carro = "Mazda RX7"
print(carro)
print(f"\nO meu carro é {carro}.")
-------------------------------------------------------------------------------------
#EX1.4
"""
Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis.
"""
nome = "Orochi"
idade = "14"
localidade = "Cabeçudos"
print(f"O meu nome é {nome}, tenho {idade} anos e moro em {localidade}.")
-------------------------------------------------------------------------------------
#EX1.5
"""
Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem
"""
linguagem = "Python"
nome = "Orochi"
print(f"Estou a aprender {linguagem} e o meu nome é {nome}. ")
------------------------------------------------------------------------------------
#EX1.6
"""
Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres.
"""
print(f"{'left aligned text' : <50}")
print(f"{'center aligned text' : ^50}")
print(f"{'right aligned text' : >50}")


print(f"{'Bem vindos ao Python' : <50}")
print(f"{'Bem vindos ao Python' : ^50}")
print(f"{'Bem vindos ao Python' : >50}")
------------------------------------------------------------------------------------
#EX1.7
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.
"""
raio = float(input("insira o raio:"))
perimetro = 2 * 3.14 * raio
area = 3.14 * raio ** 2
print(f"o perimetro é {perimetro} e a area é {area}") 
------------------------------------------------------------------------------------
#EX1.8
"""
Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
- 02-10-2024
- 02-10-2024 16:11:20
- 10-02-2024 16:11:20
- 02/10/24
- 16:11:20
""" 
import datetime 
data = datetime.datetime.now()
dia = data.strftime("%d")
mes = data.strftime("%m")
ano = data.strftime("%Y")
hora = data.strftime("%H")
minutos = data.strftime("%M")
segundos = data.strftime("%S")
print(f"{dia}-{mes}-{ano}")
print(f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print(f"{mes}/{dia}/{ano}")
print(f"{hora}:{minutos}:{segundos}")
------------------------------------------------------------------------------------
#EX1.9
"""
Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos.
"""
numero = int(input("insira o número do atleta: "))
pontos = float(input("insira a pontuação final: "))
print(f"o atleta número {numero} obteve {pontos} pontos. ")
------------------------------------------------------------------------------------
#EX1.10
"""
Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual.
"""
import datetime
data = datetime.datetime.now()
dia = data.strftime("21")
mes = data.strftime("10")
ano = data.strftime("2024")
print(f"{dia}-{mes}-{ano}")
------------------------------------------------------------------------------------
#EX1.11
"""
Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO).
"""
libras = float(input("insira o valor em libras:"))
euros = libras * 1.19
print(f"o valor em euros é {euros}")
------------------------------------------------------------------------------------
nota = float(input("insira a nota: "))

if nota > 10: 
    print("nota é maior que 10")
elif nota == 10: 
    print("nota é igual a 10")
else:
    print("nota é menor que 10")
------------------------------------------------------------------------------------
#A28
"""
Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o utilizador tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o utilizador ganhou ou perdeu.
"""
import random

segredo = int(random.randint(0, 5))
# print(f"o número secreto é: {segredo}")

numeroescolhido = int(input("insira um número entre (0 e 5): "))

if numeroescolhido > segredo:
    print("o número inserido é maior que o meu!")
elif numeroescolhido < segredo:
    print("o número inserido é menor que o meu!")

print("Acertaste o meu número")
------------------------------------------------------------------------------------
#A29 
"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem a dizer que ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.
"""
velocidade = float(input("insira a velocidade do carro: "))
multa = velocidade - 80
valor = multa * 7
if velocidade > 80:
  print(f"excedeste a velocidade em {multa}km/h e vais ter de pagar {valor}€ de multa")
else:
  print("estavas na velocidade certa!")
------------------------------------------------------------------------------------
#FP1
"""
Verificar se um número é positivo, negativo ou zero.
Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else.
"""
numero = float(input("insira um número: "))

if numero > 0:
  print(f"o número {numero} é positivo")
elif numero == 0:
  print(f"o número {numero} é igual a zero")
else:
  print(f"o número {numero} é negativo")
------------------------------------------------------------------------------------
#FP2
"""
Verificar se um número é par ou ímpar.
Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %.
"""
numero = int(input("insira um numero: "))
if numero % 2 == 0:
  print(f"o numero {numero} é par")
elif numero % 2 != 0:
  print(f"o numero {numero} é impar")
------------------------------------------------------------------------------------
#FP3
"""
Calcular a nota final de um aluno.
Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:
"""
nota = float(input("insira a nota: "))

if nota < 10: 
  print(f"tás reprovado")
elif nota > 10 and nota > 14: 
  print(f"suficiente")
elif nota > 15 and nota > 17: 
  print(f"bom")
elif nota > 17: 
  print(f"muito Bom")
else:
  print(f"Insira uma nota válida")
------------------------------------------------------------------------------------
##FP4 
"""
Conversor de temperaturas.
Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.


Fórmulas: 
Fahrenheit = Celsius * 9/5 + 32 
Kelvin = Celsius + 273.15
"""

temperatura = float(input("insira a temperatura em graus Celsius: "))
unidade =str(input("insira a unidade de destino (Fahrenheit(F), Kelvin(K) ou Ambas(A)"))

if unidade == "Fahrenheit":
  fahrenheit = temperatura * 9/5 + 32
  print(f"a temperatura em Fahrenheit é {temperatura}")
elif unidade == "Kelvin":
  kelvin = temperatura + 273.15
  print(f"a temperatura em Kelvin é {temperatura}")
if unidade== "A":
  print(f"o valor em fahrenheit é {fahrenheit} e em Kelvin é {Kelvin}")
else:
  print("Opção inválida")
------------------------------------------------------------------------------------
#FP5
"""
Cálculo de impostos
Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:

Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto.
"""
salario = int(input("insira o seu salário mensal: "))
if salario <= 1000:
  print(f"isento de impostos")
elif salario > 1000 and salario <= 2000:
  imposto = salario * 0.1
  print(f"o seu imposto é {imposto}")
elif salario > 2000:
  imposto = salario * 0.2
  print(f"o seu imposto é {imposto}")
------------------------------------------------------------------------------------
#AC
"""Considere que uma empresa tenha os códigos abaixo para os produto indicados:

100 200 300 400 500
Prego Parafuso Anilha Agulha Tesoura
Crie um pseudocódigo que peça o código do produto e mostre o respetivo produto. Em
caso de não existir o código, deve apresentar uma mensagem de erro. Utilize a instrução
"""
codigo = int(input("insira o código do produto: "))
if codigo == 100:
  print("Prego")
elif codigo == 200:
  print("Parafuso")
elif codigo == 300:
  print("Anilha")
elif codigo == 400:
  print("Agulha")
elif codigo == 500:
  print("Tesoura")
else:
  print("Código inválido")
------------------------------------------------------------------------------------
#FP6 
"""
Imprimir números de 1 a 10.
Escreve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
"""
for i in range(1, 11):
  print(i)
------------------------------------------------------------------------------------
#FP7
"""
Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.
"""
#inicializar variáveis
soma = 0
i = 1
#utilizar o ciclo while para somar de 1 a 100 
while i <= 100:
  soma += i
  i += 1
#mostrar o resultado na consola
print(f"a soma de 1 a 100 é: {soma}")

------------------------------------------------------------------------------------
#FP8 
"""
Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.
"""
frase = input("insira uma frase: ")
vogais = 0
for letra in frase:
  if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"or letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    vogais += 1
print(f"A frase tem {vogais} vogais")
------------------------------------------------------------------------------------
#FP9
"""
Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.
"""
temporario = 0
for i in range(1, 51):
  if temporario <= 49:
    temporario = i * 5
    print(temporario)
------------------------------------------------------------------------------------
#FP10
"""
Verificar se um número é primo.
Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.
"""
lista = []
for i in range(5):
  numero = int(input("insira um numero: "))
  lista.append(numero)
soma = 0
for i in lista:
  soma = soma + i
media = soma / 5
print(f"A média dos numeros é {media}")
----------------------//----------------------------------
notas = []
for i in range(0,5):
  numeros = int(input("insira um valor inteiro: "))
  notas.append(numeros) #adiciona um elemento á lista
soma = sum(notas) #calcula a soma de todos os elementos dentro da lista
x = len(notas) #devolve o número total de elementos da lista
media = (soma / x) #calcula a média 
print(media)

------------------------------------------------------------------------------------
#FP11
"""
Média de uma lista de números.
Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
"""
numero = int(input("insira um numero: "))
divisores = 0 
for i in range(1, numero + 1):
  if numero % i == 0: #verifica se o resultado da divisão é 0
    divisores += 1 #incrementa o contador de divisores
if divisores == 2: 
  print(f"o {numero} é um número primo")
else:
  print(f"o {numero} não é um número primo")
------------------------------------------------------------------------------------
#FP12
"""
Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.
"""
lista = [] #variável
for i in range(1,21): #ciclo for
  if i % 2 == 0: #verifica se o resto da divisão é 0
    lista.append(i) #adiciona o elemento à lista
print(lista) #imprime a lista
------------------------------------------------------------------------------------
#FP13
"""
Inverter uma string.
Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
"""
palavra = input("insira uma palavra ou frase: ")
palavra_invertida = ""
for i in range(len(palavra) -1, -1, -1):
  palavra_invertida += palavra[i]
print(palavra_invertida)
----------------------//-----------------------
texto = str(input("insira um texto: ")) #pedir o texto ao utilizador
textoinv = texto [::-1] #script para inverter o texto
print(textoinv) #imprimir o texto invertido
------------------------------------------------------------------------------------
#FP14
"""
Tabuada de multiplicação
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.
"""
numero = int(input("insira um numero: "))
for i in range(1, 11):
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
------------------------//----------------------
numero = int(input("insira um numero: "))
while i <= 10:
  resultado = numero * i
  print(f"{numero} x {i} = {resultado}")
  i += 1
------------------------------------------------------------------------------------
#FP15
"""
Fatorial de um número
Escreve um programa que utilize um ciclo while para calcular o fatorial de um número introduzido pelo utilizador. O fatorial de um número n (n!) é o produto de todos os números inteiros positivos até n.
"""
numero = int(input("insira um numero: "))
fatorial = 1
i = 1
while i <= numero:
  fatorial *= i
  i += 1
print(f"o fatorial de {numero} é {fatorial}")
------------------------------------------------------------------------------------
