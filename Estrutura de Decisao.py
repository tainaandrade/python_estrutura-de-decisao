#!/usr/bin/env python
# coding: utf-8

# ## 1.Faça um Programa que peça dois números e imprima o maior deles.

# In[2]:


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print("O primeiro número (",num1,") é maior")
else:
    print("O segundo número (",num2,") é maior")


# ## 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

# In[ ]:


valor = int(input("Digite um número: "))

if valor < 0:
    print("O valor é negativo")
else:
    print("O valor é positivo")


# ## 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

# In[ ]:


sexo = input("Digite a letra do seu sexo: ").upper()

if sexo == 'F':
    print("F - Feminino")
elif sexo == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido")


# ## 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[ ]:


letra = input(str("Digite uma letra: ")).upper()

if letra == ('A' or 'E' or 'I' or 'O' or 'U'):
    print("A letra digitada é uma vogal")
else: 
    print("A letra digitada é uma consoante")


# ## 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

# #### A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# #### A mensagem "Reprovado", se a média for menor do que sete;
# #### A mensagem "Aprovado com Distinção", se a média for igual a dez.

# In[ ]:


nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7 and media <=9:
    print("Aprovado")
elif media >= 10:
     print("Aprovado com Distinção")
else:
     print("Reprovado")

   


# ## 6. Faça um Programa que leia três números e mostre o maior deles.
# 

# In[ ]:


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2) or (num1 > num3):
    print("O primeiro número (",num1,") é maior")
    
elif (num2 > num1) or (num2 > num3):
    print("O segundo número (",num2,") é maior")
    
elif (num3 > num1) or (num3 > num2):
    print("O terceiro número (",num3,") é maior")
    
else:
    print("Empate")


# ## 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
# 

# In[ ]:


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

def maior_numero():
    if (num1 > num2) and (num1 > num3):
        print("O primeiro número (",num1,") é maior")

    elif (num2 > num1) and (num2 > num3):
        print("O segundo número (",num2,") é maior")

    elif (num3 > num1) and (num3 > num2):
        print("O terceiro número (",num3,") é maior")
        
    
        
def menor_numero():
    if (num1 < num3) and (num1 < num2):
        print("O primeiro número (",num1,") é menor")

    elif (num2 < num3) and (num2 < num1):
        print("O segundo número (",num2,") é menor")

    elif (num3 < num1) and (num3 < num2):
        print("O terceiro número (",num3,") é menor")
    
    else:
        print("Empate")
maior_numero()        
menor_numero()


# ## 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# 

# In[ ]:


produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

if (produto1 < produto2) and (produto1 < produto3):
    print("O produto mais barato é de: ", "%.2f" % produto1)
    
elif (produto2 < produto1) and (produto2 < produto3):
    print("O produto mais barato é de: ", "%.2f" % produto2)
    
elif (produto3 < produto1) and (produto3 < produto2):
    print("O produto mais barato é de: ", "%.2f" % produto3)
    


# ## 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

# In[ ]:


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

numeros = [num1, num2, num3]

numeros.sort(reverse=True)

print(numeros)


# ## 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# 

# In[ ]:


turno = str(input("Digite o turno que você estuda:\n M-matutino \n V-Vespertino \n N- Noturno\n ")).upper()

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print("Boa tarde!")
elif turno == 'N':
    print("Boa noite!")

else:
    print("Valor Inválido")


# ## 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# In[ ]:


salario = float(input("Digite o seu salário: "))


## salários até R$ 280,00 (incluindo) : aumento de 20%
if salario <= 280:
    novo_salario = salario * 0.20
    print("Salário antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 20%")
    print("Valor do aumento: ", novo_salario)
    print("Seu salário de", salario, "foi para:", salario + novo_salario)
    
## salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
elif salario > 280 and salario < 700:
    novo_salario = salario * 0.15
    print("Salário antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 15%")
    print("Valor do aumento: ", novo_salario)
    print("Seu salário de", salario, "foi para:", salario + novo_salario)
## salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
elif salario > 700 and salario < 1500:
    novo_salario = salario * 0.10
    print("Salário antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 10%")
    print("Valor do aumento: ", novo_salario)
    print("Seu salário de", salario, "foi para:", salario + novo_salario)
