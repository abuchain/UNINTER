estoque = {}  # Cria um dicionário vazio chamado 'estoque' para armazenar as peças


def cadastra_Peca():  # Define a função 'cadastrarPeca' para cadastrar uma nova peça no estoque
    novo_codigo = 0
    ultimo_codigo = 0
    for codigo in estoque:  # Percorre as chaves (códigos) do dicionário 'estoque'
        ultimo_codigo = int(
            codigo)  # Atualiza o valor da variável 'ultimo_codigo' com o último código existente no estoque
    novo_codigo = ultimo_codigo + 1  # Gera um novo código único para a peça

    while True:  # Loop infinito até que o cadastro seja concluído
        codigo = str(novo_codigo)
        print('Você Selecionou a Opção de Cadastrar Peça')
        print('Código da Peça:', codigo)
        nome = input('Qual o nome da peça: ')
        fabricante = input('Qual o fabricante da peça: ')
        valor = input('Qual o valor da peça: ')

        peca = {'codigo': codigo, 'nome': nome, 'fabricante': fabricante,
                'valor': valor}  # Cria um dicionário com as informações da peça
        estoque[codigo] = peca  # Adiciona a peça ao dicionário 'estoque' usando o código como chave
        print("Peça cadastrada com sucesso!")
        break  # Sai do loop while


def exclui_Peca():  # Define a função 'excluirPeca' para remover uma peça do estoque
    print("Você selecionou a opção de Remover Peça.")
    codigo = input("Digite o código da peça que deseja excluir: ")
    if codigo in estoque:  # Verifica se o código existe no estoque
        del estoque[codigo]  # Remove a peça com o código correspondente do dicionário 'estoque'
        print("Peça removida do cadastro.")
    else:
        print("Peça não encontrada no cadastro.")


def consulta_Pecas():  # Define a função 'consultarPecas' para consultar as peças do estoque
    while True:  # Loop infinito até que uma opção válida seja selecionada
        print("Você selecionou a opção de Consultar Peças.")
        opcao = input(
            "Escolha a opção desejada:\n1) Consultar todas as peças\n2) Consultar peça por código\n3) Consultar peça por fabricante\n4) Voltar\n")  # Solicita a opção desejada ao usuário
        if opcao == '1':  # Se a opção for 1, consulta todas as peças
            consulta_Todas_Pecas()
        elif opcao == '2':  # Se a opção for 2, consulta uma peça por código
            codigo = input('Informe o código da peça: ')
            consulta_Por_Codigo(codigo)
        elif opcao == '3':  # Se a opção for 3, consulta peças por fabricante
            fabricante = input('Informe o nome do fabricante da peça: ')
            consultar_Por_Fabricante(fabricante)
        elif opcao == '4':  # Se a opção for 4, retorna ao menu principal
            break
        else:
            print("Opção inválida. Digite novamente.")


def consulta_Todas_Pecas():  # Define a função 'consultarTodasPecas' para exibir todas as peças do estoque
    if estoque:  # Verifica se o estoque não está vazio
        for codigo, peca in estoque.items():  # Percorre todas as peças no estoque
            print("Código:", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    else:
        print("O cadastro está vazio.")


def consulta_Por_Codigo(
        codigo):  # Define a função 'consultarPecaPorCodigo' para consultar uma peça específica por código
    encontrada = False
    for codigo_peca, peca in estoque.items():  # Percorre todas as peças no estoque
        if codigo_peca.lower() == codigo.lower():  # Verifica se o código da peça corresponde ao código informado (ignorando maiúsculas/minúsculas)
            encontrada = True
            print("Código:", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    if not encontrada:
        print("Nenhuma peça encontrada para esse código.")


def consultar_Por_Fabricante(
        fabricante):  # Define a função 'consultarPecaPorFabricante' para consultar peças por fabricante
    encontrada = False
    for codigo, peca in estoque.items():  # Percorre todas as peças no estoque
        if peca[
            'fabricante'].lower() == fabricante.lower():  # Verifica se o fabricante da peça corresponde ao fabricante informado (ignorando maiúsculas/minúsculas)
            encontrada = True
            print("Código:", peca['codigo'])
            print("Nome:", peca['nome'])
            print("Fabricante:", peca['fabricante'])
            print("Valor:", peca['valor'])
            print("--------------------")
    if not encontrada:
        print("Nenhuma peça encontrada para esse fabricante.")


# Bloco principal do programa
print('#' * 3 + 'BEM VINDO AO CONTROLE DE ESTOQUE DE SAMUEL LUIZ ABUCHAIN: RU ????????' + '#' * 3)

while True:  # Loop infinito para exibir o menu principal e executar as opções selecionadas
    print("1) Cadastrar peça\n2) Consultar peças\n3) Remover peça\n4) Encerrar programa")
    opcao = input(">> ")
    if opcao == '1':  # Se a opção for 1, cadastra uma nova peça
        cadastra_Peca()
    elif opcao == '2':  # Se a opção for 2, consulta as peças
        consulta_Pecas()
    elif opcao == '3':  # Se a opção for 3, remove uma peça
        exclui_Peca()
    elif opcao == '4':  # Se a opção for 4, encerra o programa
        print("Você encerrou o programa.")
        break
    else:
        print("Opção inválida. Digite novamente.")
