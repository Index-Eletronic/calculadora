import funcoes

funcoes.titulo('CALCULADORA DE PLANEJADOS', 2)


funcoes.opcao()

perg = (int(input(f'Digite sua opção aqui : ').strip()))

if perg == 0:
    pass

elif perg == 1:
    funcoes.titulo('  opção para calcular a Caixa (Laterais/Base/Chápeu)'.upper())
    funcoes.caixa()

elif perg == 2:
    pass
elif perg == 3:
    pass
elif perg == 4:
    pass
elif perg == 5:
    pass
elif perg == 6:
    pass
elif perg == 7:
    pass
else:
    funcoes.titulo('Valte sempre!')

