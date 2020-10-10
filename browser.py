import os
import sys
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore

stack = deque()
TAG_LIST = ['p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']
folder = sys.argv[1]
try:
    os.mkdir(folder)
except Exception as e:
    print('Error: e')


def add_page(content=''):
    text = ''
    soup = BeautifulSoup(content, 'html.parser')
    for tag in soup.find_all(TAG_LIST):
        if tag.name == 'a':
            print(Fore.BLUE + tag.text)
        else:
            print(Fore.WHITE + tag.text)
        text += tag.text
    with open(os.path.join(pt, file_name), 'w', encoding='utf-8') as _f:
        _f.write(text)
    stack.append(file_name)


def back_button():
    try:
        stack.pop()
        prev_site = stack[-1]
    except IndexError:
        pass
    else:
        with open(os.path.join(pt, prev_site), 'r', encoding='utf-8') as _f:
            print(_f.read())


def check_url():
    if change == 'back':
        back_button()
    elif change + '.txt' in os.listdir(folder):
        with open(os.path.join(pt, change + '.txt'), 'r',
                  encoding='utf-8') as f:
            print(f.read())
    elif '.' in change:
        try:
            if change.startswith('https://'):
                add_page(requests.get(change).content)
            else:
                add_page(requests.get(f'https://{change}').content)
        except Exception as e:
            pass
    else:
        print('Error: Incorrect URL')


while True:
    change = input()
    file_name = f'{change[:change.rfind(".")]}.txt'
    pt = os.path.abspath(folder)
    if change == 'exit':
        break
    check_url()
