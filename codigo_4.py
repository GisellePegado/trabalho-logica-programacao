lista_contatos = []
id_global = 5052104

# Função genérica que recebe o títuto do menu e as alternativas e imprime na tela seguindo um padrão
def imprimir_menu(titulo, alternativas):
    n_caracteres = len(titulo)
    n_hifens = int((70-n_caracteres)/2)
    print('-' * 72)
    print('-' * n_hifens, titulo, '-' * n_hifens)
    n_alternativas = len(alternativas)
    if n_alternativas > 1:
        print('Escolha a opção desejada:')
        for i in range(n_alternativas):
            print(f'{i+1}. {alternativas[i]}')
        while True:
            try:
                alternativa_escolhida = int(input('>> '))
                if alternativa_escolhida < 1 or alternativa_escolhida > n_alternativas:
                    raise ValueError
                else:
                    return alternativa_escolhida
            except ValueError:
                print('Opção inválida')

# Função simples para imprimir uma linha usada como separador de inforamções
def imprimir_separador():
    print('-' * 20)

# Função que cadastra um contato recebendo um id como entrada e perguntando as outras informações que precisam ser adicionadas
def cadastrar_contato(id):
    imprimir_menu('MENU CADASTRAR CONTATO', [])
    print('Id do Contato:', id)
    contato = {}
    contato['Id'] = id
    contato['Nome'] = input('Por favor entre com o nome do Contato: ')
    contato['Atividade'] = input('Por favor entre com a Atividade do contato: ')
    contato['Telefone'] = input('Por favor entre com o telefone do contato: ')
    lista_contatos.append(contato.copy())

# Função auxiliar (e genérica) que recebe o tipo do parâmetro e o parâmetro que deve ser buscado na lista de contatos
def consultar_por_parametro(tipo, parametro):
    imprimir_separador()
    for contato in lista_contatos:
        if parametro == contato[tipo]:
            print(f'Id: {contato['Id']}')
            print(f'Nome: {contato['Nome']}')
            print(f'Atividade: {contato['Atividade']}')
            print(f'Telefone: {contato['Telefone']}\n')
    imprimir_separador()

# Função auxiliar que pergunta o id do contato e traz todas as informações do mesmo
def consultar_por_id():
    while True:
        try:
            id = int(input('Digite o Id do contato: '))
            if id in [contato['Id'] for contato in lista_contatos]:
                break
            else:
                raise ValueError
        except ValueError:
            print('Id inválido')
    consultar_por_parametro('Id', id)

# Função auxiliar que pergunta a atividade do(s) contato(s) e traz todas as informações do(s) mesmo(s)
def consultar_por_atividade():
    atividade = input('Digite a Atividade do(s) contato(s): ')
    consultar_por_parametro('Atividade', atividade)

# Função principal que exibe o menu de consulta de contatos e exibe os mesmos de acordo com a alternativa escolhida
def consultar_contatos():
    if len(lista_contatos) == 0:
        imprimir_separador()
        print('A lista ainda não tem contatos cadastrados')
    else:
        while True:
            menu_consultar = imprimir_menu('MENU CONSULTAR CONTATOS', ['Consultar Todos', 'Consultar por Id', 'Consultar por Atividade', 'Retornar ao menu'])
            if menu_consultar == 1:
                imprimir_separador()
                for contato in lista_contatos:
                    print(f'Id: {contato['Id']}')
                    print(f'Nome: {contato['Nome']}')
                    print(f'Atividade: {contato['Atividade']}')
                    print(f'Telefone: {contato['Telefone']}\n')
                imprimir_separador()
            elif menu_consultar == 2:
                consultar_por_id()
            elif menu_consultar == 3:
                consultar_por_atividade()
            elif menu_consultar == 4:
                return
            else:
                print('Opção inválida')

# Função que pergunta o id do contato e remove o mesmo
def remover_contato():
    if len(lista_contatos) == 0:
        imprimir_separador()
        print('A lista ainda não tem contatos cadastrados')
    else:
        while True:
            imprimir_menu('MENU REMOVER CONTATO', [])
            try:
                id = int(input('Digite o Id do contato: '))
                contato_encontrado = False
                for contato in lista_contatos:
                    if id == contato['Id']:
                        lista_contatos.remove(contato)
                        print('Contato removido com sucesso!')
                        contato_encontrado = True
                        break
                if contato_encontrado:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Id inválido')

# Programa principal
print('Bem vindo à Lista de Contatos da Giselle Maria Ferreira Pegado da Silva!')
while True:
    menu_principal = imprimir_menu('MENU PRINCIPAL', ['Cadastrar Contato', 'Consultar Contato(s)', 'Remover Contato', 'Encerrar Programa'])
    if menu_principal == 1:
        id_global += 1
        cadastrar_contato(id_global)
    elif menu_principal == 2:
        consultar_contatos()
    elif menu_principal == 3:
        remover_contato()
    elif menu_principal == 4:
        break
    else:
        print('Opção inválida')