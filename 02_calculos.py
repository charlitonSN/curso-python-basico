
# ============================================================
# AULA 02 - OPERAÇÕES MATEMÁTICAS EM PYTHON
# ============================================================

# OBJETIVO:
# Conhecer os principais operadores matemáticos do Python,
# compreender como realizar cálculos e aplicar esses conceitos
# na resolução de expressões matemáticas.


# %%
# ============================================================
# 1. OPERADORES ARITMÉTICOS
# ============================================================

# O Python permite realizar operações matemáticas utilizando
# operadores aritméticos. A seguir, veremos os principais.


# %%
# ADIÇÃO
# O operador + é utilizado para somar valores.

1 + 1


# %%
# SUBTRAÇÃO
# O operador - é utilizado para subtrair valores.

5 - 2


# %%
# MULTIPLICAÇÃO
# O operador * é utilizado para multiplicar valores.

3 * 4


# %%
# DIVISÃO
# O operador / é utilizado para dividir valores.
# O resultado será do tipo float, mesmo quando a divisão
# apresentar um número inteiro como resultado.

10 / 2


# %%
# POTENCIAÇÃO
# O operador ** é utilizado para elevar um número a uma potência.
# No exemplo, calculamos 2 elevado à terceira potência.

2 ** 3


# %%
# RESTO DA DIVISÃO
# O operador % retorna o resto de uma divisão.
# No exemplo, 10 dividido por 3 possui resto igual a 1.

10 % 3


# %%
# DIVISÃO INTEIRA
# O operador // realiza a divisão e retorna o quociente
# arredondado para baixo (floor).

10 // 3


# %%
# RAIZ QUADRADA
# Podemos calcular a raiz quadrada utilizando a potenciação.
#
# Elevar um número a 0.5 ou a 1/2 equivale a calcular
# sua raiz quadrada.
#
# Os dois exemplos abaixo apresentam o mesmo resultado.

16 ** 0.5

16 ** (1/2)


# %%
# ============================================================
# 2. UTILIZANDO PRINT() EM OPERAÇÕES MATEMÁTICAS
# ============================================================

# A função print() permite exibir o resultado de uma operação
# matemática acompanhado de um texto explicativo.
#
# O texto deve estar entre aspas, enquanto a operação
# matemática pode ser inserida diretamente na função.

print("O resultado da soma é:", 1 + 1)


# %%
# ============================================================
# 3. APLICAÇÃO PRÁTICA: EQUAÇÃO DO SEGUNDO GRAU
# ============================================================

# Com os operadores matemáticos, podemos construir expressões
# mais complexas e resolver diferentes problemas matemáticos.
#
# Um exemplo é a expressão do segundo grau:
#
# ax² + bx + c
#
# Em uma equação do segundo grau, essa expressão é igualada
# a zero:
#
# ax² + bx + c = 0
#
# A seguir, vamos calcular o valor da expressão considerando
# os seguintes valores:
#
# a = 2
# b = 5
# c = 3
# x = 4


# %%
# Substituindo os valores na expressão:
#
# 2 * 4² + 5 * 4 + 3

print(
    "O resultado da expressão é:",
    2 * (4 ** 2) + 5 * 4 + 3
)
