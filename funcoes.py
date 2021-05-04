
c = ('\033[m',         # cor 0 = sem cores
     '\033[0;30;41m',  # cor 1 = Vermelho
     '\033[0;30;42m',  # cor 2 = Verde
     '\033[0;30;43m',  # cor 3 = Amarelo
     '\033[0;30;44m',  # cor 4 = Azul
     '\033[0;30;45m',  # cor 5 = Roxo
     '\033[7;30m',  # cor 6 = Branco
    )


plan = list()
plancopia = list()
cont = 0
def caixa():
    while True:
        cont = 0
        plan.append(str(input('O TIPO DE MATERIAL : '.replace('.', ','))))
        plan.append(float(input('DIGITE:A ALTURA EM METROS : '.replace('.', ','))))
        plan.append(float(input('LARGURA EM METROS : '.replace('.', ','))))
        plan.append(float(input('QUANTIDADE : '.replace('.', ','))))
        plancopia.append(plan[:])
        mat = plancopia[0][0]
        plan.clear()
        area = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3]))
        #calc = (((plancopia[0][1] * plancopia[0][2]) * plancopia[0][3])/5.06)
        cont += (area/5.06)
        resp = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: '))
        if resp not in 'Nn':
            break
        print(f'O metro quadrado total da Caixa é: {area:.2f}')
        print(f'E serão necessários {area/5.06:.2f} placas do material {plancopia[0][0]} para fabrica-lá')
        break


#==============Calculando a caixa======================

def titulo(msg, cor=0):
        tam = len(msg) +4
        print('~' * tam)
        print(c[2], end='')
        print(f' {msg}\33[m')
        print('~' * tam)
