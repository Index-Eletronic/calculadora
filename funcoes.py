
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
def caixa():
    while True:
        plan.append(float(input('DIGITE:A ALTURA EM METROS: '.replace('.', ','))))
        plan.append(float(input('LARGURA EM METROS: '.replace('.', ','))))
        plan.append(input('LARGURA EM METROS: '.replace('.', ',')))
        plan.append(input('O TIPO DE MATERIAL: '.replace('.', ',')))
        plancopia.append(plan[:])
        #calc = (alt * lar) * qt
        plan.clear()

        print(plancopia[0][0])

        print(plancopia)
        break


#==============Calculando a caixa======================

def titulo(msg, cor=0):
        tam = len(msg) +4
        print('~' * tam)
        print(c[2], end='')
        print(f' {msg}\33[m')
        print('~' * tam)
