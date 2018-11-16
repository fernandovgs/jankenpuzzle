# 
#	Universidade de São Paulo
#	Instituto de Ciências Matemáticas e de Computação - ICMC
# 	SCC 0218 - Algoritmos Avançados e Aplicações
# 	Projeto 1 - Backtracking
#
# 	Integrantes:
#		Enzo Bustamante Junco Mendonça	9863437
# 		Fernando Vinícius Gianini Silva 9293007
# 		Rafael Olivier Cardoso			9436166

#coding: utf-8



# criarTabuleiro(r, c): cria uma matriz representando o tabuleiro do jogo.
# Também adiciona as peças em seus devidos lugares. A entrada é feita via
# stdin.
# Parâmetros:
# 	r - número de linhas (Rows)
# 	c - número de colunas (Columns)
#
def criarTabuleiro(r, c, tabuleiro):
	n_pecas = 0

	for i in range(r):
		#leitura da entrada de uma linha do tabuleiro,
		#separando suas respectivas posições 
		linha_entrada = input()
		linha_str = linha_entrada.split(" ")

		linha = []
		for j in range(c):

			#adiciona a peca na coluna desejada 
			peca = int(linha_str[j])
			linha.append(peca)

			if (peca != 0):
				n_pecas += 1

		#adiciona
		tabuleiro.append(linha)

	return n_pecas


