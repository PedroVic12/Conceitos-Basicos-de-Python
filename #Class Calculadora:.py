# Class Calculadora:
def soma(n1,n2):
    return n1 + n2


def subtração(n1,n2):
    return n1 - n2


def Multiplicação(n1,n2):
    return n1*n2


def divisão(n1,n2):
    return n1/n2


print('\nBEM VINDO CALCULADORA SIMPLES PARA NOOBS\n')

calc_dic = {
    '+':soma,
    '-':subtração,
    '*':Multiplicação,
    '/':divisão
}

def inputUsuario():
    print('\n=====================')
    print('Escolha uma operação:\n')
    for symbol in calc_dic:
        print('        ', symbol)
    print('\n=====================')

def calcularadora():
    n1 = float(input('Digite o primeiro numero: '))

    #loop
    controle = True
    while controle:
        inputUsuario()
        operation = input('Digite qual operação deseja: ')
        n2 = float(input('Digite o segundo numero: '))

        #Calculo
        calcular = calc_dic[operation]
        result = calcular(n1,n2)
        print (f'{n1} {operation} {n2} = {result}')

        #Loop Controle
        resp = input('Deseja continuar? [S | N] ou new para um novo calculo ').lower()
        if resp == 'n':
            controle = False
        if resp == 's':
            n1 = result
        if resp == 'new':
            calcularadora()




calcularadora()