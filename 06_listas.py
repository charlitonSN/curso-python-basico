
# ============================================================
# AULA 06 - LISTAS EM PYTHON
# ============================================================

# OBJETIVO:
# Compreender o funcionamento das listas em Python, aprender
# a criar, acessar, modificar e realizar operações com seus
# elementos.
#
# As listas são coleções de dados que podem ser alteradas,
# ou seja, são mutáveis.
#
# Elas podem conter elementos de diferentes tipos, como
# números, strings e até outras listas.
#
# As listas são definidas usando colchetes [] e os elementos
# são separados por vírgulas.


# ============================================================
# 1. CRIANDO LISTAS
# ============================================================

# Exemplos de criação de uma lista:

minha_lista = [1, 2, 3, 4, 5]

print(minha_lista)


# Uma lista também pode armazenar textos.

minha_lista = ["maçã", "banana", "laranja"]

print(minha_lista)


# A lista pode conter elementos de diferentes tipos,
# como números, strings e valores booleanos.

minha_lista = [1, "maçã", 3.14, True]

print(minha_lista)


# EXEMPLO DE LISTA ANINHADA:
# Uma lista aninhada é uma lista dentro de outra lista.

minha_lista = [1, 2, [3, 4], 5]

print(minha_lista)


# ============================================================
# 2. IDENTIFICANDO O TIPO DE DADO
# ============================================================

# A função type() permite identificar o tipo de dado
# armazenado em uma variável.

print(type(minha_lista))


# ============================================================
# 3. ACESSANDO ELEMENTOS DA LISTA
# ============================================================

# Os elementos de uma lista podem ser acessados utilizando
# seus índices.
#
# O índice do primeiro elemento é 0, o segundo é 1,
# e assim por diante.
#
# Para acessar um elemento individual, utilizamos
# colchetes [] e informamos o índice desejado.

minha_lista = [10, 20, 30, 40, 50]

print(minha_lista[0])  # Acessa o primeiro elemento
print(minha_lista[1])  # Acessa o segundo elemento


# ============================================================
# 4. FATIAMENTO DE LISTAS (SLICING)
# ============================================================

# O fatiamento permite acessar uma parte da lista,
# especificando o índice inicial e o índice final.
#
# O índice inicial é inclusivo, enquanto o índice final
# é exclusivo.

print(minha_lista[1:4])  # Acessa os elementos de índice 1 a 3


# Podemos fatiar do início sem precisar informar
# o índice inicial.

print(minha_lista[:3])


# Acessando os quatro últimos elementos da lista.

print(minha_lista[-4:])


# ============================================================
# 5. ACESSANDO ELEMENTOS COM ÍNDICES NEGATIVOS
# ============================================================

# Os índices negativos permitem acessar os elementos
# da lista de trás para frente.
#
# O índice -1 representa o último elemento, -2 representa
# o penúltimo elemento, e assim por diante.

print(minha_lista[-1])  # Acessa o último elemento
print(minha_lista[-2])  # Acessa o penúltimo elemento


# ============================================================
# 6. ACESSANDO ELEMENTOS DE LISTAS ANINHADAS
# ============================================================

# Para acessar elementos de uma lista aninhada, utilizamos
# dois índices.
#
# O primeiro índice acessa a lista interna.
# O segundo índice acessa o elemento dentro dela.

minha_lista = [1, 2, [3, 4], 5]

print(minha_lista[2][1])


# ============================================================
# 7. ALTERANDO ELEMENTOS DA LISTA
# ============================================================

# As listas são mutáveis, portanto podemos alterar seus
# elementos após a criação.
#
# Para modificar um elemento, basta indicar seu índice
# e atribuir um novo valor.

minha_lista[2] = 10

print(minha_lista)


# ============================================================
# 8. OPERAÇÕES MATEMÁTICAS COM LISTAS
# ============================================================

# Podemos fazer operações matemáticas com listas
# que contenham elementos numéricos.

lista2 = [0, 5, 6, 7, 1, 9, 15]

print(lista2)


# SOMA DOS ELEMENTOS
#
# A função sum() realiza a soma de todos os elementos
# numéricos da lista.

soma = sum(lista2)

print(soma)


# QUANTIDADE DE ELEMENTOS
#
# A função len() retorna a quantidade de elementos
# existentes na lista.

quantidade = len(lista2)

print(quantidade)


# ============================================================
# 9. MEDIDAS DE TENDÊNCIA CENTRAL
# ============================================================

# MÉDIA
#
# A média aritmética é calculada dividindo a soma dos
# elementos pela quantidade de observações.

media = sum(lista2) / len(lista2)

print(f"A média é: {media:.2f}")


# MEDIANA
#
# A mediana representa o valor central de um conjunto
# de dados organizados em ordem crescente.
#
# Para calcular a mediana, utilizamos a biblioteca statistics.

import statistics

mediana = statistics.median(lista2)

print(f"A mediana é: {mediana}")


# MODA
#
# A moda representa o valor que aparece com maior frequência
# em um conjunto de dados.
#
# A função multimode() retorna todas as modas encontradas.

lista3 = [1, 2, 2, 3, 4, 4, 4, 5]

moda = statistics.multimode(lista3)

print(f"A moda é: {moda}")


# ============================================================
# 10. VALORES MÍNIMO E MÁXIMO
# ============================================================

# A função min() retorna o menor valor da lista.
# A função max() retorna o maior valor da lista.

minimo = min(lista2)
maximo = max(lista2)

print(f"O valor mínimo é: {minimo}")
print(f"O valor máximo é: {maximo}")


