
# ============================================================
# AULA 04 - LÓGICA BOOLEANA E ESTRUTURAS CONDICIONAIS
# ============================================================

# OBJETIVO:
# Compreender a lógica booleana e utilizar estruturas
# condicionais para desenvolver uma calculadora simples.
#
# O programa solicita dois números e uma operação matemática.
# Em seguida, verifica a operação escolhida, realiza o cálculo
# e apresenta o resultado ao usuário.


# ============================================================
# 1. INTRODUÇÃO À LÓGICA BOOLEANA
# ============================================================

# A lógica booleana trabalha com dois valores:
#
# True  -> Verdadeiro
# False -> Falso
#
# As expressões booleanas permitem verificar condições e
# determinar quais instruções serão executadas pelo programa.


# OPERADORES LÓGICOS:
#
# and -> E: todas as condições precisam ser verdadeiras.
# or  -> OU: pelo menos uma condição precisa ser verdadeira.
# not -> NÃO: inverte o resultado lógico de uma condição.


# OPERADORES DE COMPARAÇÃO:
#
# == -> Igual a.
# != -> Diferente de.
# >  -> Maior que.
# <  -> Menor que.
# >= -> Maior ou igual a.
# <= -> Menor ou igual a.


# OPERADORES DE IDENTIDADE:
#
# is     -> Verifica se duas referências apontam para o mesmo objeto.
# is not -> Verifica se duas referências não apontam para o mesmo objeto.
#
# VERIFICAÇÃO DE VALORES:
#
# is None     -> Verifica se uma variável possui o valor None.
# is not None -> Verifica se uma variável não possui o valor None.
#
# None representa a ausência de um valor em Python.
# Diferentemente do SQL, utilizamos is None e is not None,
# e não IS NULL ou IS NOT NULL.


# ============================================================
# 2. EXEMPLOS DE EXPRESSÕES BOOLEANAS
# ============================================================

# O resultado de uma expressão booleana será True ou False.


# OPERADORES DE COMPARAÇÃO:

print(10 > 5)       # True
print(10 < 5)       # False
print(10 == 10)     # True
print(10 != 5)      # True
print(10 >= 10)     # True
print(10 <= 5)      # False


# COMPARAÇÃO ENTRE TEXTOS:

print("charliton" == "charliton")  # True
print("charliton" != "charliton")  # False


# OPERADORES LÓGICOS:

print(10 > 5 and 10 < 20)  # True
print(10 > 5 or 10 < 5)    # True
print(not 10 > 5)          # False


# ============================================================
# 3. ESTRUTURAS CONDICIONAIS
# ============================================================

# IF:
# É utilizado para verificar uma condição.
# Se ela for verdadeira (True), o bloco de código
# correspondente será executado.
#
# ELIF:
# Permite verificar outras condições caso as anteriores
# sejam falsas (False).
#
# ELSE:
# É executado quando nenhuma das condições anteriores
# foi atendida.
#
# IMPORTANTE:
# As estruturas condicionais permitem criar diferentes
# caminhos de execução, tornando os programas capazes
# de tomar decisões de acordo com as informações recebidas.
#
# SINTAXE:
#
# if condição:
#     bloco de código
#
# elif outra_condição:
#     bloco de código
#
# else:
#     bloco de código


# ============================================================
# 4. CALCULADORA SIMPLES
# ============================================================

# ENTRADA DE DADOS:
# Solicita ao usuário dois números e a operação matemática.

num1 = float(input("Digite o primeiro número: "))

operacao = input(
    "Digite a operação desejada (+, -, * ou /): "
).strip()

num2 = float(input("Digite o segundo número: "))


# PROCESSAMENTO:
# Verifica a operação escolhida e realiza o cálculo correspondente.

resultado = None

if operacao == '+':
    resultado = num1 + num2

elif operacao == '-':
    resultado = num1 - num2

elif operacao == '*':
    resultado = num1 * num2

elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: não é possível dividir por zero!")

else:
    print("Operador incompatível! Digite +, -, * ou /.")


# SAÍDA DE DADOS:
# Exibe o resultado somente quando uma operação válida foi realizada.

if resultado is not None:
    print("O resultado é:", resultado)
