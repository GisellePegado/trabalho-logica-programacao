# Função que calcula o valor da pizza de acordo com o sabor e tamanho escolhidos
def calcular_valor (sabor, tamanho):
    if sabor == 'PS': # Se a pizza for salgada
        if tamanho == 'P':
            return 30
        elif tamanho == 'M':
            return 45
        else:
            return 60
    else: # Se a pizza for doce
        if tamanho == 'P':
            return 34
        elif tamanho == 'M':
            return 48
        else:
            return 66

# Função que imprime as informações do pedido (sabor, tamanho e valor)
def imprimir_pedido (sabor, tamanho, valor):
    if sabor == 'PS':
        nomeSabor = 'Pizza Salgada'
    else:
        nomeSabor = 'Pizza Doce'
    print (f'Você pediu uma {nomeSabor} no tamanho {tamanho}: R$ {valor:.2f}\n')

# Programa principal
print('Bem vindo à Pizzaria da Giselle maria Ferreira Pegado da Silva!')
print('-' * 26, 'Cardápio', '-' * 26)
print('-' * 62)
print('-' * 5, '| Tamanho | Pizza Salgada (PS) | Pizza Doce (PD) |', '-' * 5 )
print('-' * 5, '|    P    |      R$ 30.00      |     R$ 34.00    |', '-' * 5 )
print('-' * 5, '|    M    |      R$ 45.00      |     R$ 48.00    |', '-' * 5 )
print('-' * 5, '|    G    |      R$ 60.00      |     R$ 66.00    |', '-' * 5 )
print('-' * 62)

acumulador = 0 # Variável que guarda o valor total do pedido
algoMais = True # Variável que guarda a informação de se o usuário deseja algo mais
# A variável algoMais foi definida como True para iniciar o laço do while

while algoMais == True: # Enquanto o cliente desejar algo mais, repita
    sabor = input ('Entre com o sabor desejado (PS/PD): ')
    while sabor != 'PS' and sabor != 'PD': # Trata o erro ao digitar o sabor da pizza
        print('Sabor inválido. Tente novamente\n')
        sabor = input ('Entre com o sabor desejado (PS/PD): ')

    tamanho = input ('Entre com o tamanho desejado (P/M/G): ')
    while tamanho != 'P' and tamanho != 'M' and tamanho != 'G': # Trata o erro ao digitar o tamanho da pizza
        print('Tamanho inválido. Tente novamente\n')
        tamanho = input ('Entre com o tamanho desejado (P/M/G): ')

    valor = calcular_valor(sabor, tamanho) # Chama a função que calcula o valor da pizza
    acumulador += valor # Incrementa o valor total do pedido
    imprimir_pedido (sabor, tamanho, valor) # Chama a função que imprime as informações do pedido

    desejaAlgoMais = input ('Deseja mais alguma coisa? (S/N): ')
    while desejaAlgoMais != 'S' and desejaAlgoMais != 'N':
        print('Resposta inválida. Tente novamente\n') # Trata o erro ao digitar um valor diferente de S ou N
        desejaAlgoMais = input ('Deseja mais alguma coisa? (S/N): ')
    
    if desejaAlgoMais == 'N':
        algoMais = False # Atribui à variável algoMais valor de falso para sair do laço do while
        print(f'\nO valor total a se pago: R$ {acumulador:.2f}')

