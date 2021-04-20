
# r1 < r2 + r3
# r2 < r1 + r3
# r3 < r2 + r1
print('-'*20)
print('')
print('-'*20)
r1 = float(input('fist segment: '))
r2 = float(input('secund segment: '))
r3 = float(input('third segment: '))
# styles: 0(none) 1(bold) 4(underline) 7(30.31.32.33.34.35.36.37)
if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1):
    print('Triangle ok')
    if (r1 == r2 == r3): 
        print('Equilatero')
    elif (r1 == r2 or r1 == r3) or (r2 == r3 or r2 == r1) or (r3 == r1 or r3 == r2):
        print('Isorceles')
    elif (r1 != r2 != r3 != r1): 
        print('Escaleno')
else:
    print('Triangule false')