# janKenPuzzle(n_linhas, n_colunas, n_pecas, n_finais, resultado, linha_atual, coluna_atual, tabuleiro):
# Função que verifica todos os resultados possíveis (separando os distintos) de um tabuleiro de Jan-Ken-Puzzle,
# através de um algoritmo de backtracking, que testa TODAS as possibilidades do jogo através de recursividade.
# 
# Parâmetros:
#	n_linhas: 		número de linhas do tabuleiro 
# 	n_colunas:		número de colunas do tabuleiro
# 	n_pecas:		número de peças restantes do tabuleiro. O jogo acaba quando tiver somente uma peça disponível
#	n_finais:		contador de finais possíveis (posição [0]) e distintos (posição [1])
#	resultado:		lista de resultados distintos
#	linha_atual:	linha da peça sendo trabalhada
#	coluna_atual:	coluna da peça sendo trabalhada
#	tabuleiro:		tabuleiro do jan-ken-puzzle em jogo
#
def janKenPuzzle(n_linhas, n_colunas, n_pecas, n_finais, resultado, linha_atual, coluna_atual, tabuleiro):
	#caso base 1: a posição é vazia. Não faz nada
	if (tabuleiro[linha_atual][coluna_atual] == 0):
		return

	#caso base 2: chegou no final do jogo e houve um vencedor
	if (n_pecas == 1):
		n_finais[0] += 1		#aumenta o número de finais

		#Checando se a solução final é um resultado distinto
		if (verificarResultadoDistinto(resultado, linha_atual, coluna_atual, tabuleiro[linha_atual][coluna_atual], n_finais) == True):
			n_finais[1] += 1
			linha_resultado = [0, 0, 0]

			#atribui linha, coluna e peça para o vetor de resultados distintos
			linha_resultado[0] = linha_atual + 1
			linha_resultado[1] = coluna_atual + 1
			linha_resultado[2] = tabuleiro[linha_atual][coluna_atual]

			#aumenta a matriz de resultados
			resultado.append(linha_resultado)

	#ainda não chegou no final do jogo
	else:
		peca_atual = tabuleiro[linha_atual][coluna_atual]

		#verificando a peça adjacente à direita da peça atual,
		#sendo que deve estar dentro dos parâmetros do tabuleiro.
		if (coluna_atual < n_colunas - 1):
			peca_adj = tabuleiro[linha_atual][coluna_atual + 1]

			#verificando se é uma posição vazia
			if (peca_adj != 0):
				#há uma peça naquela posição. Verifica-se se é possível destruí-la
				if(peca_atual + 1 == peca_adj or peca_atual - 2 == peca_adj):
					tabuleiro[linha_atual][coluna_atual] = 0				#atualiza a posição
					tabuleiro[linha_atual][coluna_atual + 1] = peca_atual	#atualiza a posição adjacente

					#Testa a porra toda tudo de novo (merda ineficiente do caralho)
					for i in range(n_linhas):
						for j in range(n_colunas):
								janKenPuzzle(n_linhas, n_colunas, n_pecas - 1, n_finais, resultado, i, j, tabuleiro)

					tabuleiro[linha_atual][coluna_atual] = peca_atual	#recupera a posição
					tabuleiro[linha_atual][coluna_atual + 1] = peca_adj	#recupera a posição adjacente


		#verificando a peça adjacente abaixo da peça atual,
		#sendo que deve estar dentro dos parâmetros do tabuleiro.
		if (linha_atual < n_linhas - 1):
			peca_adj = tabuleiro[linha_atual + 1][coluna_atual]

			#verificando se é uma posição vazia
			if (peca_adj != 0):
				#há uma peça naquela posição. Verifica-se se é possível destruí-la
				if(peca_atual + 1 == peca_adj or peca_atual - 2 == peca_adj):
					tabuleiro[linha_atual][coluna_atual] = 0				#atualiza a posição
					tabuleiro[linha_atual + 1][coluna_atual] = peca_atual	#atualiza a posição adjacente
					
					#Testa a porra toda tudo de novo (merda ineficiente do caralho)
					for i in range(n_linhas):
						for j in range(n_colunas):
								janKenPuzzle(n_linhas, n_colunas, n_pecas - 1, n_finais, resultado, i, j, tabuleiro)

					
					tabuleiro[linha_atual][coluna_atual] = peca_atual	#recupera a posição
					tabuleiro[linha_atual + 1][coluna_atual] = peca_adj	#recupera a posição adjacente


		#verificando a peça adjacente à esquerda da peça atual,
		#sendo que deve estar dentro dos parâmetros do tabuleiro.
		if (coluna_atual > 0):
			peca_adj = tabuleiro[linha_atual][coluna_atual - 1]

			#verificando se é uma posição vazia
			if (peca_adj != 0):
				#há uma peça naquela posição. Verifica-se se é possível destruí-la
				if(peca_atual + 1 == peca_adj or peca_atual - 2 == peca_adj):
					tabuleiro[linha_atual][coluna_atual] = 0				#atualiza a posição
					tabuleiro[linha_atual][coluna_atual - 1] = peca_atual	#atualiza a posição adjacente
					
					#Testa a porra toda tudo de novo (merda ineficiente do caralho)
					for i in range(n_linhas):
						for j in range(n_colunas):
								janKenPuzzle(n_linhas, n_colunas, n_pecas - 1, n_finais, resultado, i, j, tabuleiro)

					
					tabuleiro[linha_atual][coluna_atual] = peca_atual	#recupera a posição
					tabuleiro[linha_atual][coluna_atual - 1] = peca_adj	#recupera a posição adjacente


		#verificando a peça adjacente acima da peça atual,
		#sendo que deve estar dentro dos parâmetros do tabuleiro.
		if (linha_atual > 0):
			peca_adj = tabuleiro[linha_atual - 1][coluna_atual]

			#verificando se é uma posição vazia
			if (peca_adj != 0):
				#há uma peça naquela posição. Verifica-se se é possível destruí-la
				if(peca_atual + 1 == peca_adj or peca_atual - 2 == peca_adj):
					tabuleiro[linha_atual][coluna_atual] = 0				#atualiza a posição
					tabuleiro[linha_atual - 1][coluna_atual] = peca_atual	#atualiza a posição adjacente

					#Testa a porra toda tudo de novo (merda ineficiente do caralho)
					for i in range(n_linhas):
						for j in range(n_colunas):
								janKenPuzzle(n_linhas, n_colunas, n_pecas - 1, n_finais, resultado, i, j, tabuleiro)
					
					tabuleiro[linha_atual][coluna_atual] = peca_atual	#recupera a posição
					tabuleiro[linha_atual - 1][coluna_atual] = peca_adj	#recupera a posição adjacente


