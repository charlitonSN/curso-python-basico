
# ============================================================
# AULA 03 - VARIÁVEIS E TIPOS DE DADOS EM PYTHON
# ============================================================

# OBJETIVO:
# Aprender a armazenar informações em variáveis, identificar
# diferentes tipos de dados, receber informações do usuário
# e realizar conversões entre tipos de dados.
#
# Nesta aula, vamos retomar a expressão matemática apresentada
# na aula anterior, mas utilizando variáveis para armazenar
# os valores e facilitar a realização dos cálculos.


# %%
# ============================================================
# 1. CRIANDO E UTILIZANDO VARIÁVEIS
# ============================================================

# Variáveis são utilizadas para armazenar informações na memória,
# permitindo que seus valores sejam acessados e utilizados
# posteriormente durante a execução do programa.
#
# No exemplo abaixo, armazenamos os valores da expressão
# do segundo grau em variáveis e utilizamos esses valores
# para realizar o cálculo.

a = 2
b = 5
c = 3
x = 4

print("O resultado da expressão é:", a * (x ** 2) + b * x + c)


# %%
# ============================================================
# 2. ACESSANDO E ALTERANDO VALORES DE VARIÁVEIS
# ============================================================

# Podemos utilizar a função print() para visualizar
# o valor armazenado em uma variável.

print(a)


# %%
# O valor de uma variável pode ser alterado durante a execução
# do programa. Nesse caso, o novo valor substitui o anterior.

a = 10

print(a)


# %%
# ============================================================
# 3. PRINCIPAIS TIPOS DE DADOS
# ============================================================

# As variáveis podem armazenar diferentes tipos de informações.
# Entre os principais tipos de dados utilizados em Python, temos:
#
# int   -> Números inteiros.
# float -> Números decimais.
# str   -> Textos (strings).
# bool  -> Valores booleanos (True ou False).


# %%
# NÚMEROS INTEIROS (int)
# Representam números sem casas decimais.

z = 10

print(z)


# %%
# NÚMEROS DECIMAIS (float)
# Representam números com casas decimais.

y = 3.14

print(y)


# %%
# TEXTOS (str)
# São sequências de caracteres representadas entre aspas.

nome = "Charliton"

print(nome)


# %%
# BOOLEANOS (bool)
# Representam valores lógicos: verdadeiro (True) ou falso (False).

ativo = True

print(ativo)


# %%
# ============================================================
# 4. IDENTIFICANDO O TIPO DE DADO
# ============================================================

# A função type() permite identificar o tipo de dado
# armazenado em uma variável.

print(type(a))      # <class 'int'>
print(type(y))      # <class 'float'>
print(type(nome))   # <class 'str'>
print(type(ativo))  # <class 'bool'>


# %%
# ============================================================
# 5. RECEBENDO INFORMAÇÕES COM INPUT()
# ============================================================

# A função input() permite solicitar informações ao usuário.
# O valor digitado é armazenado na variável indicada.
#
# IMPORTANTE:
# A função input() sempre retorna uma string (str),
# mesmo quando o usuário digita um número.

idade = input("Digite sua idade: ")

print("Idade informada:", idade)


# %%
# ============================================================
# 6. CONVERSÃO DE TIPOS DE DADOS
# ============================================================

# Podemos utilizar funções de conversão para transformar
# um valor de um tipo de dado em outro.
#
# int()   -> Converte um valor para número inteiro.
# float() -> Converte um valor para número decimal.
# str()   -> Converte um valor para texto.
# bool()  -> Converte um valor para booleano.


# %%
# CONVERSÃO PARA INTEIRO (int)
# Permite converter uma entrada numérica para número inteiro.

idade = int(input("Digite sua idade: "))

print("Sua idade é:", idade)


# %%
# CONVERSÃO PARA DECIMAL (float)
# Permite receber números com casas decimais.

salario = float(input("Digite seu salário: "))

print("Seu salário é:", salario)


# %%
# CONVERSÃO PARA TEXTO (str)
# Transforma um valor em uma string.

numero = 10

print("O número é:", str(numero))


# %%
# CONVERSÃO PARA BOOLEANO (bool)
# A função bool() transforma valores em True ou False.
#
# Em geral:
# Valores considerados verdadeiros retornam True.
# Valores considerados falsos retornam False.
#
# Exemplos:
# bool(1) -> True
# bool(0) -> False

verdadeiro = bool(1)

falso = bool(0)

print("Verdadeiro:", verdadeiro)
print("Falso:", falso)
