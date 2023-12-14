'''
Дана строка со словами из 5 букв / A string with 5 letter words is given
http://russkiyslovar.ru/iz-5-bukv
Выбрать слова максимально различающиеся по буквам / Choose words that differ in letters as much as possible
'''
# Как исправить иероглифы в терминале PyCharm на русские буквы?
# Вряемя и язык -> (справа) админстративные языковые параметры -> галочка в "бета-версия: использовать Юникод..."
# https://qna.habr.com/q/1130386

# from numba import njit
import inspect
from copy import deepcopy

cyrillic_lower_letters:str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' # cyrillic chars

def input_lst(fn:str)->list:
    '''
    ввод списка из файл / input a list from a file
    '''
    print('\n',inspect.currentframe().f_code.co_name)
    with open(fn,'r') as f:
        s = f.read()
    lst=s.split()
    # print(lst)
    new_lst:list = []
    # Выбираем слова с неповторющимися символами / Choosing words with non-repeating characters
    for s1 in lst:
        l1 = len(s1)
        l2 = len(set(s1))
        if l1==l2:
            new_lst.append(s1)
            # print(s1)

    print(f' {len(lst)=}')
    new_lst_len = len(new_lst)
    print(f' {new_lst_len=}')
    return new_lst

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
    print('\n',inspect.currentframe().f_code.co_name)
    # https://www.cyberforum.ru/python-beginners/thread2695448.html
    s_3:str = ''
    new_lst_len:int = len(new_lst)
    print(f'{new_lst_len=}')
    # https://www.geeksforgeeks.org/how-to-create-a-list-of-n-lists-in-python/
    diff_words:list = [[] for x in range(new_lst_len)]
    for i in range(0,new_lst_len): # перебор по всем словам в общем списке
        diff_words[i].append('') # увеличиваем список
        diff_words[i][0] = new_lst[i]
        cyrillic_lower_letters_curr = delete_chr_from_str(cyrillic_lower_letters, new_lst[i]) # Удаляем буквы этого слова
        for j in range(0,new_lst_len): # перебор по всем оставшимся словам в общем списке
            if i != j:
                if all_chr_in_str(cyrillic_lower_letters_curr,new_lst[j]):
                    diff_words[i].append(new_lst[j])
                    cyrillic_lower_letters_curr = delete_chr_from_str(cyrillic_lower_letters_curr,new_lst[j])
        print('len(diff_words[',i,'])=',len(diff_words[i]))
        # print(diff_words[i])
        # print('Остатки букв = ',cyrillic_lower_letters_curr)
    return diff_words

def output_list_of_list_to_file(fn:str, lst:list)->None:
    print('\n',inspect.currentframe().f_code.co_name)
    # print(lst)
    with open(fn,'w') as f:
        for i,s1 in enumerate(lst):
            f.write(f'{i:4} ')
            for s2 in s1:
                f.write(s2+' ')
            f.write('\n')


# ---- Main program
new_lst = input_lst('Rus_5letters_words.txt')
diff_words = find_different_words(cyrillic_lower_letters, new_lst)
output_list_of_list_to_file('different words.txt',diff_words)
