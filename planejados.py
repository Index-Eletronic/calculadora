import funcoes
from time import sleep

funcoes.titulo('CALCULADORA DE PLANEJADOS', 2)


def calcular(a=0, l=0, p=0):
    print('PRIMEIRO DIGITE AS MEDIDAS DO QUE DESEJA CALCULAR.')
    medida = list()
    medidacopy = list()
    soma = 0
    somachapa = 0
    while True:
        medida.append(float(input('ALTURA: ')))
        medida.append(float(input('LARGURA: ')))
        medida.append(float(input('PROFUNDIDADE: ')))
        medidacopy.append(medida[:])
        medida.clear()
        calc = (medidacopy[0][0] * medidacopy[0][1])
        chapa = calc/4.95
        #funcoes.titulo (f' As medidas digitadas foram: ALtura:{alt} -  Largura: {lar} -  Profundidade: {prof}', 3)
        perg = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: ')).strip().upper()[0]
        if perg in 'Nn':
            soma += calc
            somachapa += chapa
            funcoes.titulo(f'O TOTAL EM m² é: {soma}', 2)
            funcoes.titulo(f'SERÃO NECESSÁRIAS {somachapa:.2F} CHAPAS', 4)
            sleep(1)
            break
        else:
            soma += calc
            somachapa += chapa
            funcoes.titulo(f'O TOTAL EM m² É: {soma} METROS QUADRADOS', 2)
            funcoes.titulo(f'SERÃO NECESSÁRIAS {somachapa:.2F} CHAPAS', 4)
            sleep(1)
usuario = calcular()

