lista_a_z = []
def listar_frutas():
  with open('Frutas de A a Z.txt') as f:
    for l in f:
      qualquer = l[:-2].split(";")
      lista_a_z.append(qualquer)
  return lista_a_z
     
def jogar():
  escolha = escolher_palavra()
  forca(escolha)

def forca(palavra):
  tam = len(palavra)
  falta = True
  while falta:  
    print('''
_______
| /   |
|/
|

    ''',)
    print(palavra_montada)
    print(tam*" _")

    print("Informe uma letra")
    res = input()
    indices = verifica_exist(res, palavra, tam)
    for i in range(0,tam-1):
     # if palavra[i] == indices[]
'''
def verifica_exist(letra, palavra, tam):
  lista_index = []
  for l in range(0,tam-1):
    if palavra[l] == letra:
      lista_index.Append(l)
  return lista_index
'''

def escolher_palavra():
  lista = listar_frutas()
  from random import randint
  i = randint(0, 24)
  
  coluna = lista[i]
  tam_col = len(coluna)
  
  j = randint(0, tam_col-1)

  palavra = coluna[j]
  print("palavra escolhida: ", palavra)
  return palavra


#########################################
print("""
Vamos jogar forca?

""")
asw = input()

while asw == "s":
  jogar()
  print("""
  Vamos jogar forca?
  """)
  asw = input()
