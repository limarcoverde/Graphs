from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sys
import networkx as nx

def verif(vertices,vertice):
        for i in range(0,len(vertices),1):
                if(vertices[i] == vertice):
                        return False
        return True

def verif2(position1,position2,vertices):
  flag = 0
  for i in range(len(vertices)):
    if(position1 == vertices[i]):
      flag += 1
    elif(position2 == vertices[i]):
      flag += 1
  
  if(flag == 2):
    return True
  else:
    return False

def insert(lines,MainWindow):
  newArray = []
  nodesLote = []
  edgesLote = []
  newNodes = []
  newEdges = []
  valOrNot = 0
  strvalOrNot = ""
  for i in range(len(lines)):
    newArray.append(lines[i].split("\n")[0].split(" "))

  # Verifica se quem são os vertices e arestas
  for i in range(len(newArray)):
    if(len(newArray[i]) == 1 and verif(nodesLote,newArray[i])):
      nodesLote.append(newArray[i])
    elif((len(newArray[i]) == 2 or len(newArray[i]) == 3)):
      edgesLote.append(newArray[i])
  # Ajuste dos dados
  for i in range(len(nodesLote)):
    newNodes.append(nodesLote[i][0])
  # Verificação de erros e descobrir se o grafo é ou não valorado
  for i in range(len(edgesLote)):
    if(valOrNot == 0):
        valOrNot = len(edgesLote[i])

    if(len(edgesLote[i]) == 3 and valOrNot == len(edgesLote[i])):
      strvalOrNot = "Valorado"
    elif(len(edgesLote[i]) == 2 and valOrNot == len(edgesLote[i])):
      strvalOrNot = "não Valorado"
    else:
      if(len(edgesLote[i]) == 2 or len(edgesLote[i]) == 3):
        QMessageBox.about(MainWindow, "Aviso!", "o grafico é "+strvalOrNot+", tem uma linha do arquivo não respeitando a regra\n")
        edgesLote.remove(edgesLote[i])
      else:
        QMessageBox.about(MainWindow, "Aviso!", "Coloque dois ou três valores como aresta\n")
      valOrNot = 0

  # Adicionar corretamente ao ajuste do plot o array de arestas
  if(strvalOrNot == "Valorado"):
    for i in range(len(edgesLote)):
      newEdges.append(edgesLote[i][0]+" "+edgesLote[i][1]+" "+edgesLote[i][2])
  else:
    for i in range(len(edgesLote)):
      newEdges.append(edgesLote[i][0]+" "+edgesLote[i][1])

  return newNodes,newEdges,strvalOrNot

def nValorado(G,edges,nodes):
  tupla = []
  edge = []
  ## colocando o valor das arestas em um array de tuplas para inserção no plot
  for i in range(len(edges)):
    edge = edges[i].split(" ")
    if(verif2(edge[0],edge[1],nodes)):
      tupla.append((edge[0],edge[1]))

  ## Aqui precisamos verificar quais são os vertices que não vão ter arestas
  newTuple = []
  noEdges = []
  for i in range(len(tupla)):
    newTuple += tupla[i]
  newTuple = list(dict.fromkeys(newTuple))
  #gera a lista com os vertices que não contem arestas
  x = set(nodes)
  y = set(newTuple)
  noEdges = x.difference(y)
  noEdges = list(noEdges)

  ## inserindo no plot os vertices que tem ligações
  if(len(tupla)> 0):
    G.add_edges_from(tupla)
  ## inserindo no plot os vertices que não tem ligaçõe
  for i in range(len(noEdges)):
    G.add_node(noEdges[i])

  return G

def valorado(G,edges,nodes):
  tupla = []
  weight = []
  edge = []
  # Aplicando os valores dos vertices a um dicionario onde a key são as ligações e o valor da aresta o valor da key. Ex. {('1','2') : 15}
  for i in range(len(edges)):
    edge = edges[i].split(" ")
    if(verif2(edge[0],edge[1],nodes)):
      tupla.append((edge[0],edge[1]))
      weight.append(int(edge[2]))
  res = dict((tupla[sub], weight[sub]) for sub in range(len(tupla))) 
  
  ## Aqui precisamos verificar quais são os vertices que não vão ter arestas 
  newTuple = []
  noEdges = []
  for i in range(len(tupla)):
    newTuple += tupla[i]
  newTuple = list(dict.fromkeys(newTuple))
  x = set(nodes)
  y = set(newTuple)
  noEdges = x.difference(y)
  noEdges = list(noEdges)

  ## inserindo no plot os vertices que tem ligações
  G.add_edges_from(tupla)
  ## inserindo no plot os vertices que não tem ligações
  for i in range(len(noEdges)):
    G.add_node(noEdges[i])

  return G,res

def insertion(in1,MainWindow):
  try:
    nodes = []
    edges = []
    strvalOrNot = ''
    nodes,edges,strvalOrNot = insert(in1,MainWindow)
    return nodes,edges,strvalOrNot
  except:
    print("Error")

def direction(dirOrNot):
  if(dirOrNot == 1):
          G = nx.DiGraph()
  elif(dirOrNot == 0):
          G =  nx.Graph()
  
  return G

def valOrNot(strvalOrNot,G,edges,nodes):
  ## 1 ao 7 quesito
  if(strvalOrNot == "Valorado"):
    G,res = valorado(G,edges,nodes)
    return G,res
  elif(strvalOrNot == "não Valorado"):
    G = nValorado(G,edges,nodes)
  else:
    G = nValorado(G,edges,nodes)
  res = []
  return G,res