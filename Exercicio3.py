def isFloat(valor, msg): #METODO PARA VALIDAÇÃO SE O VALOR É FLOAT
    try:
        if ((float(valor))):
            return True
    except:
        print(msg)
        return False

def dimensoesObjeto(): #METODO PARA CALCULAR A DIMENSÃO DO OBJETO
    _volume = 0
    _valor = 0
    while True: #INICIO DO LOOP
        _alturacm = input('Entre com a altura do pacote(cm):') #INFORMANDO A ALTURA EM CM
        if not isFloat(_alturacm, 'Você digitou um valor não numérico\nPor favor entre com as dimensões desejadas novamente.'): #VALIDANDO SE O VALOR INFORMADO NÃO É FLOAT
            continue

        _larguracm = input('Entre com a largura do pacote(cm):') #INFORMANDO A LARGURA EM CM
        if not isFloat(_larguracm, 'Você digitou um valor não numérico\nPor favor entre com as dimensões desejadas novamente.'):#VALIDANDO SE O VALOR INFORMADO NÃO É FLOAT
            continue

        _comprimentocm = input('Entre com o comprimento do pacote(cm):') #INFORMANDO 0 COMPRIMENTO  EM CM
        if not isFloat(_comprimentocm, 'Você digitou um valor não numérico\nPor favor entre com as dimensões desejadas novamente.'):#VALIDANDO SE O VALOR INFORMADO NÃO É FLOAT
            continue

        _volume = float(_alturacm)*float(_larguracm)*float(_comprimentocm)  # Volume (em cm) da caixa p/a objeto (altura*largura*comprimento)

        if (_volume <= 1000): #VALIDANDO SE O VOLUME É MENOR QUE 1000
            _valor = 10
        elif(_volume >= 1000 and _volume < 10000): #VALIDANDO SE O VOLUME É MAIOR OU IGUAL A 1000 E MENOR QUE 10000
            _valor = 20
        elif (_volume >= 10000 and _volume < 30000): #VALIDANDO SE O VOLUME É MAIOR OU IGUAL A 10000 E MENOR QUE 30000
            _valor = 30
        elif (_volume >= 30000 and _volume < 100000): #VALIDANDO SE O VOLUME É MAIOR OU IGUAL A 30000 E MENOR QUE 100000
            _valor = 50
        else: #VALIDANDO SE O VOLUME É MAIOR OU IGUAL A 100000
            print('O volume do objeto é (em cm³) : {}\nNão aceitamos objetos com dimensões tão grandes.'.format(_volume))
            continue
        break
    return _valor #RETORNANDO O VALOR DA DIMENSÃO

def pesoObjeto(): #METODO PARA CALCULAR O MULTIPLICADOR DO PESO DO OBJETO
    _peso = 0
    _multiplicador = 0
    while True:#INICIO DO LOOP
        _peso = input('Qual o peso do objeto (kg):')#INFORMANDO O PESO DO OBJETO EM KG
        if not isFloat(_peso,'Você digitou um valor não numérico\nPor favor entre com o peso desejado novamente.'):#VALIDANDO SE O VALOR INFORMADO NÃO É FLOAT
            continue

        _peso = float(_peso) #CONVERTENDO O PESO EM FLOAT
        if (_peso < 0.1): #VALIDANDO SE O PESO É MENOR QUE 0.1
            _multiplicador = 1
        elif (_peso >= 0.1 and _peso < 1):#VALIDANDO SE O PESO É MAIOR OU IGUAL A 0.1 E MENOR QUE 1
            _multiplicador = 1.5
        elif (_peso >= 1 and _peso < 10): #VALIDANDO SE O PESO É MAIOR OU IGUAL A 1 E MENOR QUE 10
            _multiplicador = 2
        elif (_peso >= 10 and _peso < 30): #VALIDANDO SE O PESO É MAIOR OU IGUAL A 10 E MENOR QUE 30
            _multiplicador = 3
        else: #VALIDANDO SE OPESO É MAIOR OU IGUAL A 30
            print('Não aceitamos objetos tão pesados.\nPor favor entre com o peso desejado novamente.')
            continue
        break
    return _multiplicador #RETORNANDO O MULTIPLICADOR PARA O PESO

def rotaObjeto(): #METODO PARA OBTER O MULTIPLICADOR PARA A ROTA DO OBJERO
    while True: #INICIO DO LOOP
        _rotas = 'Selecione uma rota:\n' #INICIO NA MONTAGEM DO MENU
        _rotas += 'RS - De Rio de Janeiro até São Paulo\n'
        _rotas += 'SR - De São Paulo até Rio de Janeiro\n'
        _rotas += 'BS - De Brasília até São Paulo\n'
        _rotas += 'SB - De São Paulo até Brasília\n'
        _rotas += 'BR - De Brasília até Rio de Janeiro\n'
        _rotas += 'RB - Rio de Janeiro até Brasília\n'

        _selecao = input(_rotas)  #IMPRIMINDO O MENU E OBTENDO O VALOR DA DIGITADO PARA ROTA

        if (_selecao.upper() == 'RS'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'RS'
            _multiplicador = 1
        elif (_selecao.upper() == 'SR'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'SR'
            _multiplicador = 1
        elif (_selecao.upper() == 'BS'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'BS'
            _multiplicador = 1.2
        elif (_selecao.upper() == 'SB'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'SB'
            _multiplicador = 1.2
        elif (_selecao.upper() == 'BR'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'BR'
            _multiplicador = 1.5
        elif (_selecao.upper() == 'RB'): #VALIDANDO COM UPPER O VALOR DIGITADO E COMPARANDO COM 'RB'
            _multiplicador = 1.5
        else: #VALIDANDO SE O VALOR DIGITADO NÃO ESTÁ NA LISTA ACIMA
            print('Você digitou uma rota que não existe.\nPor favor entre com a rota desejada novamente.')
            continue
        break

    return float(_multiplicador) #RETORNANDO O MULTIPLICADOR DA ROTA

print(' ')
_4499559 = 'BEM VINDO A EMPRESA LOGÍSTICA DE MARCELO EDUARDO ABUCHAIN : RU 4499559 ' # IDENTIFICAÇÃO PESSOAL
print('#'*3 + _4499559 + '#'*3) # PRINT TITULO
print(' ')

_dimensao = dimensoesObjeto() #OBTENDO A DIMENSAO DO OBJETO
_peso = pesoObjeto() # OBTENDO O MULTIPLICADOR DE PESO DO OBJETO
_rota = rotaObjeto() # OBTENDO O MULTIPLICADOR DA ROTA DO OBJETO

_impressaoConsole = 'Total a pagar(R$): {:.2f} ( dimensões: {} * peso: {} * rota: {})' #MENSAGEM DE IMPRESSÃO FINAL
_valorPagar = _dimensao*_peso*_rota #CALCULO PARA VALOR TOTAL A PAGAR

print(_impressaoConsole.format(_valorPagar,_dimensao,_peso,_rota)) #IMPRIMINDO O RESULTADO FINAL NA TELA




