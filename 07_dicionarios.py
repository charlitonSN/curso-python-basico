# %%
# ============================================================
# INTRODUÇÃO AOS DICIONÁRIOS E TUPLAS
# ============================================================

# OBJETIVO:
# Compreender o funcionamento dos dicionários e das tuplas,
# aprender a acessar, adicionar e modificar informações,
# além de entender as diferenças entre estruturas mutáveis
# e imutáveis no Python.


# ============================================================
# 1. INTRODUÇÃO AOS DICIONÁRIOS
# ============================================================

# Dicionários (dict) são estruturas de dados que armazenam
# informações no formato de pares de chave e valor (key: value).
#
# Diferentemente das listas, que acessam os elementos por
# índices numéricos, os dicionários permitem acessar os
# valores por meio de chaves.
#
# Os dicionários são definidos utilizando chaves {} e
# separando as chaves dos valores por dois-pontos (:).
#
# Cada chave deve ser única dentro do dicionário.


# ============================================================
# 2. CRIANDO UM DICIONÁRIO
# ============================================================

# Sempre utilizamos uma chave seguida de seu respectivo valor,
# separados por dois-pontos (:).

dados_pessoais = {
    'nome': 'Charliton',
    'idade': 27,
    'cidade': 'Maceió',
    'altura': 1.70,
    'formacao': ['Análise de Dados', 'Economia'],
    'empregos': [
        {'nome': 'Shapiro', 'cargo': 'Analista'},
        {'nome': 'Varejou', 'cargo': 'Gerente'},
        {'nome': 'Datebook', 'cargo': 'Cientista de Dados'}
    ]
}

print(dados_pessoais)


# %%
# ============================================================
# 3. ACESSANDO OS VALORES DO DICIONÁRIO
# ============================================================

# Para acessar um valor, utilizamos o nome da chave.

print(dados_pessoais['nome'])
print(dados_pessoais['idade'])
print(dados_pessoais['cidade'])

# Também podemos utilizar as chaves dentro de uma f-string.

print(
    f"Meu nome é {dados_pessoais['nome']} "
    f"e tenho {dados_pessoais['idade']} anos."
)


# %%
# ============================================================
# 4. ACESSANDO VALORES DE LISTAS DENTRO DE DICIONÁRIOS
# ============================================================

# Um dicionário pode armazenar diferentes estruturas de dados,
# incluindo listas e outros dicionários.
#
# Primeiro acessamos a chave do dicionário.
# Depois utilizamos o índice para selecionar o elemento da lista.

print(dados_pessoais['formacao'])

# Acessando o segundo elemento da lista.
print(dados_pessoais['formacao'][1])


# %%
# ============================================================
# 5. ACESSANDO DICIONÁRIOS DENTRO DE LISTAS
# ============================================================

# A chave 'empregos' armazena uma lista de dicionários.
# Primeiro acessamos a chave 'empregos'.
# Depois utilizamos os índices para selecionar cada dicionário.

print(dados_pessoais['empregos'])

# Verificando o tipo de dado armazenado.
print(type(dados_pessoais['empregos']))

# Acessando os elementos da lista.
print(dados_pessoais['empregos'][0])
print(dados_pessoais['empregos'][1])
print(dados_pessoais['empregos'][2])

# Verificando o tipo de dado de um elemento da lista.
print(type(dados_pessoais['empregos'][2]))

# Agora podemos acessar os valores do dicionário selecionado
# utilizando suas respectivas chaves.

print(dados_pessoais['empregos'][2]['nome'])
print(dados_pessoais['empregos'][2]['cargo'])

# Também podemos acessar informações de outros empregos.

print(dados_pessoais['empregos'][0]['nome'])
print(dados_pessoais['empregos'][0]['cargo'])


# %%
# ============================================================
# 6. ADICIONANDO E MODIFICANDO ELEMENTOS
# ============================================================

# Para adicionar uma nova informação, criamos uma nova chave.
# Se a chave já existir, seu valor será atualizado.

# Adicionando uma nova chave.
dados_pessoais['linguagem'] = 'Inglês'

# Modificando uma informação existente.
dados_pessoais['idade'] = 28

print(dados_pessoais)


# %%
# ============================================================
# 7. ACESSANDO AS CHAVES, VALORES E PARES DO DICIONÁRIO
# ============================================================

# keys(): retorna uma visão de todas as chaves do dicionário.

print(dados_pessoais.keys())

# values(): retorna uma visão de todos os valores do dicionário.

print(dados_pessoais.values())

