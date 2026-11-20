
# ============================================================
# AULA 01 - PRIMEIROS COMANDOS EM PYTHON
# ============================================================

# OBJETIVO:
# Conhecer os primeiros comandos do Python, aprender a utilizar
# comentários e compreender como exibir informações na tela
# por meio da função print().


# %%
# ============================================================
# 1. COMENTÁRIOS EM PYTHON
# ============================================================

# Os comentários são utilizados para documentar o código,
# explicar instruções e facilitar a compreensão do programa.
#
# Para criar um comentário de uma linha, utilizamos o símbolo #.
#
# Quando precisamos escrever explicações mais longas,
# podemos utilizar várias linhas iniciadas por #.
#
# Também existem as aspas triplas (''' ou """), utilizadas
# para criar strings de múltiplas linhas. Elas são comuns
# na documentação de funções, classes e módulos.


# %%
# ============================================================
# 2. ORGANIZAÇÃO DO CÓDIGO EM CÉLULAS
# ============================================================

# O marcador # %% permite dividir o código em células.
# Cada célula pode ser executada separadamente em ambientes
# compatíveis, como o VS Code com suporte a Python e Jupyter.
#
# Para executar uma célula no VS Code, podemos utilizar:
#
# Shift + Enter -> Executa a célula e avança para a próxima.
# Ctrl + Enter  -> Executa a célula sem avançar.


# %%
# ============================================================
# 3. PRIMEIRO COMANDO: HELLO WORLD
# ============================================================

# A função print() permite exibir informações na tela.
# Tradicionalmente, o primeiro exemplo de programação
# consiste em imprimir a mensagem "Olá, mundo!".

print("Olá, mundo!")


# %%
# ============================================================
# 4. UTILIZANDO PRINT() PARA EXIBIR RESULTADOS
# ============================================================

# Além de textos, a função print() também permite exibir
# resultados de operações matemáticas.

print(2 + 3)


# %%
# ============================================================
# 5. EXIBINDO TEXTOS E RESULTADOS MATEMÁTICOS
# ============================================================

# Podemos utilizar a função print() para combinar textos
# e resultados de operações matemáticas.
#
# Para separar diferentes informações, utilizamos vírgulas.
# Por padrão, o Python adiciona um espaço entre os valores.

print("O resultado da operação é:", 2 + 3)


# %%
# Também podemos apresentar mais de uma informação
# na mesma chamada da função print().

print(
    "O resultado da soma é:", 2 + 3,
    "e o resultado da multiplicação é:", 2 * 3
)


# %%
# ============================================================
# 6. CARACTERES DE ESCAPE
# ============================================================

# Os caracteres de escape permitem modificar a forma como
# os textos são apresentados na tela.
#
# \n -> Insere uma quebra de linha.
# \t -> Insere uma tabulação horizontal.


# %%
# UTILIZANDO \n PARA QUEBRAR LINHAS
#
# O caractere \n faz com que a informação seguinte
# seja exibida em uma nova linha.

print(
    "O resultado da soma é:\n", 2 + 3,
    "\ne o resultado da multiplicação é:\n", 2 * 3
)


# %%
# UTILIZANDO \t PARA INSERIR TABULAÇÕES
#
# O caractere \t adiciona um espaçamento horizontal,
# permitindo organizar as informações exibidas.

print(
    "O resultado da soma é:\t", 2 + 3,
    "\te o resultado da multiplicação é:\t", 2 * 3
)

