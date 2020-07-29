
"""
Project: Numbers in Words
Author: Yuri Lima
Email: y.m.lima19@gmail.com
GitHub: https://github.com/Yuri-Lima
Goals: The main ideia this project is in the future i will create a API. 
This API will help developments find every numbers in words. 
"""
unit = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fiveteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 
'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 
'Hundred', 'Thousand', 'Million', 'Billion', 'Trillion']
# ====================================================================================================
print('Please give me a number (Max = 13 Places Numbers):')
num = int(input())  
decimalplace = int(len(str(num)))
# ====================================================================================================
# ################################ Place Decimal ######################################################
# ====================================================================================================
trillions = int((num / 1000000000000) % 10)#9.999.999.999.999
# ************************************************************
hundred_billions = int((num / 1000000000) % 1000)#999.999.999.999
ten_billions = int((num / 1000000000) % 100)#99.999.999.999
billions = int((num / 1000000000) % 10)#9.999.999.999
# ************************************************************
hundred_millions = int((num / 1000000) % 1000)#99.999.999
ten_millions = int((num / 1000000) % 100)#99.999.999
millions = int(((num / 1000000)) % 10)#9.999.999
# ************************************************************
hundred_thousands = int((num / 1000) % 1000)#999.999
ten_thousands = int((num / 1000) % 100)#99.999
thousands = int((num / 1000) % 10)#9.999
# ************************************************************
hundreds = int((num / 100) % 10)#999
tens = int((num / 10) % 10)#3
ones = int(num / 1 % 10)#2
# ====================================================================================================
# ################################ Selection Places Decimals ##########################################
# ====================================================================================================
list_validate = {'flag_trillion': False,'flag_hundred_billion': False,'flag_ten_billion': False, 'flag_billion': False, 'flag_hundred_million': False, 'flag_ten_million': False, 
    'flag_hundred_thousand': False, 'flag_million': False, 'flag_ten_thousand': False, 'flag_thousand': False, 'flag_hundred': False, 'flag_decimal': False}