# items(): retorna uma visão dos pares de chave e valor.
# Cada par é representado por uma tupla.

print(dados_pessoais.items())

# Podemos converter o resultado de items() em uma lista.

print(list(dados_pessoais.items()))


# %%
# ============================================================
# 8. OUTROS MÉTODOS DOS DICIONÁRIOS
# ============================================================

# get(): acessa o valor de uma chave.
# Caso a chave não exista, retorna None por padrão.

print(dados_pessoais.get('nome'))
print(dados_pessoais.get('profissao'))

# Podemos definir um valor padrão para chaves inexistentes.

print(dados_pessoais.get('profissao', 'Não informado'))


# %%
# update(): adiciona novas informações ou atualiza
# valores de chaves que já existem.

dados_pessoais.update({
    'idade': 27,
    'estado': 'Alagoas'
})

print(dados_pessoais)


# %%
# pop(): remove uma chave e retorna o valor removido.

estado = dados_pessoais.pop('estado')

print(estado)
print(dados_pessoais)


# %%
# clear(): remove todos os elementos do dicionário.

# dados_pessoais.clear()


# %%
# copy(): cria uma cópia superficial do dicionário.

copia_dados = dados_pessoais.copy()

print(copia_dados)


# %%
# Verificando se uma chave existe no dicionário.
print('nome' in dados_pessoais)

# Verificando a quantidade de elementos do dicionário.
print(len(dados_pessoais))


# %%
# ============================================================
# 9. PERCORRENDO UM DICIONÁRIO COM FOR
# ============================================================

# Podemos utilizar estruturas de repetição para percorrer
# os elementos de um dicionário.

# Percorrendo somente as chaves.

for chave in dados_pessoais:
    print(chave)


# %%
# Percorrendo somente os valores.

for valor in dados_pessoais.values():
    print(valor)


# %%
# Percorrendo as chaves e seus respectivos valores.

for chave, valor in dados_pessoais.items():
    print(f'{chave}: {valor}')


# %%
# ============================================================
# 10. INTRODUÇÃO ÀS TUPLAS
# ============================================================

# Tuplas (tuple) são estruturas de dados utilizadas para
# armazenar coleções de elementos.
#
# A principal característica das tuplas é a imutabilidade:
# não podemos adicionar, remover ou substituir diretamente
# seus elementos depois da criação.
#
# As tuplas são definidas utilizando parênteses () e seus
# elementos são separados por vírgulas.
#
# Assim como as listas, podem armazenar diferentes tipos
# de dados.


# %%
# ============================================================
# 11. CRIANDO UMA TUPLA
# ============================================================

tupla = (5, 6, 'Charliton', 'Maceió')

print(tupla)

# Verificando o tipo de dado.

print(type(tupla))


# %%
# ============================================================
# 12. ACESSANDO OS ELEMENTOS DA TUPLA
# ============================================================

# A forma de acessar os valores é semelhante à das listas.
# Utilizamos os índices numéricos.

print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])

# Também podemos utilizar índices negativos.

print(tupla[-1])
print(tupla[-2])


# %%
# ============================================================
# 13. FATIAMENTO (SLICING) EM TUPLAS
# ============================================================

# O fatiamento permite selecionar partes de uma tupla.
# A posição final não é incluída no resultado.

numeros = (10, 20, 30, 40, 50, 60)

# Selecionando os elementos dos índices 1 até 3.

print(numeros[1:3])

# Selecionando os elementos do início até o índice 3.

print(numeros[:3])

# Selecionando os elementos do índice 2 até o final.

print(numeros[2:])

# Invertendo a ordem dos elementos.

print(numeros[::-1])


# %%
# ============================================================
# 14. IMUTABILIDADE DAS TUPLAS
# ============================================================

# Os elementos de uma tupla não podem ser modificados
# diretamente depois de sua criação.
#
# O código abaixo gera um TypeError.

# tupla[0] = 1


# %%
# ============================================================
# 15. TUPLAS COM APENAS UM ELEMENTO
# ============================================================

# Para criar uma tupla com apenas um elemento, precisamos
# adicionar uma vírgula depois do valor.
#
# A vírgula é o que caracteriza a tupla, e não os parênteses.

# Isso não é uma tupla, mas sim um número inteiro.

valor = (10)

print(type(valor))


# %%
# Isso é uma tupla.

valor = (10,)

print(type(valor))


# %%
# ============================================================
# 16. TUPLAS COM LISTAS EM SEU INTERIOR
# ============================================================

