dist = float(input('what will be the distance of travel: '))

cost = dist * 0.50 if dist <= 200 else dist * 0.45

print('The cost of travel will be: {}'.format(cost))
