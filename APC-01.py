
#Construir, gerir e analisar as estastísticas da ocupação de um restaurante!

#Entrada de dados:
'''
Configurações: Roda sessão de configurações, até o usuário solicitar atendimento.
.
a: área indicada do restaurante, será uma string
m: quantidade de mesas da área indicada, será um Inteiro
c: quantidade de cadeiras de mesas de determinada área, será um Inteiro
.
--Atendimento: Roda sessão de Atendimento, até o usuário fizer uma entrada -1.
.
comando:Indica comando selecionado, tipo Inteiro comandos [1, 2, 3, 4, -1]
texto: Indica o que alguns comandos precisam fazer.
.
-1 FINALIZA O PROGRAMA

Crie 3 listas:
1 - Uma para organização geral do restaurante
2 - Uma para saber quantas mesas disponíveis em cada área
3 - Uma para adicionar os grupos com sua permanência

Comece pela config e pela função que fecha o restaurante
'''

#Primeira coisa para ser feita na entrada de dados: Indicar de forma clara o que precisa ser lida, e aonde será guardado.
# comandos importantes: sort, index

from copy import deepcopy
G_org_restaurante = []
G_mesas_livres = []
G_grupos_permanencia = []
G_lista_mod = []


#G_lista_mesas_ocupadas [['area',cadeiras,pessoas,tempo_permanencia]]

# 


  # for elemento in lista:
    #config = []
    #config.append(area)
    #config.append(mesas)
    #config.append(cadeiras)
    #G_org_restaurante.append(config)

# for area in lista_areas:
#   for i in range(len(G_org_restaurante)):
#     if area == G_org_restaurante[i][0]:
#       # faz algo quando achar a area

#########if cont_comandos >= 6:
def tem_lugar(mesa,cadeira,area):
    
  contador = 0
  for mesas_ocupadas in G_lista_mesas_ocupadas:
    if mesas_ocupadas[0] == area and mesas_ocupadas[2] == cadeira:
      contador += 1
  if mesa < contador or len(G_lista_mesas_ocupadas) == 0:
    return True
  else:
    return False

def comando_1():
    entrada1 = input().split()
    pessoas = int(entrada1[4])
    area = entrada1[8]
    achou = False

    for i in range(len(G_mesas_livres)):
        menor_valor = 1000000000000
        area_restaurante = G_mesas_livres[i][0]
        if area == area_restaurante: #Area certa
            lista = G_mesas_livres[i][1]
            for elemento in lista:
              cadeira = elemento[1]
              mesa = elemento[0]
          
              if cadeira >= pessoas and (cadeira - pessoas)< menor_valor and mesa > 0:
                  menor_valor = cadeira - pessoas
                  cadeira_alvo = cadeira
                  mesa_alvo = mesa
                  mesa_e_cadeira_a_ser_ocup = G_mesas_livres[i][1].index(elemento)
                  achou = True
              
          
            if achou:
                print(f'Um grupo de {pessoas} pessoas ocupou uma mesa de {cadeira_alvo} lugares na area {area_restaurante}.')
                G_grupos_permanencia[i][1].append([pessoas,cadeira_alvo,0])
                G_mesas_livres[i][1][mesa_e_cadeira_a_ser_ocup][0] -= 1
                return pessoas
            else:
                print('Nao foi possivel levar o grupo de clientes para uma mesa.')
                return 0

def comando_2():
    ###CONSULTA DE MESAS###
    #Esse comando deve imprimir as áreas em ordem alfabética,
    #e logo abaixo deve apresentar a quantidade de mesas ocupadas de um total.
    #Exemplo-> VARANDA: (0 de 6 mesas)
    G_org_restaurante.sort()
    G_mesas_livres.sort()
    mesas_livres = 0
    total_mesas = 0
    posicao = 0
    for area in G_org_restaurante:
        for mesa in area[1]:
            total_mesas += mesa[0]
        area_livre = G_mesas_livres[posicao]
        for mesa in area_livre[1]:
            mesas_livres += mesa[0]
        print(f'{area[0]}: ({total_mesas - mesas_livres} de {total_mesas} mesas)')    
        mesas_livres = 0
        total_mesas = 0
        posicao += 1
    