# A imutabilidade da tupla impede a alteração de seus elementos.
# Entretanto, se um desses elementos for uma estrutura mutável,
# como uma lista, podemos modificar o conteúdo dessa lista.
#
# A tupla permanece com os mesmos elementos e posições,
# mas a lista armazenada dentro dela pode ser modificada.

tupla = (5, 3, 'Charliton', [5, 3, 1, 10])

print(tupla)


# %%
# Modificando um elemento da lista dentro da tupla.

tupla[-1][0] = 0

print(tupla)


# %%
# Adicionando um novo elemento à lista dentro da tupla.
#
# append(): adiciona um elemento ao final da lista.
# O valor informado dentro dos parênteses será o elemento
# adicionado.

tupla[-1].append(999)

print(tupla)


# %%
# ============================================================
# 17. PRINCIPAIS MÉTODOS DAS TUPLAS
# ============================================================

numeros = (10, 20, 30, 20, 40, 20)

# count(): conta quantas vezes determinado elemento aparece.

print(numeros.count(20))

# index(): retorna o índice da primeira ocorrência
# de determinado elemento.

print(numeros.index(30))


# %%
# ============================================================
# 18. FUNÇÕES ÚTEIS PARA TRABALHAR COM TUPLAS
# ============================================================

numeros = (10, 20, 30, 40, 50)

# len(): retorna a quantidade de elementos.

print(len(numeros))

# max(): retorna o maior elemento.

print(max(numeros))

# min(): retorna o menor elemento.

print(min(numeros))

# sum(): retorna a soma dos elementos.

print(sum(numeros))


# %%
# ============================================================
# 19. PERCORRENDO UMA TUPLA COM FOR
# ============================================================

frutas = ('Maçã', 'Banana', 'Uva', 'Laranja')

# Percorrendo diretamente os elementos.

for fruta in frutas:
    print(fruta)


# %%
# Percorrendo os elementos utilizando os índices.

for i in range(len(frutas)):
    print(frutas[i])


# %%
# ============================================================
# 20. DESEMPACOTAMENTO DE TUPLAS (UNPACKING)
# ============================================================

# O desempacotamento permite atribuir os elementos de uma
# tupla a variáveis individuais.

pessoa = ('Charliton', 27, 'Economia')

nome, idade, curso = pessoa

print(nome)
print(idade)
print(curso)


# %%
# ============================================================
# 21. DIFERENÇAS ENTRE LISTAS, TUPLAS E DICIONÁRIOS
# ============================================================

# LISTAS (list):
# Armazenam coleções de elementos.
# São mutáveis e acessadas por índices numéricos.
#
# TUPLAS (tuple):
# Armazenam coleções de elementos.
# São imutáveis e acessadas por índices numéricos.
#
# DICIONÁRIOS (dict):
# Armazenam informações em pares de chave e valor.
# São mutáveis e acessados por meio de chaves.


# %%
# Exemplo de lista.

lista = [10, 20, 30]


# %%
# Exemplo de tupla.

tupla = (10, 20, 30)


# %%
# Exemplo de dicionário.

dicionario = {
    'nome': 'Charliton',
    'idade': 27,
    'curso': 'Economia'
}


# %%
# ============================================================
# 22. APLICAÇÃO PRÁTICA: ANÁLISE DE DADOS
# ============================================================

# Exemplo de dicionário para armazenar o faturamento mensal
# de uma empresa.

vendas = {
    'janeiro': 15000,
    'fevereiro': 18000,
    'março': 22000,
    'abril': 17000
}

# Calculando o faturamento total.

total = sum(vendas.values())

# Calculando a média mensal.

media = total / len(vendas)

print(f'Faturamento total: R$ {total:,.2f}')
print(f'Média mensal: R$ {media:,.2f}')


# %%
# ============================================================
# FIM DA AULA
# ============================================================

# PRINCIPAIS CONCEITOS:
#
# 1. Dicionários armazenam dados em pares de chave e valor.
# 2. As chaves dos dicionários devem ser únicas.
# 3. Dicionários podem armazenar listas e outros dicionários.
# 4. O método items() retorna pares representados por tuplas.
# 5. Tuplas são estruturas de dados imutáveis.
# 6. Tuplas permitem acessar elementos por índices.
# 7. Listas armazenadas dentro de tuplas podem ser modificadas.
# 8. append() adiciona elementos ao final de uma lista.
# 9. O desempacotamento permite distribuir os elementos
#    de uma tupla entre diferentes variáveis.
