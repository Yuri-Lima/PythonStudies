
Name = str(input('Palidrome: ')).strip('i')
print(Name)
Name = str(input('Palidrome: ')).strip().upper().split()
print(Name)
Name = ''.join(Name)
inverse = ''

if Name == Name[::-1]:
    print('It is a Palidrome {}'.format(Name))
    print(Name == Name[::-1])

for letter in range(len(Name) -1, -1, -1):
    inverse += Name[letter]

if inverse == Name:
    print('It is a Palidrome {} equal {}'.format(inverse, Name))
else:
    print('It isn\'t a Palidrome {} unequal {}'.format(inverse, Name))