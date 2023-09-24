# Eduardo Veit Ferrão	 - 3215018
# Leonardo Biagiotti Beloti - 32160062
# Lucas Damasceno da Cunha Lima - 32132611
# Lucas Iudi Corregliano Gallinari - 32138628
# Yiou Wu - 32123213
# Turma 06G

class UBS:
  def __init__(self,ID, NOME):
    self.id = ID
    self.nome = NOME
    self.instalacao= [["0" for i in range(2)] for j in range(12)]
    self.instalacao[0][0]="Descrição"
    self.instalacao[0][1]="Salas"
    # daqui para baixo
    self.instalacao[1][0]="CLINICAS BASICAS"
    self.instalacao[2][0]="CLINICAS ESPECIALIZADAS"
    self.instalacao[3][0]="CLINICAS INDIFERENCIADO"
    self.instalacao[4][0]="CONSULTORIOS MEDICOS" 
    self.instalacao[5][0]="ODONTOLOGIA"
    self.instalacao[6][0]="OUTROS CONSULTORIOS NAO MEDICOS"
    self.instalacao[7][0]="SALA DE CURATIVO"
    self.instalacao[8][0]="SALA DE ENFERMAGEM"
    self.instalacao[9][0]="SALA DE IMUNIZACAO"
    self.instalacao[10][0]="SALA DE NEBULIZACAO"
    self.instalacao[11][0]="SALA DE REPOUSO/OBSERVACAO"
    
