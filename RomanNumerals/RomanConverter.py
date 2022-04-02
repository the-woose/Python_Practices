'''Program to convert roman numerals to integers and back'''
numeral_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# numeral_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def roman_to_int(roman):
    '''converts roman to integer'''
    for i in numeral_dict:
        if numeral_dict[roman] == numeral_dict[i]:
            print(i)
        else:
            print("doesn't exist")
    # pass
def int_to_roman(number):
    '''converts integer to roman'''
    for i in numeral_dict.items():
        if numeral_dict.values(number) == numeral_dict.values(i):
            print(i)
        else:
            print("doesn't exist")
    # pass

temp_01 = input()
roman_to_int(temp_01)
