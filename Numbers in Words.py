"""
Project: Numbers in Words
Author: Yuri Lima
Email: y.m.lima19@gmail.com
GitHub: https://github.com/Yuri-Lima
Goals: The main ideia this project is in the future i will create a API. 
This API will help developments find every numbers in words. 
"""
from Locate import unit_EN
# ====================================================================================================
num = list()
locate = list()
print('Please give me a number (Max = 13 Places Numbers):')
while True: 
    locate = '1' #input('Choice locate 1 to English and 2 to Portugues: ')
    num = '1000101101101'
    #num = '1234567891234'#input('Give me a number: ')
    if num.isnumeric() and locate.isnumeric:
        break
# ====================================================================================================
# ################################ Selection Places Decimals ##########################################
# ====================================================================================================
place = {'ones': 0, 'tens': 0, 'hundreds': 0, 'thousands': 0, 'ten_thousands': 0, 'hundred_thousands': 0,
        'millions': 0, 'ten_millions': 0, 'hundred_millions': 0, 'billions': 0, 'ten_billions': 0,
        'hundred_billions': 0, 'trillions': 0, 'ten_trillions': 0, 'hundred_trillions': 0, 'quadrillions': 0,'ends': 0}

list_validate = {'flag_trillion': False,'flag_hundred_billion': False,'flag_ten_billion': False, 'flag_billion': False, 'flag_hundred_million': False, 'flag_ten_million': False, 
    'flag_hundred_thousand': False, 'flag_million': False, 'flag_ten_thousand': False, 'flag_thousand': False, 'flag_hundred': False, 'flag_decimal': False, 'flag_one': False}
# ====================================================================================================
# ################################ Place Decimal ######################################################
# ====================================================================================================
for index, k in enumerate(place.keys(), start=1):
    if index == len(num) + 1:
        break
    else:
        place[k] = int(num[-index])

decimalplaces = index - 1 #if place['trillions']== 0 else index - 0
# Decimal Parts of Number
tens_part = int(str(place['tens']) + str(place['ones']))
tens_thousands_part = int(str(place['ten_thousands']) + str(place['thousands']))
tens_millions_part = int(str(place['ten_millions']) + str(place['millions']))
tens_billions_part = int(str(place['ten_billions']) + str(place['billions']))

#two statment below are always true
list_validate['flag_hundred'] = True
list_validate['flag_decimal'] = True
list_validate['flag_ones'] = True
# ====================================================================================================
# Thousands
if decimalplaces == 4:
    list_validate['flag_thousand'] = True
# ====================================================================================================
# Ten_thousands
elif decimalplaces == 5:
    list_validate['flag_ten_thousand'] = True