# verificarResultadoDistinto(resultado, linha_atual, coluna_atual, peca, n_finais): verifica se
# 	um dado resultado encontrado do jogo é distinto dos demais.
# 
# Parâmetros:
#	resultado: lista de resultados distintos
#	linha_atual e coluna_atual: posição do resultado encontrado
#	peca: peça do resultado encontrado
#	n_finais: indica o número de finais (possíveis e distintos)
# 
def verificarResultadoDistinto(resultado, linha_atual, coluna_atual, peca, n_finais):
	#lista contém pelo menos uma entrada
	for i in range(n_finais[1]):
		#compara todas as informações de um resultado com o resultado atual: linha, coluna e peça
		if ((resultado[i][0] == linha_atual + 1) and (resultado[i][1] == coluna_atual + 1) and (resultado[i][2] == peca)):
			return False

	return True


# bubbleSort(resultado, n_finais): Ordena a lista de resultados distintos, com os seguintes critérios:
#	#	linha: critério primário
#	#	coluna: critério secundário
#	#	peça: critério terciário
#
# Parâmetros: 
#	resultado: lista de resultados distintos
#	n_finais: indica o número de finais (possíveis e distintos)
#
def bubbleSort(resultado, n_finais):
	aux = 0;

	for i in range(n_finais[1]):

		for j in range(i + 1, n_finais[1]):
			#critério de ordenação 1: linha
			if(resultado[i][0] > resultado[j][0]):
				switchBubbleSort(resultado, i, j)

			else:
				#critério de ordenação 2: coluna
				if(resultado[i][0] == resultado[j][0]):
					if(resultado[i][1] > resultado[i][1]):
						switchBubbleSort(resultado, i, j)

					else:
						#critério de ordenação 3: peça
						if(resultado[i][1] == resultado[j][1]):
							if(resultado[i][2] > resultado[j][2]):
								switchBubbleSort(resultado, i, j)

#
# switchBubbleSort(resultado, pos1, pos2): troca duas listas de resultados de linha, na matriz.
#
# Parâmetros:
#	resultado: lista de resultados distintos
#	pos1 e pos2: posições da lista a serem trocadas 
def switchBubbleSort(resultado, pos1, pos2):
	switch(resultado, pos1, pos2, 0)
	switch(resultado, pos1, pos2, 1)
	switch(resultado, pos1, pos2, 2)

#
# switch(resultado, pos1, pos2, col): troca uma coluna de duas listas de resultados de linha, na matriz.
#
# Parâmetros:
#	resultado: lista de resultados distintos
#	pos1 e pos2: posições da lista a serem trocadas 
#	col: coluna da matriz a ser trocada
#
def switch(resultado, pos1, pos2, col):
	aux = resultado[pos1][col]
	resultado[pos1][col] = resultado[pos2][col]
	resultado[pos2][col] = aux


#################################### 
#								   #
# 			FUNÇÃO MAIN			   #
# 							       #
#################################### 
def main():
	#primeira linha da entrada de dados
	primeira_entrada = input() 

	#separa os valores da entrada em duas posições
	r_c_str = primeira_entrada.split(" ") 

	#atribui r para o número de linhas e c para o número de colunas do tabuleiro
	r = int(r_c_str[0]) 
	c = int(r_c_str[1])

	#criação do tabuleiro de jan ken puzzle
	tabuleiro = []
	n_pecas = criarTabuleiro(r, c, tabuleiro)

	#matriz de resultados, sendo:
	#	[i][0] - linha do resultado
	#   [i][1] - coluna do resultado
	#   [i][2] - peça do resultado
	resultado = []

	n_finais = [0, 0]		#número de finais (possíveis [0] e distintos [1])

	#backtracking - jan ken puzzle, começando pela posição [i][j] do tabuleiro
	for i in range(r):
		for j in range(c):
			janKenPuzzle(r, c, n_pecas, n_finais, resultado, i, j, tabuleiro)

	#Ordenando a lista de resultados distintos, com os seguintes critérios:
	#	linha: critério primário
	#	coluna: critério secundário
	#	peça: critério terciário
	bubbleSort(resultado, n_finais)

	### Saída ###
	print(str(n_finais[0]))			#número de finais possíveis
	print(str(n_finais[1]))			#número de finais distintos
	#lista de finais distintos
	for i in range(n_finais[1]):
		print(str(resultado[i][0]) + " " + str(resultado[i][1]) + " " + str(resultado[i][2]))

#roda o programa
main()
