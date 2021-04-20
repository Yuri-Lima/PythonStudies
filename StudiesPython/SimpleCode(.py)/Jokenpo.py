from random import randint

itens = ('Rock', 'Paper', 'Scissor')
comp = randint(0, len(itens)-1)
print('The computer choose: {}'.format(itens[comp]))
print('-='*20)

print('''your opitions are:
[ 0 ] Rock
[ 1 ] Paper
[ 2 ] Scissor''')
print('-='*20)
player = int(input('What is your choice?'))

if ((player + comp) == 1): #Rock e Paper--> Paper win
    print('{} vs {} Paper is winner'.format(itens[player], itens[comp]))
elif ((player + comp) == 2): #Rock e Scissor--> Rock win
    print('{} vs {} Rock is winner'.format(itens[player], itens[comp]))
elif ((player + comp) == 3): #Paper e Scissor--> Scissor win
    print('{} vs {} Scissor is winner'.format(itens[player], itens[comp]))
else:
    print('{} vs {} Draw Gamers'.format(itens[player], itens[comp]))