# ====================================================================================================
# hundreds_thousands
elif decimalplaces == 6:
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Millions 
elif decimalplaces == 7:
    list_validate['flag_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Ten_millions 
elif decimalplaces == 8:
    list_validate['flag_ten_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Hundred_millions 
elif decimalplaces == 9:
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Billions 
elif decimalplaces == 10:
    list_validate['flag_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Ten_billions 
elif decimalplaces == 11:
    list_validate['flag_ten_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Hundred_billions 
elif decimalplaces == 12:
    list_validate['flag_hundred_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Trillions 
elif decimalplaces == 13:
    list_validate['flag_trillion'] = True 
    list_validate['flag_hundred_billion'] = True
    list_validate['flag_ten_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# Trillions 
elif decimalplaces == 14:
    list_validate['flag_trillion'] = True 
    list_validate['flag_hundred_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
# ====================================================================================================
# ################################ Functions #########################################################
# ====================================================================================================
def calc_index_steps(index_tens):
    # TODO Steps into the index Unit[]
    """Steps Postision into the Unit[]

    Args:
        index_tens (int): receve the tens place to find the position into the dictionary Unit[]

    Returns:
        [type]: [description]
    """
    if locate == '1':
        _collection = str('{} {}'.format(unit_EN[(index_tens - (9 * (int((index_tens / 10)) - 2))) - (index_tens % 10)], 
                    unit_EN[index_tens % 10] if index_tens % 10 != 0 else ''))                   
    return _collection

def number_in_word(list_validate):
    """Turn number in Words

    Args:
        list_validate (Dict): wich flag works allowing or not validate contictions 'If`s' 

    Returns:
        [list]: contain all numbers in words
    """
    joins = list()
    # TODO Trillions #9.999.999.999.999
    if list_validate['flag_trillion'] and place['trillions'] != 0:
        if locate == '1':
            joins.append((str(unit_EN[place['trillions']] + ' ' + 'Trillion')))
            inc = 0
            for enum, n in enumerate(num[1::1], start=1):
                if n == '0':
                    inc += 1
            list_validate['flag_hundred_billion'] = False if inc == enum else True
    # ====================================================================================================
    # TODO Hundred_billions #999.999.999.999 
    if list_validate['flag_hundred_billion'] and place['hundred_billions'] != 0:

        if locate == '1':
            joins.append((str(unit_EN[place['hundred_billions']] + ' ' + 'Hundred')))
 
        if tens_billions_part <= 20:
            if locate == '1':
                joins.append((str(unit_EN[tens_billions_part] + ' ' + 'Billion')))

        if tens_billions_part >= 21:
           if locate == '1':
               joins.append((calc_index_steps(tens_billions_part) + ' ' + 'Billion'))
    # ====================================================================================================
    # TODO Ten_billions #99.999.999.999 
    if list_validate['flag_ten_billion'] and place['ten_billions'] != 0:
        if tens_billions_part <= 20:
            if locate == '1':
                joins.append((str(unit_EN[tens_billions_part] + ' ' + 'Billion')))               
        if tens_billions_part >= 21:
            if locate == '1':
                joins.append(calc_index_steps(place['ten_billions']) + ' ' + 'Billion')
    # ====================================================================================================
    # TODO Billions #9.999.999.999   
    if list_validate['flag_billion'] and place['billions'] != 0:
        if locate == '1':
            joins.append((str(unit_EN[place['billions']] + ' ' + 'Billion')))
            inc = 0
            for enum, n in enumerate(num[1::1], start=1):
                if n == '0':
                    inc += 1
            list_validate['flag_hundred_million'] = False if inc == enum else True
    # ====================================================================================================
    # TODO Hundred_millions #999.999.999
    if list_validate['flag_hundred_million'] and place['hundred_millions'] != 0:
        if place['hundred_millions'] != 0:
            if locate == '1':
                joins.append((str(unit_EN[place['hundred_millions']] + ' ' + 'Hundred')))

        if tens_millions_part <= 20:#9_'99'.999.999
            if locate == '1':
                joins.append((str(unit_EN[tens_millions_part] + ' ' + 'Million')))

        if tens_millions_part >= 21:#9_'99'.999.999
            if locate == '1':
                joins.append((calc_index_steps(tens_millions_part) + ' ' + 'Million'))
    # ====================================================================================================
    # TODO Ten_millions #99.999.999  
    if list_validate['flag_ten_million'] and place['ten_millions'] != 0:
        if tens_millions_part <= 20:#9_'9.9'99.999
            if locate == '1':
                joins.append((str(unit_EN[tens_millions_part] + ' ' + 'Million')))

        if tens_millions_part >= 21:
            if locate == '1':
                joins.append((calc_index_steps(tens_millions_part) + ' ' + 'Million'))
    # ==================================================================================================== 
    # TODO Millions #9.999.999    
    if list_validate['flag_million'] and place['millions'] != 0:
        if locate == '1':
            joins.append((str(unit_EN[place['millions']] + ' ' + 'Million')))
            inc = 0
            for enum, n in enumerate(num[1::1], start=1):
                if n == '0':
                    inc += 1
            list_validate['flag_hundred_thousand'] = False if inc == enum else True
    # ====================================================================================================
    # TODO Hundreds_thousands #999.999
    if list_validate['flag_hundred_thousand'] and place['hundred_thousands'] != 0:

        #hundreds_part = int((hundred_thousands / 100) % 10)#999
        if place['hundreds'] != 0:
            if locate == '1':
                joins.append((str(unit_EN[place['hundred_thousands']] + ' ' + 'Hundred')))

        #decimal_hundred_thousands_part = int((hundred_thousands % 100))
        if tens_thousands_part <= 20:
            if locate == '1':
                joins.append((str(unit_EN[tens_thousands_part] + ' ' + 'Thousand')))
  
        if tens_thousands_part >= 21:
            if locate == '1':
                joins.append((calc_index_steps(tens_thousands_part) + ' ' + unit_EN[unit_EN.index('Thousand')]))
    # ====================================================================================================
    # TODO Ten_thousands #99.999
    if list_validate['flag_ten_thousand'] and place['ten_thousands'] != 0:
        if tens_thousands_part <= 20:
            if locate == '1':
                joins.append((str(unit_EN[tens_thousands_part] + ' ' + 'Thousand')))

        if tens_thousands_part >= 21:
            if locate == '1':
                joins.append((calc_index_steps(tens_thousands_part) + ' ' + 'Thousand'))
    # ====================================================================================================
    # TODO Thousands #9.999
    if list_validate['flag_thousand'] and place['thousands'] != 0:
        if locate == '1':
            joins.append((str(unit_EN[place['thousands']] + ' ' + 'Thousand')))
            inc = 0
            for enum, n in enumerate(num[1::1], start=1):
                if n == '0':
                    inc += 1
            list_validate['flag_hundred'] = False if inc == enum else True
            list_validate['flag_decimal'] = False if inc == enum else True
    # ====================================================================================================
    # TODO Hundreds #999
    if list_validate['flag_hundred'] and place['hundreds'] != 0:
        if locate == '1':
            joins.append((str(' ' + unit_EN[place['hundreds']] + ' ' 'Hundred'))) 
    # ====================================================================================================
    # TODO Tens #99
    if list_validate['flag_decimal'] and place['tens'] != 0:
        if tens_part <= 19:
            if locate == '1':
                joins.append(str(unit_EN[tens_part]))
        elif tens_part >= 20:
            if locate == '1':
                joins.append(str('{} {}'.format(unit_EN[(tens_part - (9 * (place['tens'] - 2))) - place['ones']], unit_EN[place['ones']] if place['ones'] != 0 else '')))
    # ====================================================================================================
    # ====================================================================================================
    # TODO Ones #9
    if list_validate['flag_ones'] and place['ones'] != 0:
        if tens_part <= 19:
            if locate == '1':
                joins.append(str(unit_EN[tens_part]))
    # ====================================================================================================
    return joins

print(number_in_word(list_validate))
