listaPecas = {}  #CRIAÇÃO DO DICIONARIO VAZIO PARA ARMAZENAR OS DADOS

def menu(): #MÉTODO PARA CRIAÇÃO DO MENU PRINCIPAL
    _menu = 'Escolha a opção desejada:\n'
    _menu += '1.	Cadastrar Peça\n'
    _menu += '2.	Consultar Peça\n'
    _menu += '3.	Remover Peça\n'
    _menu += '4.	Sair\n'
    return _menu

def submenu(): #MÉTODO PARA CRIAÇÃO DO MENU SECUNDÁRIO
    _menuConsulta = '1)    Consultar Todas as Peças\n'
    _menuConsulta += '2)    Consulta Peças por Código\n'
    _menuConsulta += '3)    Consulta Peças por Fabricante\n'
    _menuConsulta += '4)    Retornar\n'
    return _menuConsulta

def proximoCodigoPeca(): #METODO PARA DEVOLVER PROXIMO CÓDIGO DE PEÇA
    if listaPecas: #VALIDANDO SE EXISTEM ITENS NA LISTA
        for codigo, peca in listaPecas.items(): #PERCORRENDO OS ITENS DA LISTA
            _novoCodigo = int(codigo) #OBTENDO O CODIGO
        _novoCodigo += 1 #SOMANDO 1 AO ULTIMO CODIGO OBTIDO
        return _novoCodigo #RETORNANDO O VALOR
    else: #CASO A LISTA NÃO TENHA VALORES
        return 1 #RETORNANDO CODIGO 1

def cadastrarPeca(indice): #METODO PARA CADASTRAR PEÇAS
    #OTENDO OS VALORS PARA CRIAR A PEÇA
    _codigo = str(indice)
    print('Você Selecionou a Opção de Cadastrar Peça')
    print('Código da Peça: {}'.format(_codigo))
    _nome = input('Qual o nome da peça:')
    _fabricante = input('Qual o fabricante da peça:')
    _valor = input('Qual o valor da peça:')

    peca = {'codigo': _codigo, 'nome': _nome, 'fabricante': _fabricante, 'valor': _valor} #CRIAÇÃO DE UM DICIONARIO COM OS VALORES COLETADOS

    listaPecas[str(indice)] = peca #ADICIONANDO O DICIONARIO AO CADASTRO, USANDO O CAMPO INDICE COMO CHAVE
    print("Peça cadastrada com sucesso!")

def excluirPeca(): #METODO PARA EXCLUIR UMA PEÇA
    codigo = input("Digite o codigo da peça que deseja excluir: ")  # OBTENDO O VALOR INFORMADO PELO USUÁRIO
    #VERIFICANDO SE O CODIGO EXISTE NO CADASTRO
    if codigo in listaPecas:
        del listaPecas[codigo]  #REMOVENDO O DICIONARIO ENCONTRADO DA PEÇA DO CADASTRO
        print("Peça removida do cadastro.")
    else: #CASO NÃO ENCONTRE A PEÇA PELO CÓDIGO
        print("Peça não encontrada no cadastro.")

def consultarPecas():
    while True:  # INICIO DO LOOP PARA MENU SECUNDÁRIO
        print(submenu())  # IMPRIMINDO O MENU SECUNDARIO
        opcao2 = input("Digite a opção de consulta que vai ser executada: ")  # OBTENDO O VALOR INFORMADO PELO USUÁRIO
        if (opcao2 == '1'):
            consultarTodasPecas()  # ACIONANDO O METODO PARA EXIBIR TODAS AS PEÇAS CDASTRADAS
        elif (opcao2 == '2'):
            codigo = input('Informe o código da peça:')  # OBTENDO O VALOR INFORMADO PELO USUÁRIO
            consultarPecaPorCodigo(codigo)  # ACIONANDO O METODO PARA EXIBIR A PEÇA CADASTRADA PARA O CODIGO INFORMADO
        elif (opcao2 == '3'):
            fabricante = input('Informe o nome do fabricante da peça:')  # OBTENDO O VALOR INFORMADO PELO USUÁRIO
            consultarPecaPorFabricante(
                fabricante)  # ACIONANDO O METODO PARA EXIBIR AS PEÇAS CADASTRADAS PARA O FABRICANTE INFORMADO
        elif (opcao2 == '4'):
            break  # RETORNAR AO MENU ANTERIOR
        else:  # VALIDANDO UMA OPÇÃO QUE NÃO EXISTE
            print("Opção inválida. Digite novamente.")

