'''Roman numeral convertor'''
numeral_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}


def roman_to_int(roman):
    '''Converts roman numerals to integer'''
    temp_var_01 = ''
    result = 0
    for i in roman:
        if temp_var_01 !='' and numeral_dict[temp_var_01] < numeral_dict[i]:
            result = result + numeral_dict[i] - 2* numeral_dict[temp_var_01]
        else: result = result + numeral_dict[i]
        print(i)
        temp_var_01 = i
    print(result)
    return result

def int_to_roman(number):
    '''placeholder'''
    return number
