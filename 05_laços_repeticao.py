
# %%
# ============================================================
# INTRODUÇÃO AOS LAÇOS DE REPETIÇÃO
# ============================================================

# Os laços de repetição permitem executar um bloco de código
# várias vezes, de acordo com uma condição ou uma sequência.


# ============================================================
# 1. LAÇO WHILE
# ============================================================

# SINTAXE:
# while condição:
#     bloco de código
#
# O código dentro do laço while será executado enquanto a
# condição for verdadeira (True).
#
# Assim como o if, o while utiliza uma condição que pode ser
# verdadeira ou falsa. A diferença é que o if executa o bloco
# uma única vez, enquanto o while permite repetir sua execução
# enquanto a condição permanecer verdadeira.


# EXEMPLO: 

i = 0

while i < 5:
    print(i)
    i += 1  # Incrementa o valor de i em 1


# %%
# ============================================================
# 2. PERCORRENDO UMA LISTA COM WHILE
# ============================================================

# Também podemos utilizar o while para percorrer os elementos
# de uma lista.
#
# Para isso, utilizamos um contador (i) para controlar a posição
# de cada elemento.
#
# A função len() retorna a quantidade de elementos da lista.
# O índice começa em 0, por isso utilizamos i < len(lista).

lista = [10, 25, 3, 80, 7]

i = 0

while i < len(lista):  # len() retorna a quantidade de elementos de uma sequencia ou coleção.
    print(lista[i])
    i += 1  # Avança para a próxima posição da lista. A expressão i += 1 é equivalente a i = i + 1, 
            # ou seja, incrementa o valor de i em 1.


# %%
# ============================================================
# 3. CALCULADORA COM LAÇO WHILE
# ============================================================

# Nesta versão, utilizamos o while True para permitir que o
# usuário realize várias operações sem precisar reiniciar
# o programa.
#
# O comando break é utilizado para encerrar o laço quando
# o usuário não desejar continuar utilizando a calculadora.


while True:

    # ENTRADA DE DADOS:
    # Solicita os números e a operação matemática desejada.

    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação desejada (+, -, * ou /): ").strip()
    num2 = float(input("Digite o segundo número: "))

    resultado = None

    # PROCESSAMENTO:
    # Verifica a operação escolhida e realiza o cálculo.

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
    # Exibe o resultado somente quando uma operação válida
    # foi realizada.

    if resultado is not None:
        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

    # CONTINUIDADE:
    # Pergunta se o usuário deseja realizar outra operação.

    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()
    # strip() remove espaços em branco no início e no final da string.
    if continuar != 's':
        print("Encerrando a calculadora. Até logo!")
        break  # Interrompe o laço while e encerra a calculadora


# %%
# ============================================================
# 1. LAÇO FOR
# ============================================================
# O laço for é utilizado para percorrer uma sequência de elementos, como listas, tuplas ou strings.
# A cada iteração, o laço for atribui o próximo elemento da sequência a uma
# variável e executa o bloco de código associado.
# Exemplo: percorrer uma lista de números e imprimir cada elemento.
lista_numeros = [10, 25, 3, 80, 7]

for numero in lista_numeros:
    print(numero)


# %%
# Outro exemplo: percorrer uma string e imprimir cada caractere.
palavra = "Python"

for caractere in palavra:
    print(caractere)

# %%
# Mais um exemplo: Imprimir a quantidade de caractees A na palavra "banana".

i = 0
for caractere in "banana":
    if caractere == "a":
        i += 1
print(f"A letra 'a' aparece {i} vezes na palavra.")
