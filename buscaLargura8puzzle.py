import numpy  as np 
import copy

meta = np.array(range(9)).reshape((3,3)) #gerando matriz meta 3x3
meta2 = np.array(range(9)).reshape((3,3)) #gerando matriz de teste

#array de estados da matriz
estado = []

#checando se uma matriz e igual a matriz a meta
def check(puzzle,meta): return np.array_equal(puzzle,meta)

#verificar se tem elemento repetido na array
def verificArrayIqual(estados,meta):
	for i in estados:
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


#funcao de buscar em largura
def bfs(puzzle):
	movedir = moveToLeft(puzzle)
	moveesq = moveToRigth(puzzle)   
	movedown = moveToDown(puzzle)
	movetop = moveToTop(puzzle)

	if(verificArrayIqual(estado,movedir) == False):
		estado.append(movedir)
	if(verificArrayIqual(estado,movetop) == False):
		estado.append(movetop)		
	if (verificArrayIqual(estado,moveesq)== False):
		estado.append(moveesq)	
	if(verificArrayIqual(estado,movedown) == False):
		estado.append(movedown)





#mini = [[1,2,3],[4,5,0],[6,7,8]]

#matriz inicial para testes
 
meta2[0][0] = 1
meta2[0][1] = 2
meta2[0][2] = 3
meta2[1][0] = 4
meta2[1][1] = 5
meta2[1][2] = 0
meta2[2][0] = 6
meta2[2][1] = 7
meta2[2][2] = 8


#add matriz inical ao array de estados da matriz
estado.append(meta2)

print " Estado inicial"
print estado[0]
print "-------------"
cont = 0

#verifica se estado atual (matriz atual) e a meta
while check(estado[cont],meta) != True:
	#chama a funcao que expande a matriz realizando os movimento
	bfs(copy.deepcopy(estado[cont]))
	cont = cont + 1
	if (cont % 1000 == 0):
		print cont

print cont















