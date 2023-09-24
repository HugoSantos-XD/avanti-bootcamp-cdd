"Crie uma tupla com os nomes de alguns animais.Em seguida, "
"peça ao usuário para digitar o nome de um animal e verifique se ele está presente na tupla"

tupla = ('ave','cachorro','ema','foca','golfinho','hipopotamo')

animal = str(input('Digite o nome do animal:'))

if animal in tupla:
    print('ANIMAL ESTÁ NA TUPLA')
else:
    print('ANIMAL NÃO ESTÁ NA TUPLA')