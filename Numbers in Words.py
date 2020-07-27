
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
# print(decimalplace)
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
# ################################ Flags Places Decimals ##############################################
# ====================================================================================================
flag_decimal = False
flag_hundred = False
flag_thousand = False
flag_ten_thousand = False
flag_hundred_thousand = False
flag_million = False
flag_ten_million = False
flag_hundred_million = False
flag_billion = False
flag_ten_billion = False
flag_hundred_billion = False
flag_trillion = False
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
    #flag_thousand = True
# ====================================================================================================
# hundreds_thousands
elif decimalplace == 6:
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_ten_thousand = True
    #flag_thousand = True
# ====================================================================================================
# Millions 
elif decimalplace == 7:
    list_validate['flag_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_ten_thousand = True
    #flag_thousand = True
# ====================================================================================================
# Ten_millions 
elif decimalplace == 8:
    list_validate['flag_ten_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_million = True
    #flag_ten_thousand = True
    #flag_thousand = True
# ====================================================================================================
# Hundred_millions 
elif decimalplace == 9:
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_ten_million = True
    #flag_million = True
    #flag_ten_thousand = True
    #flag_thousand = True
# ====================================================================================================
# Billions 
elif decimalplace == 10:
    list_validate['flag_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_ten_million = True
    #flag_million = True
    #flag_ten_thousand = True
    #flag_thousand = True

# ====================================================================================================
# Ten_billions 
elif decimalplace == 11:
    
    list_validate['flag_ten_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_billion = True
    #flag_ten_million = True
    #flag_million = True
    #flag_ten_thousand = True
    #flag_thousand = True

# ====================================================================================================
# Hundred_billions 
elif decimalplace == 12:

    list_validate['flag_hundred_billion'] = True
    list_validate['flag_hundred_million'] = True
    list_validate['flag_hundred_thousand'] = True
    list_validate['flag_hundred'] = True
    list_validate['flag_decimal'] = True
    #flag_ten_billion = True
    #flag_billion = True
    #flag_ten_million = True
    #flag_million = True
    #flag_ten_thousand = True
    #flag_thousand = True
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
# TODO Function 1 formule
def calc_index_steps(index_tens):
    _collection = str('{} {}'.format(unit[(index_tens - (9 * (int((index_tens / 10)) - 2))) - (index_tens % 10)], 
                    unit[index_tens % 10] if index_tens % 10 != 0 else ''))
    return _collection
# ====================================================================================================
# TODO Function tests of numbers
def tests_numbers():
    list_numbers = (0, 1, 10, 100, 101, 110, 220, 202, 1000, 1001, 1010, 2020, 2200, 10000, 10101, 10202, 11100, 12000, 100000, 100100, 101010, 101101, 120020)

# ====================================================================================================
# ################################ Code Beginner ######################################################
# ====================================================================================================
# TODO Trillions
def number_in_word(list_validate):
    collection = str()
    joins = list()   
    if list_validate['flag_trillion'] and trillions != 0:
        collection = str(unit[trillions] + ' ' + unit[unit.index('Trillion')]) 
        joins.append(collection)
        #print('Trillion')
        if hundred_billions == hundred_millions == ten_millions == millions == hundred_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_billion'] = False
    # ====================================================================================================
    # TODO Hundred_billions
    if list_validate['flag_hundred_billion'] and hundred_billions != 0:
        hundreds_billion_part = int((hundred_billions / 100) % 10)#999
        if hundreds_billion_part % 10 != 0:
            collection = str(unit[hundreds_billion_part] + ' ' + unit[unit.index('Hundred')]) 
            joins.append(collection)
            #print('hundred_billions')
        
        decimal_billion_part = int((hundred_billions % 100))
        if decimal_billion_part <= 20:
            collection = str(unit[decimal_billion_part] + ' ' + unit[unit.index('Billion')]) 
            joins.append(collection)
            #print('decimal_billion_part < 20')

        if decimal_billion_part >= 21:
            collection = calc_index_steps(decimal_billion_part)
            collection += ' ' + unit[unit.index('Billion')]
            joins.append(collection)
            #print('decimal_billion_part >= 21')
    # ====================================================================================================
    # TODO Ten_billions
    if list_validate['flag_ten_billion'] and ten_billions != 0:
        if ten_billions <= 20:
            collection = str(unit[ten_billions] + ' ' + unit[unit.index('Billion')]) 
            joins.append(collection)
            #print('ten_billions <= 20')

        if ten_billions >= 21:
            collection = calc_index_steps(ten_billions)
            collection += ' ' + unit[unit.index('Billion')]
            joins.append(collection)
            #print('ten_billions >= 21')
            #The code that make 10 000 000 works, should be in the condition Millions above here
    # ====================================================================================================
    # TODO Billions   
    if list_validate['flag_billion'] and billions != 0:
        collection = str(unit[billions] + ' ' + unit[unit.index('Billion')]) 
        joins.append(collection)
        #print('Billion')
        if hundred_millions == ten_millions == millions == hundred_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_million'] = False
    # ====================================================================================================
    # TODO Hundred_millions
    if list_validate['flag_hundred_million'] and hundred_millions != 0:
        hundreds_million_part = int((hundred_millions / 100) % 10)#999
        if hundreds_million_part % 10 != 0:
            collection = str(unit[hundreds_million_part] + ' ' + unit[unit.index('Hundred')]) 
            joins.append(collection)
            #print('hundred_millions')
        
        decimal_million_part = int((hundred_millions % 100))
        if decimal_million_part <= 20:
            collection = str(unit[decimal_million_part] + ' ' + unit[unit.index('Million')]) 
            joins.append(collection)
        # print('decimal_million_part < 20')

        if decimal_million_part >= 21:
            collection = calc_index_steps(decimal_million_part)
            collection += ' ' + unit[unit.index('Million')]
            joins.append(collection)
            #print('decimal_million_part >= 21')
 
    # ====================================================================================================
    # TODO Ten_millions
    if list_validate['flag_ten_million'] and ten_millions != 0:
        if ten_millions <= 20:
            collection = str(unit[ten_millions] + ' ' + unit[unit.index('Million')]) 
            joins.append(collection)
            #print('ten_millions <= 20')

        
        if ten_millions >= 21:
            collection = calc_index_steps(ten_millions)
            collection += ' ' + unit[unit.index('Million')]
            joins.append(collection)
            #print('ten_millions >= 21')
            #The code that make 10 000 000 works, should be in the condition Millions above here
    # ==================================================================================================== 
    # TODO Millions    
    if list_validate['flag_million'] and millions != 0:
        collection = str(unit[millions] + ' ' + unit[unit.index('Million')]) 
        joins.append(collection)
        #print('millions')
        if hundred_thousands == ten_thousands == thousands == hundreds == tens == ones == 0:
            list_validate['flag_hundred_thousand'] = False
    # ====================================================================================================
    # TODO Hundreds_thousands
    if list_validate['flag_hundred_thousand'] and hundred_thousands != 0:

        hundreds_part = int((hundred_thousands / 100) % 10)#999
        if hundreds_part % 10 != 0:
            collection = str(unit[hundreds_part] + ' ' + unit[unit.index('Hundred')]) 
            joins.append(collection)
            #print('hundred_thousands')

        decimal_hundred_thousands_part = int((hundred_thousands % 100))
        if decimal_hundred_thousands_part <= 20:
            collection = str(unit[decimal_hundred_thousands_part] + ' ' + unit[unit.index('Thousand')]) 
            joins.append(collection)
            #print('decimal_hundred_thousands_part <= 20') 
        if decimal_hundred_thousands_part >= 21:
            collection = calc_index_steps(decimal_hundred_thousands_part)
            collection += ' ' + unit[unit.index('Thousand')]
            joins.append(collection)
            #print('decimal_hundred_thousands_part >= 21') 
    # ====================================================================================================
    # TODO Ten_thousands
    if list_validate['flag_ten_thousand'] and ten_thousands != 0:
        if ten_thousands <= 20:
            collection = str(unit[ten_thousands] + ' ' + unit[unit.index('Thousand')]) 
            joins.append(collection)
            #print('ten_thousands <= 20') 
        if ten_thousands >= 21:
            collection = calc_index_steps(ten_thousands)
            collection += ' ' + unit[unit.index('Thousand')]
            joins.append(collection)
            #print('ten_thousands >= 21')
    # ====================================================================================================
    # TODO Thousands
    if list_validate['flag_thousand'] and thousands != 0:
        collection = str(unit[thousands] + ' ' + unit[unit.index('Thousand')]) 
        joins.append(collection)
        #print('thousands')
    # ====================================================================================================
    # TODO Hundreds
    if list_validate['flag_hundred'] and hundreds != 0:
        collection = str(' ' + unit[hundreds] + ' ' + unit[unit.index('Hundred')]) 
        joins.append(collection) 
        #print('hundreds')          
    # ====================================================================================================
    # TODO Tens
    # Numbers under 19
    decimal = int(str(num)[-2:])
    if list_validate['flag_decimal'] and decimal != 0:
        if decimal <= 19:
            collection = str(unit[decimal])
            joins.append(str(unit[decimal]))
            #print('decimal <= 19')  
        elif decimal >= 20:
            collection = str('{} {}'.format(unit[(decimal - (9 * (tens - 2))) - ones], unit[ones] if ones != 0 else ''))
            joins.append(collection)
            #print('decimal >= 20')
    # ====================================================================================================
    #print(joins)
    #print('- = '*30)
    #print('trillions {}, hundred_billions {}, ten_billions {}, billions: {}, hundred_millions: {}, ten_millions: {}, millions: {}, hundred_thousands: {}, ten_thousands: {}, thousands: {}, hundreds:{}, tens: {}, ones: {}'
    #.format(trillions, hundred_billions, ten_billions, billions, hundred_millions, ten_millions, millions, hundred_thousands, ten_thousands, thousands, hundreds, tens, ones))    
    return joins

print(number_in_word(list_validate))