def comando_3():
    ###CONSULTA DE LOTAÇÃO###
    #Imprime como saída uma lista com cada área, em ordem alfabética,
    #com a respectiva lotação atual e capacidade total.
    #Exemplo-> VARANDA: (0 de 40 pessoas)
    G_org_restaurante.sort()
    G_grupos_permanencia.sort()
    lugares_disponiveis = 0
    total_cadeiras = 0
    total_mesas = 0
    total_capacidade = 0
    posicao = 0
    for area in G_org_restaurante:
        for cadeiras in area[1]:
            total_cadeiras += cadeiras[1]
            total_mesas += cadeiras[0]
            total_capacidade += total_cadeiras * total_mesas
            total_mesas = 0
            total_cadeiras = 0
        area_livre = G_grupos_permanencia[posicao]
        for pessoas in area_livre[1]:
            lugares_disponiveis += pessoas[0]    
        print(f'{area[0]}: ({lugares_disponiveis} de {total_capacidade} pessoas)')    
        lugares_disponiveis = 0
        total_capacidade = 0
        posicao += 1

def comando_4():
    ###ADIÇÃO OU REMOÇÃO DE MESAS###
    #O comando 4 consiste em adicionar ou remover mesas com quantidade
    #específica de cadeiras em uma área
    #ENTRADA-> Quero OP mais Z mesas com X cadeiras cada na area Y
    #SAÍDA-> Z mesas de X cadeiras OP com sucesso na area Y.
    entrada1 = input().split()
    op = entrada1[1]
    mesas = int(entrada1[3])
    cadeiras = int(entrada1[6])
    area = entrada1[11]
    if op == "adicionar":
        for i in range(len(G_mesas_livres)):
            area_restaurante = G_mesas_livres[i][0]
            nAchou = True
            if area == area_restaurante:  # Area certa
                lista = G_mesas_livres[i][1]
                for elemento in lista:
                    cadeira = elemento[1]
                    mesa = elemento[0]
                    posicao = G_mesas_livres.index(mesa)
                    if cadeira == cadeiras:
                        mesa += mesas
                        nAchou = False
                        G_mesas_livres.pop(posicao)
                        G_mesas_livres.insert(posicao, mesa)
            

#     if C_org_restaurante[i][0] == area:
#         if cadeiras == restaurante[i]

#lista_temp = []
#lista_temp.appende(area)
#continhas
#lista_temp.append(mesas_ocup, mesas_totais)    
input()
while True:
    action = input('Area númeroMesas númeroCadeiras\n')
    if action == '--ATENDIMENTO':
        G_mesas_livres = deepcopy(G_org_restaurante)
        break
    flag_achou = False
    action = action.split()
    area = action[0]
    mesas = int(action[1])
    cadeiras = int(action[2])
    for elemento in G_org_restaurante:
      if elemento[0] == area:
        elemento[1].append([mesas,cadeiras])
        flag_achou = True

    if flag_achou == False:
        G_org_restaurante.append([area,[[mesas,cadeiras]]])
        G_grupos_permanencia.append([area,[]])
print(G_org_restaurante)        
    #verificar se já existe a quantidade de cadeiras
    #Se já existir, adicionar + a quanitdade de mesas na posição 0
#for i in range(len(G_org_restaurante)):
  #area_restaurante = G_org_restaurante[i][0]
  #lista = G_org_restaurante[i][1]
  #print(G_org_restaurante)
  #lista.sort(key=lambda x : x[1])
quantidade_de_pessoas = 0   
while True:
    comandos = input()
    if comandos == '1':
        quantidade_de_pessoas += comando_1()
        #ajuste_permanencia()
    if comandos == '2':
        comando_2()
        #ajuste_permanencia()
    if comandos == '3':
        comando_3()
        #ajuste_permanencia()
    if comandos == '4':
        comando_4()
        #ajuste_permanencia()
    if comandos == '-1':
        break
print(quantidade_de_pessoas)






