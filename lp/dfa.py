
estados = ['q1','q2','q3','q4']
dados  =  [0,1]
print dados
grafo = {'q0': {'q1':0, 'q0':1},
	'q1':  {'q0':0, 'q2':1},
	'q2':  {'q3':0, 'q4':1},
	'q3':  {'q4':0, 'q1':1},
	'q4':  {'q0':0, 'q1':1}}
lista_entrada = [0,0,0,1,1]
lista_final = ['q1','q2']


def defineEstado(est):
	global lista_final,inicial
 	if est.count(">") == 1: 		
		inicial = est.replace(">","")
	if est.count(">*") == 1:
       	 lista_final.append(est.replace(">*",""))
   	elif est.count('*') ==1:
		lista_final.append(est.replace("*",""))
[ defineEstado(i) for i in estados]

def removeE(lis):
	i = 0
	while i < len(lis):
  			if lis[i] == 'e':
      	 			lis.pop(i)
   			else:
      		 		i += 1	
	
	return lis		

def difEsta(tes,lis):
	lista = []
	tes = tes.split(',')
	for i in tes:
		lis.append(i)
	return lis 	
	

def automato(grafo,i,aux):
	vez = 1
	print("entrou na validacao\n lista entrada->")
	global lista_entrada
	lista_entrada = list(set(lista_entrada))
	print lista_entrada
	if(aux == 2):
		print("acabou seu arrombado")
	print("\n\n")
	lista = []
	print("a lista inicia")
	print lista
	if vez == 1:
		for k in lista_entrada:
			print("\n validando vazio =: &->")
			print k
			print grafo[k,'&']
			tam = grafo[k,'&']
			print len(tam)
			if(len(tam) > 3):
				lista = difEsta(grafo[k,'&'],lista)				
			else:
				lista.append(grafo[k,'&'])				
				print lista
			vez=2
	if vez == 2:
		print "opa=:"
		print lista
		lista = list(set(lista))
		lista = removeE(lista)

		for j in lista_entrada:	
		   		print j			
				print("\n validando => "+i)
				print grafo[j,i]
				tam = grafo[j,i]
				print len(tam)
				if(len(tam) > 3):
					lista = difEsta(grafo[j,i],lista)
				else:					
					lista.append(grafo[j,i])
	
	print("aqui esta lista->");	
	lista = removeE(lista)	
	print lista
	lista_entrada = lista
	print lista_entrada
			
	    	#lista_entrada.append(grafo[j,i])
	
print grafo['q0'][0]

"""
for i in lista_entrada:
	for j in lista_final:
		if i == j:
	
		
if aux==0:
	print("automato nao aceito")
	tkMessageBox.showinfo("automato aceito","String nao acieta ")
#print(grafo(['>*q1',i])
"""