# Decimal
if decimalplace <= 2:
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Hundreds    
elif decimalplace == 3:
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Thousands
elif decimalplace == 4:
    list_validate['flag_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Ten_thousands
elif decimalplace == 5:
    list_validate['flag_ten_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# hundreds_thousands
elif decimalplace == 6:
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Millions 
elif decimalplace == 7:
    list_validate['flag_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Ten_millions 
elif decimalplace == 8:
    list_validate['flag_ten_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Hundred_millions 
elif decimalplace == 9:
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Billions 
elif decimalplace == 10:
    list_validate['flag_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Ten_billions 
elif decimalplace == 11:
    list_validate['flag_ten_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Hundred_billions 
elif decimalplace == 12:
    list_validate['flag_hundred_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# Trillions 
elif decimalplace == 13:
    list_validate['flag_trillion'] = True 
    list_validate['flag_hundred_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
# ====================================================================================================
# ################################ Functions ######################################################
# ====================================================================================================
# TODO Steps into the index Unit[]
def calc_index_steps(index_tens):
    _collection = str('{} {}'.format(unit[(index_tens - (9 * (int((index_tens / 10)) - 2))) - (index_tens % 10)], 
                    unit[index_tens % 10] if index_tens % 10 != 0 else ''))
    return _collection
# ====================================================================================================
# ################################ Code Begin ######################################################
# ====================================================================================================
# TODO Trillions
def number_in_word(list_validate):
    joins = list()   
    if list_validate['flag_trillion'] and trillions != 0:
        joins.append((str(unit[trillions] + ' ' + unit[unit.index('Trillion')])))
        if hundred_billions == hundred_millions == ten_millions == millions == hundred_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_billion'] = False
    # ====================================================================================================
    # TODO Hundred_billions
    if list_validate['flag_hundred_billion'] and hundred_billions != 0:
        hundreds_billion_part = int((hundred_billions / 100) % 10)#999
        if hundreds_billion_part % 10 != 0:
            joins.append((str(unit[hundreds_billion_part] + ' ' + unit[unit.index('Hundred')])))
        
        decimal_billion_part = int((hundred_billions % 100))
        if decimal_billion_part <= 20:
            joins.append((str(unit[decimal_billion_part] + ' ' + unit[unit.index('Billion')])))

        if decimal_billion_part >= 21:
            joins.append((calc_index_steps(decimal_billion_part) + ' ' + unit[unit.index('Billion')]))
    # ====================================================================================================
    # TODO Ten_billions
    if list_validate['flag_ten_billion'] and ten_billions != 0:
        if ten_billions <= 20:
            joins.append((str(unit[ten_billions] + ' ' + unit[unit.index('Billion')])))

        if ten_billions >= 21:
            collection = calc_index_steps(ten_billions)
            collection += ' ' + unit[unit.index('Billion')]
            joins.append(collection)
    # ====================================================================================================
    # TODO Billions   
    if list_validate['flag_billion'] and billions != 0:
        joins.append((str(unit[billions] + ' ' + unit[unit.index('Billion')])))

        if hundred_millions == ten_millions == millions == hundred_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_million'] = False
    # ====================================================================================================
    # TODO Hundred_millions
    if list_validate['flag_hundred_million'] and hundred_millions != 0:
        hundreds_million_part = int((hundred_millions / 100) % 10)#999
        if hundreds_million_part % 10 != 0:
            joins.append((str(unit[hundreds_million_part] + ' ' + unit[unit.index('Hundred')])))
        
        decimal_million_part = int((hundred_millions % 100))
        if decimal_million_part <= 20:
            joins.append((str(unit[decimal_million_part] + ' ' + unit[unit.index('Million')])))

        if decimal_million_part >= 21:
            joins.append((calc_index_steps(decimal_million_part) + ' ' + unit[unit.index('Million')]))
    # ====================================================================================================
    # TODO Ten_millions
    if list_validate['flag_ten_million'] and ten_millions != 0:
        if ten_millions <= 20:
            joins.append((str(unit[ten_millions] + ' ' + unit[unit.index('Million')])))
        
        if ten_millions >= 21:
            joins.append((calc_index_steps(ten_millions) + ' ' + unit[unit.index('Million')]))
    # ==================================================================================================== 
    # TODO Millions    
    if list_validate['flag_million'] and millions != 0:
        joins.append((str(unit[millions] + ' ' + unit[unit.index('Million')])))
        if hundred_thousands == ten_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_thousand'] = False
    # ====================================================================================================
    # TODO Hundreds_thousands
    if list_validate['flag_hundred_thousand'] and hundred_thousands != 0:

        hundreds_part = int((hundred_thousands / 100) % 10)#999
        if hundreds_part % 10 != 0:
            joins.append((str(unit[hundreds_part] + ' ' + unit[unit.index('Hundred')])))

        decimal_hundred_thousands_part = int((hundred_thousands % 100))
        if decimal_hundred_thousands_part <= 20:
            joins.append((str(unit[decimal_hundred_thousands_part] + ' ' + unit[unit.index('Thousand')])))

        if decimal_hundred_thousands_part >= 21:
            joins.append((calc_index_steps(decimal_hundred_thousands_part) + ' ' + unit[unit.index('Thousand')]))
    # ====================================================================================================
    # TODO Ten_thousands
    if list_validate['flag_ten_thousand'] and ten_thousands != 0:
        if ten_thousands <= 20:
            joins.append((str(unit[ten_thousands] + ' ' + unit[unit.index('Thousand')])))
        if ten_thousands >= 21:
            joins.append((calc_index_steps(ten_thousands) + ' ' + unit[unit.index('Thousand')]))
    # ====================================================================================================
    # TODO Thousands
    if list_validate['flag_thousand'] and thousands != 0:
        joins.append((str(unit[thousands] + ' ' + unit[unit.index('Thousand')])))
    # ====================================================================================================
    # TODO Hundreds
    if list_validate['flag_hundred'] and hundreds != 0:
        joins.append((str(' ' + unit[hundreds] + ' ' + unit[unit.index('Hundred')]))) 
    # ====================================================================================================
    # TODO Tens
    # Numbers under 19
    decimal = int(str(num)[-2:])
    if list_validate['flag_decimal'] and decimal != 0:
        if decimal <= 19:
            joins.append(str(unit[decimal]))
        elif decimal >= 20:
            joins.append(str('{} {}'.format(unit[(decimal - (9 * (tens - 2))) - ones], unit[ones] if ones != 0 else '')))
    # ====================================================================================================
    #print('trillions {}, hundred_billions {}, ten_billions {}, billions: {}, hundred_millions: {}, ten_millions: {}, millions: {}, hundred_thousands: {}, ten_thousands: {}, thousands: {}, hundreds:{}, tens: {}, ones: {}'
    #.format(trillions, hundred_billions, ten_billions, billions, hundred_millions, ten_millions, millions, hundred_thousands, ten_thousands, thousands, hundreds, tens, ones))    
    return joins

print(number_in_word(list_validate))
