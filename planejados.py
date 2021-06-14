import funcoes

funcoes.titulo('CALCULADORA DE PLANEJADOS', 2)


def calcular(a=0, l=0, p=0):
    print('PRIMEIRO DIGITE AS MEDIDAS DO QUE DESEJA CALCULAR.')
    medida = list()
    copaimed = list()
    soma = 0
    while True:
        medida.append(float(input('ALTURA: ')))
        medida.append(float(input('LARGURA: ')))
        medida.append(float(input('PROFUNDIDADE: ')))
        copaimed.append(medida[:])
        calc = (copaimed[0][0] * copaimed[0][1])
        medida.clear()
        medidas = copaimed[0][0], copaimed[0][1], copaimed[0][2]
        print(medidas)
        perg = str(input('TEM MAIS DA MESMA MEDIDA PARA ADICIONAR? [S/N]: ')).strip().upper()[0]
        if perg == 'Nn':
            break
        else:
            soma += calc
        print(soma)

usuario = calcular()

