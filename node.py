class Node:
  def __init__(self,dataval = None):
    self.dataval = dataval
    self.nextval = None

#criação da classe ListaEncadeada Simples
class ListaEncadeadaSimples:
  def __init__(self):
    self.headval = None

  def mostra_lista(self):
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval
  
  def insere_inicio(self,newData):
    newNode = Node(newData)
    
    newNode.nextval = self.headval

    self.headval = newNode

  def insere_final(self,newData):
    newNode = Node(newData)

    if self.headval is None:
      self.headval = newNode
      return
    fim = self.headval
    while(fim.nextval):
      fim = fim.nextval
    fim.nextval = newNode
  
  def insere_no_meio_de_2_nodes(self, node_referencia, newData):
    if node_referencia is None:
      print("Node Não se encontra nessa lista")
      return
    newNode = Node(newData)
    newNode.nextval = node_referencia.nextval
    node_referencia.nextval = newNode
  
  def remove(self, oldData):
    ponteiro = self.headval
    if ponteiro == None:
      print("lista vazia")
    if ponteiro.dataval == oldData and ponteiro.nextval == None:
      ponteiro.dataval = None
    else:
      while oldData != ponteiro.dataval:
        anterior = ponteiro
        ponteiro = ponteiro.nextval
      if ponteiro.nextval == None:
        anterior.nextval = None
      else:
        anterior.nextval = ponteiro.nextval
        ponteiro = None
            