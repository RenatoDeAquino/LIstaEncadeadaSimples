import os
import time
#criação da classe node
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
    ponteiro = lista.headval
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
            
lista = ListaEncadeadaSimples()

user_input = 0

while user_input != 6:
  os.system("clear")
  print("Bem vindo a minha lista encadeada")
  print("diga o que deseja fazer")
  print("(1) - Adicionar elemento no inicio da lista")
  print("(2) - Adicionar elemento no final da lista")
  print("(3) - Adicionar após um elemento")
  print("(4) - Remover elemento")
  print("(5) - Mostrar a lista")
  print("(6) - Sair")
  
  user_input = int(input("->"))
  switch(user_input):
  case(1):
  if user_input == 1:
    os.system("clear")
    print("Diga o que deseja incluir na lista encadeada")
    user_input = input("->")
    lista.insere_inicio(user_input)
    print("Elemento inserido com sucesso")
    time.sleep(1)
  
  if user_input == 2:
    os.system("clear")
    print("Diga o que deseja incluir na lista encadeada")
    user_input = input("->")
    lista.insere_final(user_input)
    print("Elemento incluidos com sucesseo")
    time.sleep(1)

  if user_input == 3:
    os.system("clear")
    print("Diga o que deseja incluir na lista encadeada")
    user_input = input("->")
    print("Diga após qual elemento você deseja incluir")
    reference = input("->")
    a = lista.headval
    while a.dataval != reference:
      a = a.nextval
    lista.insere_no_meio_de_2_nodes(a,user_input)
    print("Elemento inserido com sucesso")
    time.sleep(1)
  
  if user_input == 4:
    os.system("clear")
    print("Qual elemento deseja remover da lista encadeada")
    user_input = input("->")
    if lista.headval == None or lista.headval.dataval == None:
      print("A lista já está vazia")
    else:
      lista.remove(user_input)
      print("Elemento Excluido com sucesso")
      time.sleep(1)
  
  if user_input == 5:
    os.system("clear")
    if lista.headval == None or lista.headval.dataval == None:
      print("Não possui elemento na lista")
      time.sleep(1)
    else:
      lista.mostra_lista()
      time.sleep(1)
os.system("clear")