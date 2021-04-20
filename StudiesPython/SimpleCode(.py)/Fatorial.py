
fatorial = 1

numb = int(input('Type a number: '))
print('Calculating {}! = '.format(numb), end='')
for c in range(numb, 0, -1):
    print('{}'.format(c), end='')
    fatorial *= c
    if c != 1:
        print(' x ', end='')
    else:
        print(' = {}'.format(fatorial))

print('{:-^40}'.format('Fim do Programa'))