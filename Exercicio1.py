_4499559 = ' LOJA DO MARCELO EDUARDO ABUCHAIN : RU 4499559 ' # IDENTIFICAÇÃO PESSOAL

_separador = '#'*60 # CRIANDO LINHA DE SEPARADOR

print(_separador)
print('#'*7 + _4499559 + '#'*6) # PRINT TITULO
print('#'*21 + '   BEM VINDO !!!  ' + '#'*21) # PRINT BOAS VINDAS
print(_separador)
print(' ')

_desconto = 0 # PRINT INICIANDO O DESCONTO COMO 0
_valor = float(input('Digite o valor do Produto :')) # ENTRADA DO VALOR DO PRODUTO
_qtde = int(input('Digite a quantidade do Produto :')) # ENTRADA DA QUANTIDADE DO PRODUTO

_valorTotal = _valor * _qtde # VALOR TOTAL DA VENDA SEM DESCONTO

if(_qtde >=10): # VERIFICAÇÃO SE DEVE TER DESCONTO OU NÃO
    if(_qtde >= 10 and _qtde < 100): # VERIFICAÇÃO SE DESCONTO DEVE SER 5%
        _desconto = 0.05
    elif(_qtde >= 100 and _qtde < 1000): # VERIFICAÇÃO SE DESCONTO DEVE SER 10%
        _desconto = 0.10
    else: # VERIFICAÇÃO SE DESCONTO DEVE SER 15%
        _desconto = 0.15

_valorDesconto = 0.00 # INICIANDO O VALOR DE DESCONTO COM 0.00

if(_desconto != 0): # VERIFICAÇÃO SE DEVE SER APLICADO DESCONTO OU NÃO
    _valorDesconto = _valorTotal * _desconto

print(' ')
print(_separador)
print('#'*16 + ' CUPOM DE VALIDAÇÃO DA VENDA ' + '#'*15)
print(_separador)
print(' ')
print('Valor Total da Compra : R$ {:.2f}'.format(_valorTotal)) # IMPRIMINDO VALOR TOTAL DA COMPRA SEM DESCONTO
print('Percentual de Desconto Aplicado : {} %'.format(_desconto * 100)) # IMPRIMINDO PERCENTUAL DE DESCONTO APLICADO
print('Valor de Desconto : R$ {:.2f}'.format(_valorDesconto)) # IMPRIMINDO O VALOR DO DESCONTO
print('Valor Total a Pagar : R$ {:.2f}'.format(_valorTotal-_valorDesconto)) # IMPRIMINDO VALOR TOTAL DA COMPRA COM DESCONTO