# ============================================================
# 11. RESUMO DAS OPERAÇÕES ESTATÍSTICAS
# ============================================================

print(f"""
Resumo estatístico da lista:

Lista: {lista2}
Quantidade de elementos: {len(lista2)}
Soma: {sum(lista2)}
Média: {statistics.mean(lista2):.2f}
Mediana: {statistics.median(lista2)}
Mínimo: {min(lista2)}
Máximo: {max(lista2)}
""")


# ============================================================
# 12. MÉTODOS DE MANIPULAÇÃO DE LISTAS
# ============================================================

# Os métodos são recursos próprios das listas que permitem
# adicionar, remover, localizar e organizar seus elementos.
#
# Diferentemente das funções, os métodos são chamados
# utilizando o nome da lista seguido de um ponto (.).


# ============================================================
# 13. ADICIONANDO ELEMENTOS
# ============================================================

# APPEND()
#
# O método append() adiciona um novo elemento ao final
# da lista.

lista = [1, 2, 3, 4, 5]

lista.append(6)

print(lista)


# INSERT()
#
# O método insert() permite adicionar um elemento em
# uma posição específica da lista.
#
# Sua estrutura é: insert(índice, elemento).

lista = [1, 2, 3, 4, 5]

lista.insert(2, 10)  # Adiciona 10 no índice 2

print(lista)


# EXTEND()
#
# O método extend() permite adicionar vários elementos
# de outra coleção ao final da lista.

lista = [1, 2, 3]

lista.extend([4, 5, 6])

print(lista)


# ============================================================
# 14. REMOVENDO ELEMENTOS
# ============================================================

# REMOVE()
#
# O método remove() remove a primeira ocorrência de um
# determinado valor na lista.

lista = [1, 2, 3, 4, 5, 3]

lista.remove(3)

print(lista)


# POP()
#
# O método pop() remove um elemento de acordo com seu índice.
#
# Quando nenhum índice é informado, remove o último elemento.
#
# O método também retorna o valor removido.

lista = [1, 2, 3, 4, 5]

removido = lista.pop(2)

print(f"Elemento removido: {removido}")
print(lista)


# Removendo o último elemento sem informar o índice.

lista = [1, 2, 3, 4, 5]

lista.pop()

print(lista)


# CLEAR()
#
# O método clear() remove todos os elementos da lista,
# deixando-a vazia.

lista = [1, 2, 3, 4, 5]

lista.clear()

print(lista)


# ============================================================
# 15. ORGANIZANDO ELEMENTOS
# ============================================================

# SORT()
#
# O método sort() organiza os elementos da lista em ordem
# crescente.
#
# Ele modifica a própria lista.

lista = [5, 2, 8, 1, 9, 3]

lista.sort()

print(lista)


# Podemos utilizar o parâmetro reverse=True para organizar
# os elementos em ordem decrescente.

lista = [5, 2, 8, 1, 9, 3]

lista.sort(reverse=True)

print(lista)


# REVERSE()
#
# O método reverse() inverte a ordem atual dos elementos
# da lista.
#
# Diferentemente do sort(), ele não organiza os valores
# em ordem crescente ou decrescente.

lista = [1, 5, 3, 8, 2]

lista.reverse()

print(lista)


# ============================================================
# 16. LOCALIZANDO E CONTANDO ELEMENTOS
# ============================================================

# INDEX()
#
# O método index() retorna o índice da primeira ocorrência
# de um determinado elemento na lista.

lista = [10, 20, 30, 40, 50]

posicao = lista.index(30)

print(f"O elemento está no índice: {posicao}")


# COUNT()
#
# O método count() retorna quantas vezes determinado
# elemento aparece na lista.

lista = [1, 2, 2, 3, 2, 4, 5]

quantidade = lista.count(2)

print(f"O número 2 aparece {quantidade} vezes.")


# ============================================================
# 17. COPIANDO LISTAS
# ============================================================

# COPY()
#
# O método copy() cria uma cópia superficial da lista.
#
# Dessa forma, podemos modificar a nova lista sem alterar
# os elementos da lista original (em listas simples).

lista_original = [1, 2, 3, 4, 5]

lista_copia = lista_original.copy()

lista_copia.append(6)

print(f"Lista original: {lista_original}")
print(f"Lista copiada: {lista_copia}")


# ============================================================
# 18. VERIFICANDO SE UM ELEMENTO EXISTE
# ============================================================

# O operador in verifica se determinado elemento está
# presente na lista.
#
# O resultado será um valor booleano: True ou False.

lista = [10, 20, 30, 40, 50]

print(30 in lista)  # Retorna True
print(60 in lista)  # Retorna False


# O operador not in verifica se determinado elemento
# NÃO está presente na lista.

print(60 not in lista)  # Retorna True
print(30 not in lista)  # Retorna False


# ============================================================
# 19. RESUMO DOS PRINCIPAIS MÉTODOS
# ============================================================

# append()  -> Adiciona um elemento ao final da lista.
# insert()  -> Adiciona um elemento em uma posição específica.
# extend()  -> Adiciona vários elementos ao final da lista.
# remove()  -> Remove a primeira ocorrência de um valor.
# pop()     -> Remove um elemento pelo índice.
# clear()   -> Remove todos os elementos da lista.
# sort()    -> Organiza os elementos da lista.
# reverse() -> Inverte a ordem dos elementos.
# index()   -> Retorna o índice de um elemento.
# count()   -> Conta as ocorrências de um elemento.
# copy()    -> Cria uma cópia superficial da lista.
