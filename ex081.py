lista = []
cont = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Deseja continuar? [S/N]'))
    if continuar not in 'Ss':
        break

lista.sort(reverse=True)
print(f'Foram digitados {cont} numeros')
print(f'A lista em forma decrescente: {lista}')
if 5 in lista:
    print('Sim, temos o valor 5 na lista.')
else:
    print('Não temos o valor 5 na lista.')