## salários de R$ 1500,00 em diante : aumento de 5%
elif salario >= 1500:
    novo_salario = salario * 0.05
    print("Salário antes do reajuste: ", salario)
    print("Percentual de aumento aplicado: 5%")
    print("Valor do aumento: ", novo_salario)
    print("Seu salário de", salario, "foi para:", salario + novo_salario)
    
    


# ### 12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# In[ ]:


vh = float(input("Digite o valor da sua hora: "))
qhtm = float(input("Digite a quantidade de horas trabalhadas no mês: "))

salario_bruto = vh * qhtm 

sindicato = (salario_bruto/100) * 3
ir = 0
inss = (salario_bruto/100) * 10
fgts = (salario_bruto/100) * 11

## Salário Bruto até 900 (inclusive) - isento
if salario_bruto <= 900:
    print("Isento")
    
## Salário Bruto até 1500 (inclusive) - desconto de 5%
elif salario_bruto > 901 and salario_bruto <= 1500:
    ir = (salario_bruto/100) * 5
    salario_liquido = salario_bruto - sindicato - ir - inss
    
## Salário Bruto até 2500 (inclusive) - desconto de 10%
elif salario_bruto > 1501 and salario_bruto <= 2500:
    ir = (salario_bruto/100) * 10
    salario_liquido = salario_bruto - sindicato - ir - inss
    
## Salário Bruto acima de 2500 - desconto de 20%
elif salario_bruto > 2501:
    ir = (salario_bruto/100) * 20
    salario_liquido = salario_bruto - sindicato - ir - inss

    
def impressao(salario_bruto, sindicato, ir, fgts, inss, salario_liquido):
    print("Salário Bruto", salario_bruto)
    print("Sindicato: ", sindicato)
    print("IR: ", ir)
    print("FGTS: ", fgts)
    print("Total Descontos: ",  sindicato + ir+inss)
    print("Salário Líquido: ", salario_liquido)


impressao(salario_bruto, sindicato, ir, fgts, inss, salario_liquido)


# ## 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

# In[ ]:


num = int(input("Digite um número: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Segunda")
elif num == 3:
    print("Terça")
elif num == 4:
    print("Quarta")
elif num == 5:
    print("Quinta")
elif num == 6:
    print("Sexta")
elif num == 7:
    print("Sábado")
else:
    print("Valor Inválido")


# ## 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# In[ ]:


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1+nota2) / 2

if media >= 9.0 and media <=10.0:
    print(" \n Média:", media, "\n Conceito: A \n APROVADO")
    
elif media >=7.5 and media < 9.0: 
    print(" \n Média:", media, "\n Conceito: B \n APROVADO")
    
elif media >=6.0 and media < 7.5: 
    print(" \n Média:", media, "\n Conceito: C \n APROVADO")
    
elif media >=4.0 and media < 6.0: 
    print(" \n Média:", media, "\n Conceito: D \n REPROVADO")
    
elif media < 4.0: 
    print(" \n Média:", media, "\n Conceito: E \n REPROVADO")


# ## 15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# #### Dicas:
# #### Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# #### Triângulo Equilátero: três lados iguais;
# #### Triângulo Isósceles: quaisquer dois lados iguais;
# #### Triângulo Escaleno: três lados diferentes;''

# In[ ]:


lado1 = int(input("Digite o primeiro lado do triângulo: "))
lado2 = int(input("Digite o segundo lado do triângulo: "))
lado3 = int(input("Digite o terceiro lado do triângulo: "))

equilatero = lado1 

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):
    print("Não é um triângulo")
elif(lado1 == lado2) and (lado1 == lado3):
    print("Equilátero")
