'''
Дана строка со словами из 5 букв
http://russkiyslovar.ru/iz-5-bukv
Выбрать слова максимально различающиеся по буквам
'''
from numba import njit
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
    sn = deepcopy(cyrillic_lower_letters)
    for s1 in s:
        if s1 in sn:
            # print('delete ',s1)
            cyrillic_lower_letters = cyrillic_lower_letters.replace(s1, '')
    return cyrillic_lower_letters


@njit
def find_different_words(new_lst:list[str]):
    # https://www.cyberforum.ru/python-beginners/thread2695448.html
    s_3:str = ''
    new_lst_len:int = len(new_lst)
    diff_words:set = {new_lst[0]}
    global cyrillic_lower_letters
    print('Big Cycle')
    for i in range(1,new_lst_len):
        print(i,' from', new_lst_len)
        for s_2 in diff_words:
            res_max = 0
            for j in range(i,new_lst_len):
                if
                res = len(set(new_lst[j]) - set(s_2)) + len(set(s_2) - set(new_lst[j]))
                if res > res_max:
                    res_max = res
                    s_3 = new_lst[j]
            diff_words.append(s_3)

            print(diff_words)

    print('len(diff_words)=',len(diff_words))
    print(diff_words)

find_different_words(new_lst)

print(f'{cyrillic_lower_letters=}')
cyrillic_lower_letters=delete_chr_from_str(cyrillic_lower_letters,'вдеть')
print(f'{cyrillic_lower_letters=}')
# print(delete_chr_from_str('вдеть')):