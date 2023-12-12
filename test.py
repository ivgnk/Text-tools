# Разница
# По мотивам
# https://www.cyberforum.ru/python-beginners/thread2695448.html

#---- (1)
def diff_func(a:str, b:str):
    print(f'\nWords = {a} , {b}')
    print( len(set(a) ^ set(b)) )
    print('- - -')
    print(f'{len(set(a) - set(b))=}')
    print(f'{len(set(b) - set(a))=}')
    print( len(set(a) - set(b)) + len(set(b) - set(a)) )

def thetest_diff_func():
    a1 = 'абака'
    a2 = 'слово'
    a3 = 'гамма'
    diff_func(a1,a2)
    diff_func(a2,a3)
    diff_func(a1,a3)
    diff_func(a1,a1)

#---- (2)
def thetest_vhodit():
    cyrillic_lower_letters:str  = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    cyrillic_lower_letters2:str = 'абгеёжзйклмнпрсуфцчшщъыьэюя'
    s = "входит"
    vhodit = True
    for s1 in s:
        if s1 in cyrillic_lower_letters:
            print('Входит!')
        else:
            print('НЕ Входит!')

    for s1 in s:
        if s1 in cyrillic_lower_letters2:
            print('Входит!')
        else:
            print('НЕ Входит!')
