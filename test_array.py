import numpy

'''

ndarray (array do numpy) é:
    - homogêneo: ou seja, todos os elementos devem ser do mesmo tipo
    - tamanho fixo: é possivel alterar os valores da array, mas não retira-los ou adicionar novo valor. Caso queira, será necessario criar um outra array

''' 


arrayteste = [1,2,3,4,5]
print (arrayteste)

# array: cria uma array numpy a partir de uma lista do python
teste = numpy.array(arrayteste)
teste1 = numpy.array([1,2,3,4,5])
multiplicação = 2 * teste1

print(teste)
print(teste1)
print(multiplicação)

#  loadtxt: recebe um arquivo txt e transforma seu conteudo em um array
anos_de_nascimento = numpy.loadtxt("anos_de_nascimento.txt")

# avarage: calcula a media dos valores do array

# size: calcula o tamanho do array

# ndim: mostra o numero de dimensões do array

# shape: devolve dois valores - a quantidade de elementos do array e o numero de dimensões

# dtype: mostra o tipo dos elementos do array

# arange: cria uma sequencia de elementos, semelhando ao range()

# reshape: da uma nova forma ao array, sem modificar osdados

# zeros: cria um array cheio de zeros

# sort: ordena os elementos

# concatenate: combina 2 arrays

# toList: transforma em uma estrutura padrão do python




# array de 2 dimensões

teste = numpy.arange(10).reshape(2,5)
# criamos uma array de 0 a 9, e então dividimos os valores em 2 arrays dentro de um array

print(teste[0][2])
# estamos acessando o primeiro array, em sua terceira posição

print(teste.shape)
# o resultado é (2,5) - duas dimensões, cada um com cinco valores

print(teste.ndim)
# o resultado seria 2, de duas dimensões




# array de 3 dimensões

teste3 = numpy.arange(60).reshape(3,4,5)
# criamos uma array de 0 a 59 e dividimos eles em arrays, dentro de arrays, dentro de um array

print(teste3[2][1][2])
# estamos acessando o terceiro valor do segundo array dentro do terceiro array

print(teste3.shape)
# o resultado é (3,4,5) - tres dimensões - são 3 arrays, cada um com 4 arrays, cada um com 5 valores

print(teste3.ndim)
# resultado é 3



# realizando filtros no array
a = numpy.arange(0,20,3)

print(a)

print(a[a > 12])
print(a[a%2==0])




# podemos tambem realizar filtros em arrays de mais dimensões
a = numpy.array([[1,2,3,4], [5,6,7,8]])

print(a)
print(a[a>=3])
# retorno: [3 4 5 6 7 8] - note que todos os valores que passam do filtro é retornado em uma unica array

print(a[a>=3].ndim)
# o retorno: 1 - visto que a resposta é uma array de 1 dimensão




# usando o zeros()
a = numpy.zeros(3)
a = numpy.zeros((3))
# é criado uma array de 1 dimensão com 3 colunas de valor 0

a = numpy.zeros((3,2))
# é criado uma array de 2 dimensões: um array com 3 arrays com 2 valores cada

a = numpy.zeros((3,2,4))
# é criado uma array de 3 dimensões: um array com 3 arrays com 2 arrays com 4 valores cada



# concatenação
a = numpy.array([[4,7,8], [2,3,8]])
b = numpy.array([[1,2,3], [3,4,3]])
c = numpy.concatenate((a,b))
print(c)