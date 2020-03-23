# LstaEncadeadaSimples
O intuito do projeto é uma implementação de lista encadeada para fazer com que pessoas que estejam aprendendo tenham uma pequena implementação de uma funcionando para fazerem uma melhor

## Sobre o Projeto:
### Para baixar o projeto use o comando 
```sh
git clone https://github.com/RenatoDeAquino/ListaEncadeadaSimples
``` 

### Para rodar o programa
Rode o programa lista.py
caso esteja em uma máquina linux vá para a pasta do projeto e utilize o comando 
```sh
python3 lista.py
```

caso esteja em uma máquina windows vá para a pasta do projeto e utilize o comando
```sh
lista.py
```

#### Lista.py:
  No arquivo lista.py é a parte de "interface" com o usário onde ele pega as informações do usuario
#### Node.py:
No arquivo Node.py é a parte onde a lista está codificada
## Funções:
  #### Mostrar lista:
  pegando o inicio da lista percorre o proximo dela e colocando na tela a informação gravada
  #### insere inicio:
  pedindo para o usuário a informação que deseja ser guardada ele colocará ela na cabeça da lista, caso tenha um elemento na frente ele vai "empurrar" a lista para frente afim de deixar todas as ligações ainda verdadeiras
  #### insere final:
  pedindo para o usuário a informação que deseja ser guardada ele percorerá a lista até encontrar a cauda da lista e ai adicionar no próximo elemento da cauda o valor que deseja ser guardado
  #### insere no meio de 2 node:
  pedindo para o usuário a informação que deseja ser guardada e após qual node deseja ser guardado ele percorrerá a lista atrás do node que o usuário escolheu e então irá adicionar o elemento logo adiante e "empurando" a lista caso seja necessário
  #### remove
  pendindo para o usuario qual o Node que ele deseja remover ele percorerá a lista atrás do elemento e remover ele da lista e puxando a lista para continuar as ligações

## Autor
| <img src="https://user-images.githubusercontent.com/43344209/77370723-43bcc280-6d40-11ea-81e2-5d4922c9f4a1.jpeg" width="150"/> |
| :--------------------: |
| **Renato Aquino**      |
| Desenvolvedor Back-End |
