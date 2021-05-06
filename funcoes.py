
c = ('\033[m',         # cor 0 = sem cores
     '\033[0;30;41m',  # cor 1 = Vermelho
     '\033[0;30;42m',  # cor 2 = Verde
     '\033[0;30;43m',  # cor 3 = Amarelo
     '\033[0;30;44m',  # cor 4 = Azul
     '\033[0;30;45m',  # cor 5 = Roxo
     '\033[7;30m',  # cor 6 = Branco
    )

def opcao():
   print('\033[0;30;41mDIGITE A OPÇÃO QUE DESEJA CALCULAR:\33[m')
   print('''
            [0] - calcular a plaejado todo
            [1] - calcular area da caixa (laterais, base, chápeu e divisória central (se houver)).
            [2] - calcular o fundo
            [3] - Calular a(s) porta(s)
            [4] - Calcular as gavetas
            [5] - calcular as prateleiras
            [6] - calcular os fiancos.
            [7] - calcular um painel.
        '''.upper())


def medidas(m='SEM MATERIAL', a=0, l=0, p=0):
    print('PRIMEIRO DIGITE AS MEDIDAS DO QUE DESEJA CALCULAR.')
    medida = list()
    copaimed = list()
    while True:
        medida.append(str(input('O TIPO DE MATERIAL : ').strip().upper()))
        medida.append(float(input('DIGITE:A ALTURA EM METROS : '.replace('.', ','))))
        medida.append(float(input('LARGURA EM METROS : '.replace('.', ','))))
        medida.append(float(input('PROFUNDIDADE : '.replace('.', ','))))
        copaimed.append(medida[:])
        medida.clear()
        medidas = copaimed[0][0], copaimed[0][1], copaimed[0][2], copaimed[0][3]
        print(medidas)
        break

def caixa():

        plan = list()
        plancopia = list()
        while True:
            cont = 0
            plan.append(str(input('O TIPO DE MATERIAL : ').strip().upper()))
            plan.append(float(input('DIGITE:A ALTURA EM METROS : '.replace('.', ','))))
            plan.append(float(input('LARGURA EM METROS : '.replace('.', ','))))
            plan.append(float(input('QUANTIDADE : '.replace('.', ','))))
            plancopia.append(plan[:])
            plan.clear()
            area = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3]))
            #calc = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3])/5.06)
            cont += (area/5.06)
            resp = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: '))
            if resp not in 'Nn':
                break
            subtitulos(f'O metro quadrado total da Caixa é: {area:.2f} metros '.upper())
            subtitulos(f'E serão necessários {area/5.06:.2f} CHapas de 2.75 x 1.84 do material {plancopia[0][0]} '.upper())
            break


def fundo():

    plan = list()
    plancopia = list()
    while True:
        cont = 0
        plan.append(str(input('O TIPO DE MATERIAL : ').strip().upper()))
        plan.append(float(input('DIGITE:A ALTURA EM METROS : '.replace('.', ','))))
        plan.append(float(input('LARGURA EM METROS : '.replace('.', ','))))
        plan.append(float(input('QUANTIDADE : '.replace('.', ','))))
        plancopia.append(plan[:])
        plan.clear()
        area = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3]))
        # calc = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3])/5.06)
        cont += (area / 5.06)
        resp = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: '))
        if resp not in 'Nn':
            break
        subtitulos(f'O metro quadrado total da Caixa é: {area:.2f} metros '.upper())
        subtitulos(
            f'E serão necessários {area / 5.06:.2f} CHapas de 2.75 x 1.84 do material {plancopia[0][0]} '.upper())
        break


def titulo(msg, cor=0):
        tam = len(msg) +4
        print('~' * tam)
        print(c[2], end='')
        print(f' {msg}\33[m')
        print('~' * tam)

def subtitulos(msg):
    print(c[5], end='')
    print(f'{msg}\33[m')
    print(c[5], end='')


