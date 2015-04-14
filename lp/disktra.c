#include<stdio.h>
#include<stdlib.h>
#define INF 0x3f3f3f3f

void imp_grafo(int grafo[6][6])
{
  int i,j;
  
  printf("GRAFO DO SISTEMA\n\n");
  for (i=0;i<6;i++)
  {  
    for (j=0;j<6;j++)
      printf("%3d ",grafo[i][j]);
    printf("\n");
  }
}


void dig_origem_destino(int *origem, int *destino)
{
     
  printf("digite a origem - numeros entre '0' e '5': ");
  fflush(stdin);
  scanf("%d",&*origem);
  printf("\n");
 
  printf("digite o destino - numeros entre '0' e '5':: ");
  fflush(stdin);
  scanf("%d",&*destino);
  printf("\n");
}    

void inicializa(int *foi, int *custo, int *prec, int *estima)  //inicializa as variáveis.
{
  int i;
            
  for(i=0 ; i<6 ; i++) //foi "visitado", custo "peso", prec "precedente" e estima "armazena o menor custo". 
  { 
    

    foi[i]= 0;
    custo[i] = INF;
    prec[i]=INF;
    estima[i]= INF;

 
    
  }

}


void printDados(int *estima , int *custo){

  int i = 0;
 for(i=0 ; i<6 ; i++) 
  { 
 
     printf("Custo = %d \n Estima = %d \n",custo[i],estima[i]);

 
    
  }

}

int estima_menor(int *estima, int *menor, int *posicao) //define qual o próximo nó a ser visitado
{
  int i;   
  *menor = estima[0];
  *posicao = 0;
  
  for (i=0;i<6;i++)   //percorre todos os elementos de estima e identifica quem tem o menor custo. 
  {
     if (estima[i] < *menor) 
     {
         *menor = estima[i];    //quando atualizar menor, salva em posicao o índice (corresponde ao nó a ser visitado).
         *posicao = i;
     }
  }

  estima[*posicao]=INF;  //Na próxima análise de estima o valor "menor atual" não fará parte, pois agora é número infinito.
  return *posicao;   //retorna o índice da estima que corresponde ao nó de menor custo.
}


void calc_peso(int *estima, int *menor, int *posicao, int *foi, int origem, int destino, int *custo, int *prec, int grafo[6][6])
{                         //função para calcular os custos.
  int k,j;   
  foi[origem]=0;       //o primeiro nó já recebe os valores.
  custo[origem] = 0; 
  prec[origem] = origem;
  k = origem;   // usa-se o 'k' como sendo o vertice a ser visitado.
     
     
  while(!foi[destino])  //enquanto o nó do destino ainda não foi visitado... 
  {
    
      if(!foi[k])                //se o nó atual não foi visitado...
        for(j=0 ; j<6 ; j++)       //visita os vizinhos.
          if ((grafo[k][j]) > 0)    //se o visinho tiver custo maior que zero...
          { 
            grafo[j][k]*=(-1);    //marca o caminho inverso do nó ao precedente para não ser visitado novamente.
           
            if(custo[j]>custo[k]+(grafo[k][j])) //se custo do nó for menor do que o calculado antes...
              {
                prec[j]=k;                        //atualiza o precedente.
                custo[j]=custo[k]+(grafo[k][j]);  //atualiza o custo.
                estima[j]=custo[j];               //guarda o custo do nó, para despois ver quem tem o menor custo e ser escolhido como próximo nó a ser visitado.
                
              }
                                 
          }
   
    foi[k]=1;  //marca o nó como visitado.
    k=estima_menor(estima,menor,posicao);   //atualiza  o nó a ser visitado, verificando qual tem o menor custo.
    printf("%d",k);
    char h = getchar();
  }
}

void faz_caminho(int *caminho, int destino, int *prec, int *cont_caminho, int origem,int *estima, int *custo)
{                         //função que guarda no vetor caminho, a rota para traçar o caminho de menor custo.
  int i,j;                //obs. caminho[0] guarda o último nó e caminho[cont_caminho] guarda o nó origem
  
  caminho[0]= destino;   //guarda em caminho[0] o nó destino.
  i=1;
  j=destino;
  
  
  while (prec[j] >=0)  //enquanto o precedente do nó não é zero "nó de origem", ou seja, enquanto não chega na origem.
  { 
    (*cont_caminho)++;    //incrementa o contador para saber o tamanho do vetor caminho.
    caminho[i]=prec[j];  //caminho[0] já preenchido. Caminho (a partir do 1) com o valor do precedente do nó atual j.
    i++;
    j=prec[j];     //faz o nó atual ser o seu precedente.
    if (j==origem)   //se nó atual igual a origem, significa que chegou na origem e a rota completa já está guardada no vetor caminho.
      break;
  
  }
    
}

void imprime_caminho(int *caminho, char *vertices, int origem, int destino, int cont_caminho,int *custo)
{                        //função para imprimir a rota armazenada no vetor caminho.
  int k,j,i,contador;
    
  k=cont_caminho;    //atualiza k com o tamanho do vetor caminho.
  contador=k;        //contador para diferenciar a impressão do destino. 
  
  while (k>=0)
  {  
    j=k;
    i=caminho[j];    //armazena em i o valor de caminho para depois fazer a equivalencia com os vértices "ABCDEF".
    if (contador>0)
      printf("%c -> ",vertices[i]);
    else                               //contador não foi maior que zero, ou seja, é o último nó a ser impresso...
      printf("%c\n",vertices[i]);     //não aparece a seta.
    k--;                              //decrementa k para imprimir o próximo caminho
    contador--;                      //decrementa o contador que não deixará imprimir a seta para o último nó.
    
  }
  
  printf("\n");
  printf("o MENOR custo entre '%c' e '%c' eh: %d\n\n\n\n",vertices[origem],vertices[destino],custo[destino]);
  
}




main()
{
  
  int * caminho = (int*)malloc(sizeof(caminho));
  int menor,estima[6],posicao;
  int foi[6], custo[6],prec[6], origem=0,destino=1;
  char vertices[6]={'A','B','C','D','E','F'};
  
  
  
 
 do{
       
  int grafo[6][6]={{0,7,9,0,0,14},{7,0,10,15,0,0},{9,10,0,11,0,2},{0,15,11,0,6,0},{0,0,0,6,0,9},{14,0,2,0,9,0}};
  int cont_caminho=0;    //zera o contador que indica o tamanho do vetor caminho
  

  printf("conforme GRAFO, digite a origem e destino \n");
  printf("para SAIR - digite origem '0' e destino '0'\n\n");

  dig_origem_destino(&origem,&destino);
  
  if(origem==destino)
  {
    printf("PROGRAMA FINALIZADO\n");    
    break; 
  }  

  inicializa(foi,custo,prec,estima);  //inicializa as variáveis.
   calc_peso(estima, &menor,&posicao,foi,origem,destino,custo,prec,grafo); //calcula os custos
  printDados(estima,custo);
   faz_caminho(caminho,destino,prec,&cont_caminho,origem,estima,custo);
   imprime_caminho(caminho,vertices,origem,destino,cont_caminho,custo);
  /*
  
  
  
   
  faz_caminho(caminho,destino,prec,&cont_caminho,origem,estima,custo); //armazena o caminho de menor custo

  imprime_caminho(caminho,vertices,origem,destino,cont_caminho,custo);  //imprime o caminho de menor custo
  
  system("pause");*/
  
}while(origem!=destino);
  
     



}