def consultarTodasPecas():  #METODO PARA EXIBIR TODOS OS CADASTROS DE PEÇAS
    if listaPecas:#VALIDANDO SE EXISTEM ITENS NA LISTA
        for indice, peca in listaPecas.items(): #PERCORRENDO OS ITENS DO DICIONARIO E EXIBINDO OS VALORES
            print("Código:", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    else: #CASO NÃO ENCONTRE NENHUM ITEM NO DICIONARIO
        print("O cadastro está vazio.")

def consultarPecaPorCodigo(codigo): #METODO PARA EXIBIR OS DADOS DE UMA PEÇA POR CÓDIGO
    encontradas = False #INICIANDO A VARIAVEL DE VALIDAÇÃO
    for indice, peca in listaPecas.items():#PERCORRENDO OS ITENS DO DICIONARIO
        if peca['codigo'].lower() == codigo.lower(): #VERIFICANDO SE O CODIGO INFORMADO ESTA NO LOOP
            encontradas = True #ALTERANDO O ESTADO DA VARIAVEL DE VALIDAÇÃO
            #IMPRIMINDO OS VALORES DO CODIGO ENCONTRADO
            print("Código", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    if not encontradas: #VALIDANDO O ESTADO DA VARIAVEL DE VALIDAÇÃO = FALSE
        print("Nenhuma peça encontrada para esse código.")

def consultarPecaPorFabricante(fabricante): #METODO PARA EXIBIR OS DADOS DE PEÇAS POR FABRICANTE
    encontradas = False #INICIANDO A VARIAVEL DE VALIDAÇÃO
    for indice, peca in listaPecas.items():#PERCORRENDO OS ITENS DO DICIONARIO
        if peca['fabricante'].lower() == fabricante.lower(): #VERIFICANDO SE O FABRICANTE INFORMADO ESTA NO LOOP
            encontradas = True #ALTERANDO O ESTADO DA VARIAVEL DE VALIDAÇÃO
            # IMPRIMINDO OS VALORES DO FABRICANTE ENCONTRADO
            print("Código", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    if not encontradas: #VALIDANDO O ESTADO DA VARIAVEL DE VALIDAÇÃO = FALSE
        print("Nenhuma peça encontrada para esse fornecedor.")

#PROGRAMA PRINCIPAL
_empresa = 'BEM VINDO AO CONTROLE DE ESTOQUE DA BICICLETARIA DE MARCELO EDUARDO ABUCHAIN : RU 4499559 ' # IDENTIFICAÇÃO PESSOAL
print('#'*3 + _empresa + '#'*3) # PRINT TITULO

while True: #INICIO DO LOOP PARA O MENU
    #print(menu()) #IMPRIMINDO O MENU PRINCIPAL
    #opcao = input("Digite uma opção: ") #OBTENDO O VALOR INFORMADO PELO USUÁRIO
    opcao = input(menu()+'>>')

    if opcao == '1':
        cadastrarPeca(proximoCodigoPeca()) #ACIONANDO METODO DE CADASTRAR PEÇA E PASSANDO O CODIGO PARA CADASTRO DA PRÓXIMA PEÇA
    elif opcao == '2':
        consultarPecas() #ACIONANDO METODO DE CONSULTAR PEÇAS
    elif opcao == '3':
        excluirPeca() #ACIONANDO O METODO PARA EXCLUIR UMA PEÇA DO CADASTRO
    elif opcao == '4':
        print("Você encerrou o programa.")
        break #ENCERRANDO O PROGRAMA
    else: #VALIDANDO UMA OPÇÃO QUE NÃO EXISTE
        print("Opção inválida. Digite novamente.")