elif(lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print("Isósceles")
else:
    print("Escaleno")


# ## 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações

# In[ ]:




a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

delta = b**2 - 4*a*c

if a == 0:
    print("Não é uma equação de segundo grau")
    print(delta)
elif delta < 0:
    print("A equação não possui raizes reais")
    print(delta)
else: 
    xmenos = (-b - delta ** 0.5) / 2.0*a 
    xmais = (-b + delta ** 0.5) / 2.0*a
    print("Resultado: ", xmenos, xmais)
    print(delta)
    


# ## 17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

# In[ ]:


ano = int(input("Digite um ano: "))


if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print("Ano bissexto")
else:
    print("Não é bissexto")


# ## 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

# In[ ]:


dia = input("Digite o dia: ")
mes = input("Digite o mês: ")
ano = input("Digite o ano: ")

if dia > "31" or mes > "12":
    print("Data Inválida")
else:
    print(dia,"/",mes,"/",ano, "é uma data válida")
    


# ## 19. Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

# In[ ]:


num = input("Digite um número menor que 1000: ")
result = str(num)
tam = len(result)

def centenas():
    centena = result[0:1]
    dezena  = result[1:2]
    unidade = result[2:3]
    
    if  tam == 3 and int(centena) > 1 and int(dezena) > 1 and int(unidade)  > 1:
        print (centena, "centenas,", dezena, "dezenas e",unidade, "unidades")
        
    elif tam == 3 and int(centena) <= 1 and int(dezena) > 1 and int(unidade)  > 1:
        print (centena, "centena,", dezena, "dezenas e",unidade, "unidades")
        
    elif tam == 3 and int(centena) > 1 and int(dezena) <=1 and int(unidade)  > 1:
        print (centena, "centenas,", dezena, "dezena e",unidade, "unidades")
        
    elif tam == 3 and int(centena) > 1 and int(dezena) > 1 and int(unidade)  <=1:
        print (centena, "centenas,", dezena, "dezenas e",unidade, "unidade")
        
def dezenas():
    dezena  = result[0:1]
    unidade = result[1:2]
    
    if tam == 2 and int(dezena) > 1 and int(unidade)  > 1:
        print (dezena+" dezenas e "+unidade+ " unidades")
    elif tam == 2 and int(dezena) <= 1 and int(unidade)  > 1:
        print (dezena+" dezena e "+unidade+ " unidades")
    elif tam == 2 and int(dezena) > 1 and int(unidade)  <= 1:
        print (dezena+" dezenas e "+unidade+ " unidade")
        
def unidades():
    unidade = result[0:1]
    if tam == 1 and int(unidade)  > 1:
        print (unidade+ " unidades")
    elif tam == 1 and int(unidade)  <= 1:
        print(unidade+ " unidade")
    
    
centenas()
dezenas()
unidades()


# ## 20. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
# #### a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# #### b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# #### c. A mensagem "Aprovado com Distinção", se a média for igual a 10.

# In[ ]:


nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <=9:
    print("Aprovado, média: ", media)
elif media >= 10:
     print("Aprovado com Distinção, média: ", media)
else:
     print("Reprovado, média: ", media)

   


# ## 21. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# In[ ]:


numero = int(input('Valor para sacar [10-600]: '))

cem = int(numero / 100)
numero = numero - (cem*100)

cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

dez = int(numero/10)
numero = numero - (dez*10)

cinco = int(numero/5)
numero = numero - (cinco*5)

um = numero

print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  1,00 = ',um)


# ## 22. Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

# In[ ]:


num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# ## 23. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

# In[ ]:


num = float(input("Digite um número: "))
 
if num == round(num):
    print("Inteiro")
else: 
    print("Decimal")


# ## 24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
# ## O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# ### a. par ou ímpar;
# ### b. positivo ou negativo;
# ### c. inteiro ou decimal.

# In[ ]:


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

operacao = input("Qual o operação você deseja realizar? ")

def def_adicao():
    if adicao % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    if adicao  >= 0:
        print("Positivo")
    else:
        print("Negativo")
    if adicao == round(adicao):
        print("Inteiro")
    else: 
        print("Decimal")
            
if operacao == "Adição":
    print("Resultado:", adicao)
    def_adicao()
        
def def_subtracao():
    if subtracao % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    if subtracao  >= 0:
        print("Positivo")
    else:
        print("Negativo")
    if subtracao == round(subtracao):
        print("Inteiro")
    else: 
        print("Decimal")
            
if operacao == "Subtração":
    print("Resultado:", subtracao)
    def_subtracao()
        
def def_multiplicacao():
    if multiplicacao % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    if multiplicacao  >= 0:
        print("Positivo")
    else:
        print("Negativo")
    if multiplicacao == round(multiplicacao):
        print("Inteiro")
    else: 
        print("Decimal")
            
if operacao == "Multiplicação":
    print("Resultado:", multiplicacao)
    def_multiplicacao()
        
def def_divisao():
    if divisao % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
    if divisao  >= 0:
        print("Positivo")
    else:
        print("Negativo")
    if divisao == round(divisao):
        print("Inteiro")
    else: 
        print("Decimal")
            
if operacao == "Divisão":
    print("Resultado:", divisao)
    def_divisao()


# ## 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# ### "Telefonou para a vítima?"
# ### "Esteve no local do crime?"
# ### "Mora perto da vítima?"
# ### "Devia para a vítima?"
# ### "Já trabalhou com a vítima?" 
# ### O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# In[ ]:


p1 = input("Telefonou para a vítima? ")
p2 = input("Esteve no local do crime? ")
p3 = input("Mora perto da vítima? ")
p4 = input("Devia para a vítima? ")
p5 = input("Já trabalhou com a vítima? ")

lista = [p1, p2, p3, p4, p5]

if lista.count("Sim") == 2:
    print("Suspeita")
elif lista.count("Sim") == 3 or lista.count("Sim") == 4:
    print("Cúmplice")
elif lista.count("Sim") == 5:
        print("Assasino")
else:
    print("Inocente")


# ## 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# ### Álcool:
# #### até 20 litros, desconto de 3% por litro
# #### acima de 20 litros, desconto de 5% por litro
# ### Gasolina:
# #### até 20 litros, desconto de 4% por litro
# #### acima de 20 litros, desconto de 6% por litro 
# 
# ### Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é RS 2,50 o preço do litro do álcool é R$ 1,90.

# In[ ]:





# In[ ]:


qtd_litros = float(input("Qual será a quantidade de litros? "))
combustivel = input("Digite o tipo de combustível. A- Álcool, G-Gasolina ").upper()


if (combustivel == "A"):
    
    if  qtd_litros <=20:
        valor_final = qtd_litros * preco_litro_alcool - (valor_final * 3 / 100)
    else:
        valor_final = qtd_litros * preco_litro_alcool - (valor_final * 5 / 100)
       

    
elif (combustivel == "G"):
    preco_litro_gasolina = 2.5
    if qtd_litros <= 20:
        valor_final = qtd_litros * preco_litro_alcool - (valor_final * 4 / 100)
    else:
        valor_final = qtd_litros * preco_litro_alcool - (valor_final * 6 / 100)
        
print(f"Valor a ser pago com desconto: R${valor_final:.2f}")



# ## 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# ####    ...................
# 

# In[40]:


qtd_morangos = int(input("Digite a quantidade de morangos: "))
qtd_macas = int(input("Digite a quantidade de maçãs: "))



if qtd_morangos > 5:
    total_morango = qtd_morangos * 2.2
else:
    total_morango = qtd_morangos * 2.5
    
if qtd_macas > 5:
    total_maca = qtd_macas * 1.5
else:
    total_maca = qtd_macas * 1.8


print("Quantidade de morangos:", qtd_morangos, "\nQuantidade de morangos:", qtd_macas)
total = total_morango + total_maca
if total > 25 or (qtd_morangos + qtd_macas) > 8:
    
    print("Total de compras com desconto de 10%: ", (total - (total * 0.10)))
else: 
    print("Total de compras: ",total)





# ## 28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

# In[62]:


tipo_carne = input("Qual o tipo da carne? ")
qtd_carne = int(input("Qual a quantidade de carne? "))
tipo_pagamento = input("Qual o tipo de pagamento em cartão? SIM ou NÃO: ")

if tipo_carne == "File Duplo":
    if qtd_carne > 5:
        valor = qtd_carne * 5.8
    else: 
        valor = qtd_carne * 4.9
    
if tipo_carne == "Alcatra":
    if qtd_carne > 5:
        valor = qtd_carne * 6.8
    else: 
        valor = qtd_carne * 5.9
        
        
if tipo_carne == "Picanha":
    if qtd_carne > 5:
        valor = qtd_carne * 7.8
    else: 
        valor = qtd_carne * 6.9
        
if tipo_pagamento == "SIM":
        desconto =  (valor * 0.05)
        total = valor - desconto
else:
        tipo_pagamento == "NAO"
        total = valor
print("----- Cupom Fiscal -----")
print("Carne: ", tipo_carne)
print("Quantidade: ", qtd_carne)
print("Preço: ", valor)
print("Cartão? ", tipo_pagamento)
print("Total com desconto:", total)
print("----- Cupom Fiscal -----")


# In[ ]:




