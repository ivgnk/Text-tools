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

def get_params_from_json()-> (str, str):
    config = ConfigParser()
    config.read('Scrap2_config.ini')
    a = config.get('main', 'base_url'); base_url_ = a.strip(); print(f'{base_url_=}')
    a = config.get('main', 'folder');  folder_ = a.strip(); print(f'{folder_=}')
    return base_url_, folder_

base_url_, folder_    = get_params_from_json()
# https://python-lab.ru/vyhod-i-zavershenie-programmy-v-python
# sys.exit(0)
for i in range(1,12): # 1,285
    print(i)
    fsn = 'page-'+str(i)
    # https://ru.stackoverflow.com/questions/628701/Вывод-числа-с-ведущими-нолями
    fdn = 'page-'+ str(i).zfill(3)
    curr_url = base_url_+fsn
    res_fn = folder_+fdn+'.webp'
    urllib.request.urlretrieve(curr_url,res_fn)

