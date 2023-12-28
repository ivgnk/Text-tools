'''
A) get/put parameters from json
https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file

B) Scraping
08.05.2021 Скачивание файлов в Python АВТОР В. ДРОНОВ
https://tonais.ru/file/skachivanie-faylov-v-python
'''

import urllib.request
# from pstring import swlz
from configparser import ConfigParser
import sys
ini_fn = 'Scrap2_config_book2.ini'
def get_params_from_json(ini_fn:str)-> (str, str, int, int):
    config = ConfigParser()
    config.read(ini_fn)
    a = config.get('main', 'base_url'); base_url_ = a.strip(); print(f'{base_url_=}')
    a = config.get('main', 'folder');  result_folder_ = a.strip(); print(f'{result_folder_=}')
    a = config.get('main', 'prefix_fn');  prefix_fn_ = a.strip(); print(f'{prefix_fn_=}')

    a = config.get('main', 'first_index');  first_index_ = int(a.strip()); print(f'{first_index_=}')
    a = config.get('main', 'last_index');  last_index_ = int(a.strip()); print(f'{last_index_=}')
    return base_url_, result_folder_, prefix_fn_, first_index_, last_index_

base_url_, folder_, prefix_fn_, first_index_, last_index_    = get_params_from_json(ini_fn)
# https://python-lab.ru/vyhod-i-zavershenie-programmy-v-python
# sys.exit(0)
if first_index_ == 1:
    base_index = 0
else:
    base_index = first_index_-1

total_pages = last_index_ - first_index_ + 1
print(f'{total_pages=}')
for i in range(first_index_, last_index_+1): # 1,285
    print(i,'  ',i-base_index,' from ',total_pages)
    fsn = prefix_fn_+str(i)
    # https://ru.stackoverflow.com/questions/628701/Вывод-числа-с-ведущими-нолями
    fdn = 'page-'+ str(i-base_index).zfill(3)
    curr_url = base_url_+fsn
    res_fn = folder_+fdn+'.webp'
    urllib.request.urlretrieve(curr_url,res_fn)

