pessoas = int(input('Quantas pessoas'))
biggest = 0
lowest = 0
for c in range(1, pessoas + 1):
    weight = float(input('What is the weight of person {}: '.format(c)))
    if c == 1:
        biggest = c
        lowest = c
    else:
        if weight > biggest:
            biggest = weight
        if weight < lowest: 
            lowest = weight
print('The biggest weight is {}'.format(biggest))