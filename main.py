# Eduardo Veit Ferrão	 - 3215018
# Leonardo Biagiotti Beloti - 32160062
# Lucas Damasceno da Cunha Lima - 32132611
# Lucas Iudi Corregliano Gallinari - 32138628
# Yiou Wu - 32123213
# Turma 06G

from Grafos import UBS,GrafoND
import networkx as nx
import matplotlib.pyplot as plt

def Read():
   with open("grafo.txt", "r") as arquivo:
     for line in arquivo:
       for word in line.split():
         print(word,end=' ')
       print("\n")
     
def leitura():
  with open("grafo.txt", "r") as arquivo:
    origem, destino, rotulo = '', '', ''
    # Lê quantidade de vertices
    line = arquivo.readline()
    tipo = int(line[0])
    # Lê quantidade de arestas
    line = arquivo.readline()
    vertice= int(line)
    #print(vertice)
    g = GrafoND(vertice)
    Node=0
    for i in range(vertice):
      line = arquivo.readline()
      a=0
      x=0
      for word in line.split():
        if(a==0):
          x=int(word)
        elif(a==1):
          Node=UBS(x,word)
        else:
          Node.instalacao[a-1][1]=int(word)
        a+=1
      g.INF[x]=Node
      
    # Lê as ligações
    line = arquivo.readline()
    arestas=int(line)
    for i in range(arestas):
      line = arquivo.readline()
      a=0
      origem=-1
      destino=-1
      rotulo=1
      for word in line.split():
        if(a==0):
          origem=int(word)
        if(a==1):
          destino=int(word)
        if(a==2):
          rotulo=int(word)
        a+=1
      g.insereA(origem, destino, rotulo) 

    return g
    
def MostrarGrafo(g):
  i =g.n
  Grafo=nx.Graph()
  for x in range(i-1):
    Grafo.add_node(x+1)
  for a in range(i):
    for b in range(i):
      if (g.adj[a][b]!=float('inf')):
        Grafo.add_edge(a,b,weight=g.adj[a][b])
  nx.draw(Grafo, with_labels=True)

  plt.show()

# Gravar arquivo
def gravarArquivo(g):
  saida = g.exibirDados()
  with open("grafo.txt", "w+") as arquivo:
    for linha in saida:
      arquivo.write(str(linha) + "\n")
  print("\nArquivo 'grafo.txt' foi atualizado com sucesso\n")
  

def Menu():
  print("\n========== Mapeamento das UBSs de Guarulhos ==========\n") 
  print("[1] - Ler dados do arquivo grafo.txt")                            
  print("[2] - Gravar dados no arquivo grafo.txt") 
  print("[3] - Inserir vértice")
  print("[4] - Remover vértice")
  print("[5] - Inserir aresta")                       
  print("[6] - Remover aresta") 
  print("[7] - Exibir conteúdo do arquivo grafo.txt")
  print("[8] - Exibir dados que estão armazenados na memória")
  print("[9] - Exibir matriz de adjacência")
  print("[10] - O grafo é conexo?")  
  print("[0] - Encerrar a aplicação\n")                       
          
      
def main():
  flag = False
  Menu()

  while (flag is False):
    print("\rLeia os dados do arquivo antes de executar outro comando (opção [1])\n")
    comando=int(input("Comando: "))
  
    # Ler dados do arquivo grafo.txt
    if(comando==1):
      g = leitura()
      flag = True
      Menu()

  while True:
    comando=int(input("Comando: "))

    # Gravar dados no arquivo grafo.txt
    if(comando==2):
      gravarArquivo(g)

    # Inserir vértice
    elif(comando==3):
      nome=str(input("\nDigite o nome da nova UBS: "))
      g.inserirVertice(nome) 
      continuar="1"
      x=len(g.INF)-1
      for a in range(11):
          print("[",a+1,"]",g.INF[x].instalacao[a+1][0])
      while(continuar!="0" and x>-1):
        info=int(input("\nQual informação você deseja atualizar? "))
        numero=int(input("\nQuantas salas? "))
        if(numero>=0 and 12>=info>=1):
          #print(x)
          g.UpdateUBS_Room(x,info,numero)
        continuar=str(input("Você deseja continuar?\nSim = 1  Não = 0\n"))
      Menu()

    # Remover vértice
    elif(comando==4):
      nome=str(input("\nDigite o nome da UBS a ser removida: "))
      print("\r")
      x=g.FindUBS(nome)
      if(x>-1):
        g.RemoveVertice(x) 
      else:
        print(nome,"Não encontrado")

    # Inserir aresta
    elif(comando==5):
      g.showUBS()
      origem=int(input("\nDigite a origem: "))
      destino=int(input("Digite o destino: "))
      peso=int(input("Digite o peso: "))
      print("\r")
      g.insereA(origem,destino,peso)
      Menu()

    # Remover aresta
    elif(comando==6):
      g.showUBS()
      origem=int(input("\nDigite a origem: "))
      destino=int(input("Digite o destino: "))
      print("\r")
      g.removeA(origem,destino)
      Menu()

    # Exibir conteúdo do arquivo grafo.txt
    if(comando==7):
      Read()
      Menu()

    # Exibir dados que estão armazenados na memória
    elif(comando==8):
      saida = g.exibirDados()
      for info in saida:
        print(info)
      Menu()

    # Exibir matriz de adjacência
    elif(comando==9):
      g.show()
      Menu()

    # Mostra conexidade do grafo
    elif(comando==10):
      print("\nO grafo é conexo? ",g.Conexo())
      print("\r")

    # Encerra a aplicação
    elif(comando==0):
      exit()

    # Funções para a parte 2 do projeto
    '''
    # Exibir grafo com Matplotlib
    elif(comando==11):
      MostrarGrafo(g)

    # Exibir lista de UBS
    elif(comando==12):
      g.showUBS()
      Menu()

    # Listar informações da UBSs
    elif(comando==13):
      nome=str(input("\nDigite o nome da UBS: "))
      print("\n")
      x=g.FindUBS(nome)
      if(x>-1):
        g.PrintUBS_info(nome)
      else:
        print(nome,"UBS não encontrada")
      Menu()

    # Exibir caminho mínimo entre duas UBSs
    elif(comando==14):
      origem=str(input("\nDigite o nome da UBS Origem: "))
      x=g.FindUBS(origem)
      destino=str(input("\nDigite o nome da UBS Destino: "))
      print("\n")
      y=g.FindUBS(destino)
      if(x>-1 and y>-1):
        if (g.Conexo()):
          g.ProcurarCaminho(origem,destino)
      else:
        print("ERROR")

    # Buscar sala
    elif(comando==15):
      Sala=str(input("\nQue sala você procura? "))
      numero=int(input("\nQuantos salas deste tipo você procura? "))
      g.FindUBS_Room(Sala,numero)
      Menu()

    # Adicionar informação em uma UBS existente
    elif(comando==16):
      node=str(input("\nAdicionar informação em qual UBS: "))
      continuar="1"
      x=g.FindUBS(node)
      for a in range(11):
          print("[",a+1,"]",g.INF[x].instalacao[a+1][0])
      while(continuar!="0" and x>-1):
        info=int(input("\nQual informação você deseja atualizar? "))
        numero=int(input("\nQuantas Salas? "))
        if(numero>=0 and 12>=info>=1):
          g.UpdateUBS_Room(x,info,numero)
        continuar=str(input("Você deseja continuar?\nSim = 1  Não = 0\n"))
      Menu()'''


main()