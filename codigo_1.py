# Função para calcular o valor mensal
def calcular_valor_mensal (valorBase, porcetagem):
    return valorBase*porcetagem

# Função para calcular porcetagem de acordo com a idade
def calcular_porcentagem (idade):
    if idade >= 0 and idade < 19:
        return 100 / 100
    elif idade >= 19 and idade < 29:
        return 150 / 100
    elif idade >= 29 and idade < 39:
        return 225 / 100
    elif idade >= 39 and idade < 49:
        return 240 / 100
    elif idade >= 49 and idade < 59:
        return 350 / 100
    else:
        return 600 / 100

# Programa principal
print('Bem vindo ao Sistema da Giselle Maria Ferreira Pegado da Silva')
valorBase = float(input('Informe o valor Base do plano: R$ '))
idade = int(input('Informe a idade do cliente: '))

# Chamando a função que calcula a porcetagem 
porcentagem = calcular_porcentagem (idade)
# Chamando a função que calcula o valor mensal
valorMensal = calcular_valor_mensal (valorBase, porcentagem)
# Imprimindo resultado
print(f'O valor mensal do plano é de: R$ {valorMensal:.2f}')