class GrafoND:
  TAM_MAX_DEFAULT = 200 # qtde de vértices máxima default
  
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n # número de vértices
    self.m = 0 # número de arestas
    self.INF=[0]*n
    
    # matriz de adjacência
    self.adj = [[float('inf') for i in range(n)] for j in range(n)]
    #self.adj = [[0 for i in range(n)] for j in range(n)]

  def insereA(self, v, w, r):
    if self.adj[v][w] == float('inf'):
      #Atualiza para as duas
      self.adj[v][w] = r 
      self.adj[w][v] = r 
      self.m+=1 # atualiza qtd arestas
    elif self.adj[v][w] !=0:
      #Atualiza para as duas
      self.removeA(v,w)
      self.adj[v][w] = r 
      self.adj[w][v] = r 
      self.m+=1 # atualiza qtd arestas


  # remove uma aresta v->w do Grafo	
  def removeA(self, v, w):
    if self.adj[v][w] != float('inf') or self.adj[v][w] != 0:
      #self.adj[v][w] = 0
      #self.adj[w][v] = 0
      self.adj[v][w] = float('inf')
      self.adj[w][v] = float('inf')
      self.m-=1 # atualiza qtd arestas
      
  def show(self):
      print(f"\n n: {self.n:2d} ", end="")
      print(f"m: {self.m:2d}\n")
      for i in range(self.n):
          for w in range(self.n):
              if self.adj[i][w] == float('inf'):
                  print(f"Adj[{i:2d},{w:2d}] = " + str(float('inf')), end=" ") 
              elif self.adj[i][w] == 0:
                  print(f"Adj[{i:2d},{w:2d}] = 0", end=" ")
              else:
                  print(f"Adj[{i:2d},{w:2d}] = " + str(self.adj[i][w]), end=" ")
          print("\n")

      
      print("\nFim da impressão da matriz.")
      print("\r")

  def inserirVertice(self,NOME):
    matriz = [[float('inf') for i in range(self.n+1)] for j in range(self.n+1)]
    for i in range(self.n):
      for j in range(self.n):
        matriz[i][j]=self.adj[i][j]
    self.adj=matriz
    Node=UBS((len(self.INF)),NOME)
    self.INF.append(Node)
    self.n=self.n+1
    
  def RemoveVertice(self,vertice):
    for i in range(self.n):
      for j in range(self.n):
        if i>vertice and j<vertice and j<self.n and i<self.n:
          self.adj[i-1][j]=self.adj[i][j]
        if i<vertice and j>vertice and j<self.n and i<self.n:
          self.adj[i][j-1]=self.adj[i][j]
        if i>vertice and j>vertice:
          self.adj[i-1][j-1]=self.adj[i][j]
    self.n=self.n-1
    aux=[]
    num=0
    for i in self.adj:
      i.pop(self.n)
      if num!=self.n:
        self.m=self.m-1
        aux.append(i)
        num+=1
    self.adj=aux
    self.INF.remove(self.INF[vertice])
    self.m=0
    for i in range(self.n):
      for j in range(self.n):
        if(i>j and self.adj[i][j]!=float('inf')):
          self.m+=1
    

  def Conexo(self):
    n=1
    lista=[0]*self.n
    for j in range (self.n):
      Atual=j
      for i in range (self.n):
          if Atual!=i and (self.adj[Atual][i]!=float('inf')) and n<self.n and lista[n]!=i and not(i in lista):
              lista[n]=i
              n+=1
    lista=sorted(lista)
    teste=[]
    for i in range(self.n):
      teste.append(i)
      
    if(lista!=teste):
      return False
    return True

  #Pegar dados atuais que serão gravados no arquivo grafo.txt FUNCÀO 2
  def exibirDados(self):
    #cada index da array é uma linha da saida
    #tipo do grafo
    saida = [2]
    saida.append(self.n)
    #info das ubs
    for i in range(self.n):
      ubs = str(i) + " " + self.INF[i].nome
      x = self.FindUBS(self.INF[i].nome)      
      for j in range(1, len(self.INF[x].instalacao)):
          ubs += " " + str(self.INF[x].instalacao[j][1])
      saida.append(ubs)  
    #quantidade arestas
    saida.append(self.m)
    #caminhos e pesos
    for i in range(self.n):
      for w in range(i, self.n):
        if self.adj[i][w] != float('inf'):
          caminho = str(i) + " " + str(w) + " " + str(self.adj[i][w])
          saida.append(caminho)
    return saida
  
  def FindUBS(self,NOME):
    for i in range(self.n):
      if (self.INF[i].nome==NOME):
        return i
    return -1

  
  def FindUBS_Room(self,info,num):
    v=0
    for i in range(self.n):
        for b in range(11):
          if(str(self.INF[i].instalacao[b+1][0])==info and int(self.INF[i].instalacao[b+1][1]>=num)):
            print("Índice:",i)
            print("Nome:", self.INF[i].nome)
            print(self.INF[i].instalacao[b+1][0],"Salas:",self.INF[i].instalacao[b+1][1])
            print("\n")
            v+=1
    if(v==0):
      print("Erro, nome errado ou não exitem salas o suficiente")
  
  def UpdateUBS_Room(self,index,info,num):  
    self.INF[index].instalacao[info][1]=num

  def PrintUBS_info(self,NOME):
    x=self.FindUBS(NOME)
    if(x==-1):
      print(NOME,"Não encontrado")
    else:
      print("Índice:",x)
      print("Nome:",self.INF[x].nome)
      for i in range(len(self.INF[x].instalacao)):
        for j in range(len(self.INF[x].instalacao[i])):
          print(self.INF[x].instalacao[i][j], end="|")
        print("\n")
        
  def showUBS(self):
    for i in range(self.n):
      print("[",i,"]",self.INF[i].nome)  
    #print("\nFim da impressao das UBS.")
  
  def intersection(self,lst1, lst2):
    k=0
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
  
  def Dijkstra(self,origem):
    matriz=[]
    # cria a matriz
    for i in range(6):
      aux=[[]]*(self.n+1)
      matriz.append(aux)  
    for i in range(6):
      for j in range(self.n+1):
        if i==0 and j!=0:
          matriz[i][j]=j-1
        if i==1:
          if j==0:
            matriz[i][j]="dij"
          if j==origem+1:
            matriz[i][j]=0
          if j!=origem+1 and j!=0:
            matriz[i][j]=float('inf')
        if i==2:
          if j==0:
            matriz[i][j]="A"
          else:
            matriz[i][j]=j-1
        if j==0 and i==3:
          matriz[i][j]="F"
        if i==4:
          if j==0:
            matriz[i][j]="S"
        if i==5:
          if j==0:
            matriz[i][j]="Rota"
          else:
            matriz[i][j]=0
        if i ==j==0:
          matriz[i][j]='X'

    # primeira interação
    k=1
    aux=[]
    for i in range(self.n):
      if(self.adj[origem][i]!=float('inf')):
        matriz[1][i+1]=self.adj[origem][i]
        matriz[5][i+1]=origem
        aux.append(i)
        matriz[3][k]=origem
    matriz[2].remove(origem)
    matriz[4]=self.intersection(aux,matriz[2])
    
    menor=100
    for i in range(self.n-1):
      if (matriz[1][i+1]<menor and i!=origem):
        menor= matriz[1][i+1]
        r =i
    
    k+=1
    while(len(matriz[2])>1):
      r1=r
      v=0
      for i in range(self.n):
        if (matriz[1][i+1]>self.adj[r][i]+matriz[1][r+1]):
          
          matriz[1][i+1]=self.adj[r][i]+matriz[1][r+1]
          matriz[5][i+1]=r
          aux.append(i)
          matriz[3][k]=r
          v+=1
      if(v==0):
        matriz[3][k]=r
      matriz[2].remove(r)
      matriz[4]=self.intersection(aux,matriz[2])
      
      menor=100
      for i in range(self.n-1):
        if (i!= origem+1 and matriz[1][i+1]<menor and i in matriz[4]):
          menor= matriz[1][i+1]
          r =i
      if(r1==r and len(matriz[4])>0):
        r=matriz[4][0]
      
      k+=1
  
    return matriz[1], matriz[5]

  def ProcurarCaminho(self,Partida,Chegada):
    x=self.FindUBS(Partida)
    y=self.FindUBS(Chegada)
    distancia,rota=self.Dijkstra(x)
    x+=1
    y+=1
    print("Distancia Total: ",distancia[y])
    caminho=[y-1]
    while(x!=y):
      y=rota[y]+1
      caminho.append(y-1)
    caminho.reverse()
    for i in range(len(caminho)):
      if (i<len(caminho)-1):
        print(self.INF[caminho[i]].nome,"->",end="")
      else:
        print(self.INF[caminho[i]].nome)