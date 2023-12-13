'''
Дана строка со словами из 5 букв
http://russkiyslovar.ru/iz-5-bukv
Выбрать слова с максимально различающиеся по буквам
'''
# from numba import njit
from copy import deepcopy

cyrillic_lower_letters:str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

with open('Rus_5letters_words.txt','r') as f:
    s = f.read()
lst=s.split()
new_lst:list = []
# 1-Шаг: слова с неповторющимися символами
for s1 in lst:
    l1 = len(s1)
    l2 = len(set(s1))
    if l1==l2:
        new_lst.append(s1)
        print(s1)

print(f' {len(lst)=}')
new_lst_len = len(new_lst)
print(f' {new_lst_len=}')

# 2-Шаг: слова с максимально различающимися буквами
# 1 слово берем из 1 элемента списка

diff_words = [new_lst[0]]
print(diff_words)

def delete_chr_from_str(cyrillic_lower_letters:str,s:str)->str:
    '''
    удаляем из списка кириллических символов (cyrillic_lower_letters) буквы из s
    '''
    sn = deepcopy(cyrillic_lower_letters)
    for s1 in s:
        if s1 in sn:
            # print('delete ',s1)
            cyrillic_lower_letters = cyrillic_lower_letters.replace(s1, '')
    return cyrillic_lower_letters

def all_chr_in_str(cyrillic_lower_letters:str,s:str)->bool:
    '''
    проверяем, что все буквы из списка кириллических символов (cyrillic_lower_letters) есть в s
    '''
    res = [s1 in cyrillic_lower_letters for s1 in s]
    return all(res)

def thetest_all_chr_in_str():
    s = 'вдеть'
    global cyrillic_lower_letters
    print(f'До удаления {cyrillic_lower_letters=}')
    print('До удаления all_chr_in_str = ', all_chr_in_str(cyrillic_lower_letters, s))
    cyrillic_lower_letters=delete_chr_from_str(cyrillic_lower_letters,s)
    print(f'После удаления {cyrillic_lower_letters=}')
    print('После удаления all_chr_in_str = ',all_chr_in_str(cyrillic_lower_letters, s))


def find_different_words(cyrillic_lower_letters, new_lst:list[str]):
    # https://www.cyberforum.ru/python-beginners/thread2695448.html
    s_3:str = ''
    new_lst_len:int = len(new_lst)
    diff_words:list = [new_lst[0]] # вывбираем первое слово (с неповторяющимися буквами)
    cyrillic_lower_letters = delete_chr_from_str(cyrillic_lower_letters, new_lst[0]) # Удаляем буквы первого слова
    print('Big Cycle')
    for i in range(1,new_lst_len): # перебор по всем словам в общем списке
        print(i,' from', new_lst_len)
        if all_chr_in_str(cyrillic_lower_letters,new_lst[i]):
            diff_words.append(new_lst[i])
            res_max = 0 # перебор по всем словам в целевом списке
            cyrillic_lower_letters = delete_chr_from_str(cyrillic_lower_letters,new_lst[i])

    print('len(diff_words)=',len(diff_words))
    print(diff_words)
    print('Отстатки букв = ',cyrillic_lower_letters)

# thetest_all_chr_in_str()

find_different_words(cyrillic_lower_letters, new_lst)
