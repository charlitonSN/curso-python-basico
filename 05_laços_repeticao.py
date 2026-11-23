
# %%
# ============================================================
# INTRODUÇÃO AOS LAÇOS DE REPETIÇÃO
# ============================================================

# OBJETIVO:
# Compreender o funcionamento das estruturas de repetição
# while e for, aprender a percorrer sequências e aplicar
# esses conhecimentos em exemplos práticos e na calculadora.


# %%
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
# uma única vez quando a condição é verdadeira, enquanto o
# while permite repetir sua execução enquanto a condição
# permanecer verdadeira.


# EXEMPLO:
# Imprimir os números de 0 a 4.

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
# A função len() retorna a quantidade de elementos de uma
# sequência ou coleção.
#
# Como os índices começam em 0, utilizamos a condição
# i < len(lista) para percorrer todas as posições.


lista = [10, 25, 3, 80, 7]

i = 0

while i < len(lista):
    print(lista[i])
    i += 1

    # i += 1 é equivalente a i = i + 1.
    # Essa operação incrementa o valor de i em 1,
    # permitindo avançar para a próxima posição da lista.


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

    # strip() remove espaços em branco no início e no final
    # da string.
    #
    # lower() converte os caracteres para letras minúsculas.

    if continuar != 's':
        print("Encerrando a calculadora. Até logo!")
        break  # Interrompe o laço while.


# %%
# ============================================================
# 4. LAÇO FOR
# ============================================================

# O laço for é utilizado para percorrer os elementos de uma
# sequência ou coleção, como listas, tuplas, conjuntos e strings.
#
# A cada iteração, a variável utilizada no for recebe o próximo
# elemento da sequência e executa o bloco de código associado.
#
# Diferentemente do while, não precisamos controlar
# manualmente um contador para percorrer todos os elementos.


# EXEMPLO:
# Percorrendo uma lista e imprimindo cada elemento.

lista_numeros = [10, 25, 3, 80, 7]

for numero in lista_numeros:
    print(numero)


# %%
# ============================================================
# 5. PERCORRENDO UMA STRING COM FOR
# ============================================================

# O laço for também pode percorrer os caracteres de uma string.
#
# A cada iteração, a variável caractere recebe um caractere
# da palavra.

palavra = "Python"

for caractere in palavra:
    print(caractere)


# %%
# ============================================================
# 6. CONTANDO CARACTERES COM FOR E IF
# ============================================================

# Podemos combinar estruturas de repetição e condicionais
# para realizar análises sobre uma sequência.
#
# Neste exemplo, contamos quantas vezes a letra "a" aparece
# na palavra "banana".
#
# A cada iteração, o for verifica um caractere.
# Se o caractere for igual a "a", incrementamos o contador.


i = 0

for caractere in "banana":
    if caractere == "a":
        i += 1

print(f"A letra 'a' aparece {i} vezes na palavra.")


# %%
# ============================================================
# 7. FUNÇÃO RANGE()
# ============================================================

# A função range() permite gerar uma sequência de números
# inteiros, sendo bastante utilizada em conjunto com o for.
#
# SINTAXE:
# range(início, fim, passo)
#
# início -> Número em que a sequência começa (inclusivo).
# fim    -> Número em que a sequência termina (exclusivo).
# passo  -> Intervalo entre os números.
#
# O início e o passo são opcionais.
# Quando não informamos o início, o padrão é 0.
# Quando não informamos o passo, o padrão é 1.


# EXEMPLO 1:
# Gera números de 0 a 4.

for numero in range(5):
    print(numero)


# EXEMPLO 2:
# Gera números de 1 a 10.

for numero in range(1, 11):
    print(numero)


# EXEMPLO 3:
# Gera números pares de 0 a 10.

for numero in range(0, 11, 2):
    print(numero)


# %%
# ============================================================
# 8. TABUADA COM FOR E RANGE()
# ============================================================

# A tabuada é um exemplo prático da utilização dos laços
# de repetição.
#
# Neste exemplo, utilizamos range() para gerar os números
# de 1 a 10 e realizar as multiplicações.


num_tabuada = float(
    input("Qual tabuada você deseja ver? (Digite um número de 1 a 10): ")
)

print(f"\nTabuada do {num_tabuada}:")

for i in range(1, 11):
    resultado = num_tabuada * i
    print(f"{num_tabuada} x {i} = {resultado}")
