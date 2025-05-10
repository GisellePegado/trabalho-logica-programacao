# Função auxiliar que pergunta o tipo de madeira desejada e retorna a resposta do usuário
def pergunta_tipo():
    print('Entre com o Tipo de Madeira desejada:')
    print('PIN - Tora de Pinho')
    print('PER - Tora de Peroba')
    print('MOG - Tora de Mogno')
    print('IPE - Tora de Ipê')
    print('IMB - Tora de Imbuia')
    tipoMadeira = input('>>>')
    return tipoMadeira

# Função principal que pergunta o tipo de madeira desejada e retorna o valor do m³ correspondente
def escolha_tipo():
    tipoMadeira = pergunta_tipo()
    while tipoMadeira != 'PIN' and tipoMadeira != 'PER' and tipoMadeira != 'MOG' and tipoMadeira != 'IPE' and tipoMadeira != 'IMB':
        print('Escolha inválida, entre com o modelo novamento\n')
        tipoMadeira = pergunta_tipo()
    if tipoMadeira == 'PIN':
        return 150.40
    elif tipoMadeira == 'PER':
        return 170.20
    elif tipoMadeira == 'MOG':
        return 190.90
    elif tipoMadeira == 'IPE':
        return 210.10
    else:
        return 220.70

# Função que pergunta a quantidade de toras e retorna esse valor e o desconto correspondente
def qtd_toras():
    while True:
        try:
            qtdToras = int(input('Entre com a quantidade de toras (m³): '))
            if qtdToras <= 2000:
                break
            else:
                print('Não aceitamos pedidos com essa quantidade de toras.\nPor favor, entre com a quantidade novamente.\n')
        except ValueError:
            print('Resposta inválida.\nPor favor, entre com a quantidade novamente.\n')

    if qtdToras < 100:
        desconto = 0
    elif qtdToras >= 100 and qtdToras < 500:
        desconto = 4/100
    elif qtdToras >= 500 and qtdToras < 1000:
        desconto = 9/100
    else:
        desconto = 16/100
    return qtdToras, desconto
    
# Função auxiliar que pergunta o tipo de transporte e retorna a resposta
def pergunta_transporte():
    print('\nEscolha o tipo de Transporte:')
    print('1 - Transporte Rodoviário - R$ 1000.00')
    print('2 - Transporte Ferroviário - R$ 2000.00')
    print('3 - Transporte Hidroviário - R$ 2500.00')
    tipoTransporte = int(input('>>>'))
    return tipoTransporte

# Função principal que pergunta o tipo de transporte e retorna o custo correspondente
def transporte():
    tipoTransporte = pergunta_transporte()
    while tipoTransporte != 1 and tipoTransporte != 2 and tipoTransporte != 3:
        print('Resposta inválida. Tente novamente\n')
        tipoTransporte = pergunta_transporte()
    if tipoTransporte == 1:
        return 1000
    elif tipoTransporte == 2:
        return 2000
    else:
        return 2500

# Programa principal
print('Bem vindo à Madeireira da Lenhadora Giselle Maria Ferreira Pegado da Silva\n')
tipoMadeira = escolha_tipo() # Chamada da função que retorna o valor do m³ do tipo de madeira escolhido
qtdToras, desconto = qtd_toras() # Chamada da função que retorna a quantidade de toras e o desconto correspondente
valorTransporte = transporte() # Chamada da função que retorna o valor do tipo de transporte escolhido

total = ((tipoMadeira*qtdToras)*(1-desconto)) + valorTransporte # Função que calcula o custo total

print(f'Total: R$ {total:.2f}')
