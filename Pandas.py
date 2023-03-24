import pandas

"""



"""

# Series: apresenta a lista em uma label


a = pandas.Series([1,2,3,4,5])

print(a)
# como não definimos o valor da label, irá vir de 0,1,2, ....

a = pandas.Series([1,2,3], ['buno', 'otavio', 'gui'])

print(a['gui'])
# aqui escolhemos o valor das label, sendo possivel acessar os valores por eles

print(a+1)
# somamos todos os valores a 1
# caso trocassemos a ordem dos arrays, iria quebrar, pois não tem como adicionar 1 a strings


print(a.median())
# acha a mediana

print(a.array)
# voce recebe só o array (pandasArray)

print(a.array.to_numpy())
# transformamos o pandasArray em um array do numpy




# DataFrame: cria uma tabela, tipo excel
concursos = pandas.DataFrame({
  "banca": ['cesgranrio', 'cespe'],
  "salario": [3000, 5000],
  "data": ['10/11/2121', '22/44/2323']
})

print(concursos)


# podemos criar um dataframe a partir de dados de uma array
alunos = [['bruno', 'sp', 12], ['mat', 'seila',12], ['digo', 'bh', 12]]

db = pandas.DataFrame(alunos, columns=['nome', 'cidade', 'idade'])

print(db)
print(db['nome'])
print(db[['nome', 'idade']])
# primeiro parametro é o array com os valores, e o segundo parametro é passando as colunas
# note que, se quisermos filtrar mais de uma coluna, devemos colocar dentro de um array



# leitor csv
dados = pandas.read_csv('concursos.csv', ';')
# o segundo parametro é o delimitador, ou seja, o que esta separando os valores

print(dados.info())
# irá imprimir informações extras

print(numpy.avarage[dados['salario']])
# usando a biblioteca numpy, estamos fazendo a média dos valores da coluna salarios

bancas = dados['bancas']
print(bancas.drop_duplicates())
# para excluir os valores duplicados

# head: mostra os 5 primeiros por padrão

# tail: mostra os 5 ultimos por padrão

#shapes: linhas e colunas

#concat: concatena dataframes

#index: retorna os indices da series

print(bancas.isin(['cespe']))
# retorna um booleano falando se o item se encontra nas linhas