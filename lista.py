import os
import time
from node import Node, ListaEncadeadaSimples
#criação da classe node
node = Node()
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