
text = 'curso em video python'
text2 = 'curso python'
print(len(text[0::1]))
print(text.count('o',0,20))
print(text.find('yuri'))
print('python' in text)
print(text.replace()
print(text.upper())
print(text.capitalize())
print(text.title())
print(text.strip())
print(text.lstrip())
lista = text.split()
print(len(lista))
for x in range(0, int(len(lista))):
    print(lista[x] in text)

print(lista[0])
text = ''.join(lista)
print(len(text))

print('Yuri sua altura {} e seu peso {}'.format(lista[3], lista[0]))