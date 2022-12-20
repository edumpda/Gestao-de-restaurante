#Construcao de sistema para gestao de pedidos de um restaurante!

import csv
mesas = dict()
areas_inseridas = []
cardapios = dict()
cardapios_inseridos = []
itens_totais = []
estoques = dict()
estoques_inseridos = []
pedidos_validos = dict()
cont = 0
valor = ''
comandos_existentes = ['+ atualizar mesas', '+ atualizar cardapio', '+ atualizar estoque', '+ relatorio mesas', '+ relatorio cardapio', '+ relatorio estoque', '+ fazer pedido', '+ relatorio pedidos', '+ fechar restaurante']
def atualizar_mesas_1(arq_mesas):
    
    arq = open(arq_mesas, 'r')
    for i in arq:
        i = i.strip().split(',')
        if i[1] not in areas_inseridas:
            areas_inseridas.append(i[1])
        mesas[i[0]] = i[1:]
    arq.close()

def atualizar_cardapio_2(arq_cardapio):
   arq = open(arq_cardapio, 'r')
   for i in arq:
       i = i.strip().split(',')
       cardapios[i[0]] = i[1:]
       itens_totais.append(i[0])
   arq.close()

def atualizar_estoque_3(arq_estoque):
    global estoques
    if arq_estoque in estoques_inseridos:
        for i in estoques:
            estoques = { **estoques, i: estoques[i] + estoques[i]}
    else:
        arq = open(arq_estoque, 'r')
        for i in arq:
            i = i.strip().split(',')
            estoques[i[0]] = int(i[1])
        arq.close()
        
def relatorio_mesas_4(arq_mesas):
    if mesas == {}:
        print('- restaurante sem mesas')
    else:
        for area in sorted(areas_inseridas):
            print(f'area:{area}')
            tem_mesa = False
            for mesa in sorted(mesas):
                if mesas[mesa][0] == area:
                    print(f'- mesa: {mesa}, status:{mesas[mesa][1]}')
                    tem_mesa = True
            if not tem_mesa:
                print('- area sem mesas')
                
        
def relatorio_cardapio_5(cardapios):
    if cardapios == {}:
        print('- cardapio vazio')
    else:
        for i in sorted(cardapios):
            listinha = {}
            item = i
            print(f'item: {item}')
            for j in sorted(cardapios[i]):
                ing = j
                if j not in listinha:
                    listinha[j]=cardapios[i].count(j)
                    print(f'-{j}: {listinha[j]}')
                    
def relatorio_estoque_6(estoques):
    contador = {}
    if estoques == {}:
        print('- estoque vazio')
    else:
        for i in sorted(estoques):
            print(f'{i}: {estoques[i]}')

def fazer_pedido_7(mesinha, item):
    global pedidos_validos
    if mesinha not in mesas:
        print(f'erro >> mesa {mesinha} inexistente')
        return
    if mesas[mesinha][1] == ' livre':
        print(f'erro >> mesa {mesinha} desocupada')
        return    
    if item not in itens_totais:
        print(f'erro >> item {item} nao existe no cardapio')
        return
    for i in cardapios[item]:
        if i.strip() not in estoques:
            print(f'erro >> ingredientes insuficientes para produzir o item {item}')
            break
    else:
        print(f'sucesso >> pedido realizado: item {item} para mesa {mesinha}')
        if mesinha in pedidos_validos:
            pedidos_validos.setdefault(mesinha, []).append(item)
        else:
            pedidos_validos[mesinha] = [item]
#diminuir ou zerar(se zerar, apague o ing) quantidade dos ings

def relatorio_pedidos_8(pedidos_validos):
    if pedidos_validos == {}:
        print('- nenhum pedido foi realizado')
    else:    
        for i in sorted(pedidos_validos):
            pd_mesa = i
            print(f'mesa: {pd_mesa}')
            for j in sorted(pedidos_validos[i]):
                pd_item = j
                print(f'- {pd_item}')

def fechar_restaurante_9(pedidos_validos):
    if pedidos_validos == {}:
        print('- historico vazio')
        print('=> restaurante fechado')
    else:
        for i in pedidos_validos:
            n = 1
            pd_mesa = i
            for j in pedidos_validos[i]:
                pd_item = j
                print(f'{n}. mesa {pd_mesa} pediu {pd_item}')
                n += 1
        print('=> restaurante fechado')

print('=> restaurante aberto')
while True:
    comandos = input()
    if comandos == '+ atualizar mesas':
        arq_mesas = input()
        atualizar_mesas_1(arq_mesas)
        
    if comandos == '+ atualizar cardapio':
        arq_cardapio = input()
        if arq_cardapio in cardapios_inseridos:
            cardapio = {}
        atualizar_cardapio_2(arq_cardapio)
        cardapios_inseridos.append(arq_cardapio)
        
    if comandos == '+ atualizar estoque':
         arq_estoque = input()
         atualizar_estoque_3(arq_estoque)
         estoques_inseridos.append(arq_estoque)
         
    if comandos == '+ relatorio mesas':
         relatorio_mesas_4(mesas)
         
    if comandos == '+ relatorio cardapio':
         relatorio_cardapio_5(cardapios)
         
    if comandos == '+ relatorio estoque':
         relatorio_estoque_6(estoques)
         
    if comandos == '+ fazer pedido':
         pedidos = input().split()
         mesinha = pedidos[0].strip(',')
         item = ' '.join(pedidos[1:])
         fazer_pedido_7(mesinha, item)
    
    if comandos == '+ relatorio pedidos':
         relatorio_pedidos_8(pedidos_validos)
    
    if comandos == '+ fechar restaurante':
         fechar_restaurante_9(pedidos_validos)
         break
    if comandos not in comandos_existentes:
        print('erro >> comando inexistente')

