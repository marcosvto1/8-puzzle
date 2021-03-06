import numpy  as np
from os import system
import copy

meta = np.array(range(9)).reshape((3,3)) #gerando matriz meta 3x3
meta2 = np.array(range(9)).reshape((3,3))  #gerando matriz de teste

#array de estados da matriz
estado = []
#array de estados visitados da matriz
estadoV = []

meta2[0][0] = 1
meta2[0][1] = 2
meta2[0][2] = 3
meta2[1][0] = 4
meta2[1][1] = 5
meta2[1][2] = 0
meta2[2][0] = 6
meta2[2][1] = 7
meta2[2][2] = 8

"""
meta2[0][0] = 1
meta2[0][1] = 0
meta2[0][2] = 2
meta2[1][0] = 3
meta2[1][1] = 4
meta2[1][2] = 5
meta2[2][0] = 6
meta2[2][1] = 7
meta2[2][2] = 8
"""
#checando se uma matriz e igual a matriz a meta
def check(puzzle,meta): return np.array_equal(puzzle,meta)

#verificar se tem elemento repetido na array
def verificArrayIqual(estados,meta):
	for i in estados:
		if(check(i,meta) == True):
			return True
	return False

#verificar se matriz atual ja foi visitada
def checkVisit(estadosVisitados,meta):
	for i in estadosVisitados:
		if(check(i,meta) == True):
			return True
	return False

#retorna o estado aleatorio da matriz (Estado Inicial do jogo)
def getPuzzle():
	puzzle = np.array(range(9))
	np.random.shuffle(puzzle)
	puzzle = puzzle.reshape((3,3))
	return puzzle 

#busca o indices do buraco da matriz
def searchZero(puzzle): return [(i,j) for i in range(3) for j in range(3) if puzzle[i][j] == 0][0]

#movendo buraco a esquerda
def moveToLeft(puzzle):

	i , j = searchZero(puzzle)

	if j - 1 >=0:
		puzzle2 = puzzle.copy()
		puzzle2[i][j -1] , puzzle2[i][j] = puzzle2[i][j] ,puzzle2[i][j -1]
		return puzzle2
	else:
		return puzzle.copy()

#movendo    buraco a direita
def moveToRigth(puzzle):

	i , j = searchZero(puzzle)

	if j + 1 < 3:
		puzzle2 = puzzle.copy()
		puzzle2[i][j +1] , puzzle2[i][j] = puzzle2[i][j] ,puzzle2[i][j + 1]
		return puzzle2
	else:
		return puzzle.copy()

#movendo buraco pra cima
def moveToTop(puzzle):

	i , j = searchZero(puzzle)

	if i - 1 >= 0:
		puzzle2 = puzzle.copy()
		puzzle2[i -1 ][j] , puzzle2[i][j] = puzzle2[i][j] ,puzzle2[i-1][j]
		return puzzle2
	else:
		return puzzle.copy()

#movendo buraco pra baixo
def moveToDown(puzzle):

	i , j = searchZero(puzzle)

	if i + 1 < 3:
		puzzle2 = puzzle.copy()
		puzzle2[i +1 ][j] , puzzle2[i][j] = puzzle2[i][j] ,puzzle2[i+1][j]
		return puzzle2
	else:
		return puzzle.copy()

#listando um vector de matriz
def printArray(arr):
	print "mostrando estados \n"
	for row in arr:
		print row

#funcao de buscar em profundidade
def bfs(puzzle):

	moveesq = moveToLeft(puzzle) 	 
	movedown = moveToDown(puzzle)
	movetop = moveToTop(puzzle)
	movedir = moveToRigth(puzzle)	

	if(verificArrayIqual(estado,moveesq) == False):
		estado.append(moveesq)
	if(verificArrayIqual(estado,movetop) == False):
		estado.append(movetop)		
	if (verificArrayIqual(estado,movedown)== False):
		estado.append(movedown)
	if(verificArrayIqual(estado,movedir) == False):
		estado.append(movedir)




#add matriz inical ao array de estados da matriz
estado.append(meta2)
cont =0
qtdI = 0
#verifica se estado atual (matriz atual) e a meta
while check(estado[len(estado)-1],meta) != True:
#for x in range(10):	
	#verifica se estado atual da matriz ja foi visitado
	while(checkVisit(estadoV,estado[len(estado)-1]) == True):
		#print "Entrou no checkVisit hahahaha:"
		v = estado.pop()
		#print v

	estadoAtual = estado.pop()
	estadoV.append(estadoAtual)
	#print "estado de Entrada"
	system("clear")
	print estadoAtual
	#print "----------------"
	#chama a funcao que expande a matriz realizado os movimento
	bfs(estadoAtual)
	if(cont == 0):
		del estado[0]	
	#print "Estados Visitados"
	#printArray(estadoV)
	#print "---------\nEstados"
	#printArray(estado)
	cont = cont + 1
	qtdI = qtdI + 1
	if (qtdI % 1000 == 0):
		print qtdI	

#fim

print "Final"
printArray(estadoV)














