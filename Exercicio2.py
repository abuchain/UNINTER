
print(' ')
_4499559 = ' LANCHONETE DO MARCELO EDUARDO ABUCHAIN : RU 4499559 ' # IDENTIFICAÇÃO PESSOAL
print('#'*3 + _4499559 + '#'*3) # PRINT TITULO
_menu = '########################### MENU ##########################\n' #CRIAÇÃO DO MENU
_menu += '---------------------------------------------------\n'
_menu += '|  Código |  Descrição				 |  Valor(R$) |\n'
_menu += '|   100	  |	 Cachorro-Quente		 |	9,00      |\n'
_menu += '|   101	  |	 Cachorro-Quente Duplo	 |	11,00     |\n'
_menu += '|   102	  |	 X-Egg					 |	12,00     |\n'
_menu += '|   103	  |	 X-Salada				 |	13,00     |\n'
_menu += '|   104	  |  X-Bacon				 |	14,00     |\n'
_menu += '|   105	  |	 X-Tudo					 |	17,00     |\n'
_menu += '|   200	  |	 Refrigerante Lata		 |	5,00      |\n'
_menu += '|   201	  |	 Chá Gelado				 |  4,00      |\n'
_menu += '---------------------------------------------------\n'

print(_menu) #EXIBINDO O MENU

_strContinue = 'Deseja pedir mais alguma coisa?\n1 - SIM\n0 - NÃO\n' #TEXTO DA MENSAGEM PARA CONTINUAÇÃO DO PEDIDO
_pedidoTotal = 0.00 #INICIO DO VALOR TOTAL DO PEDIDO

while True:
    _produto = '' #INICIO DA VARIAVEL PRODUTO
    _valorProduto = 0.00 #INICIO DA VARIAVEL VALOR DO PRODUTO
    _msg = 'Você pediu um {} no valor de R$ {:.2f}' #MENSAGEM  A SER IMPRESSA

    _codProduto = int(input('Entre com o código desejado:'))  # ENTRADA DO CÓDIGO DO PRODUTO

    if(_codProduto == 100): #INCIO DAS VERIFICAÇÕES DOS CODIGOS DOS PRODUTOS
        _produto = 'Cachorro-Quente'
        _valorProduto = 9.00
    elif (_codProduto == 101):
        _produto = 'Cachorro - Quente Duplo'
        _valorProduto = 11.00
    elif (_codProduto == 102):
        _produto = 'X-Egg'
        _valorProduto = 12.00
    elif (_codProduto == 103):
        _produto = 'X-Salada'
        _valorProduto = 13.00
    elif (_codProduto == 104):
        _produto = 'X-Bacon'
        _valorProduto = 14.00
    elif (_codProduto == 105):
        _produto = 'X-Tudo'
        _valorProduto = 17.00
    elif (_codProduto == 200):
        _produto = 'Refrigerante Lata'
        _valorProduto = 5.00
    elif (_codProduto == 201):
        _produto = 'Chá Gelado'
        _valorProduto = 4.00
    else: #VALIDAÇÃO PARA OPÇÃO INVÁLIDA
        input('Opção Inválida\n')
        if (int(input(_strContinue)) == 1):
            continue
        else:
            break

    _pedidoTotal += _valorProduto #SOMANDO VALOR TOTAL DO PEDIDO

    print(_msg.format(_produto, _valorProduto))

    if(int(input(_strContinue)) == 1):
        continue
    else:
        break

print('#'*10 + ' CUPOM DE VALIDAÇÃO DA VENDA ' + '#'*11)
print('O Total a ser pago é R$ {:.2f}'.format(_pedidoTotal)) #IMPRESSÃO DO TOTAL DO PEDIDO