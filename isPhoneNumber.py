#começa com 0, 4 é o ultimo numero da primeira parte e 5 é o -, termina no 9

def isPhoneNumber(string):
    if len(string) != 10:
        return False
    for i in range(0,4):
        if not text[i].isdecimal():
            return False
        if text[5] != '-':
            return False
    for i in range(6,9):
        if not text[i].isdecimal():
            return False
        
print('95580-7775 is a phone number:')
print(isPhoneNumber('95580-7775'))