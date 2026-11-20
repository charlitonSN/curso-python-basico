
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

while i < len(lista):
    print(lista[i])
    i += 1  # Avança para a próxima posição da lista


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
        print("O resultado é:", resultado)

    # CONTINUIDADE:
    # Pergunta se o usuário deseja realizar outra operação.

    continuar = input("Deseja realizar outra operação? (s/n): ").strip().lower()

    if continuar != 's':
        print("Encerrando a calculadora. Até logo!")
        break  # Interrompe o laço while e encerra a calculadora


# OBSERVAÇÕES:
#
# strip() remove espaços em branco no início e no final da string.
#
# lower() converte os caracteres da string para letras minúsculas,
# permitindo que tanto 'S' quanto 's' sejam reconhecidos.
#
# break encerra imediatamente o laço de repetição.
