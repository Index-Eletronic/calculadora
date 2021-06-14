from time import sleep

c = ('\033[m',         # cor 0 = sem cores
     '\033[0;30;41m',  # cor 1 = Vermelho
     '\033[0;30;42m',  # cor 2 = Verde
     '\033[0;30;43m',  # cor 3 = Amarelo
     '\033[0;30;44m',  # cor 4 = Azul
     '\033[0;30;45m',  # cor 5 = Roxo
     '\033[7;30m',  # cor 6 = Branco
    )

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print('~' * tam)
    print(c[2], end='')
    print(f' {msg}\33[m')
    print('~' * tam)

titulo('CALCULADORA DE PLANEJADOS', 2)

def calcular():
    print('PRIMEIRO DIGITE AS MEDIDAS DO QUE DESEJA CALCULAR.')
    medida = list()
    medidacopy = list()
    soma = 0
    somachapa = 0
    quant = 0
    while True:
        medida.append(float(input('ALTURA: ')))
        medida.append(float(input('LARGURA: ')))
        medida.append(float(input('PROFUNDIDADE: ')))
        qtde = int(input('QUANTAS PEÇAS SERÃO NECESSÁRIAS:  '))
        if qtde >= 0:
                quant += qtde
        medidacopy.append(medida[:])
        medida.clear()
        calc = (medidacopy[0][0] * medidacopy[0][1]) * quant
        chapa = calc/4.95
        #funcoes.titulo (f' As medidas digitadas foram: ALtura:{alt} -  Largura: {lar} -  Profundidade: {prof}', 3)
        perg = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: ')).strip().upper()[0]
        if perg in 'Nn':
            soma += calc
            somachapa += chapa
            medidacopy.append(str(input('QUAL É O MATERIAL: ')))
            titulo(f'O TOTAL EM m² é: {soma}', 2)
            sleep(1)
            titulo(f'SERÃO NECESSÁRIAS {somachapa:.2F} CHAPAS DO MAERIAL: {medidacopy[1]}', 4)
            sleep(1)
            print('SALVANDO DADOS EM: Lista de Material.txt...')
            sair = str(input('Aperte ENTER para SAIR'))
            break
        else:
            soma += calc
            somachapa += chapa
            titulo(f'O TOTAL EM m² É: {soma} METROS QUADRADOS', 2)
            sleep(1)
            titulo(f'SERÃO NECESSÁRIAS {somachapa:.2F} CHAPAS', 4)
            sleep(1)

usuario = calcular()