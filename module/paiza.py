import time

import requests
# from module import user
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# headless Chrome ブラウザの準備
options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)
browser.implicitly_wait(3)


def input_form(css_selector, val):
    el = browser.find_element_by_css_selector(css_selector)
    el.clear()
    el.send_keys(val)

def get_data(email, password):

    # データを格納する箱
    data = {}

    # ログインページにアクセス
    login_url = 'https://paiza.jp/login'
    browser.get(login_url)

    input_form('#email', email)
    input_form('#password', password)
    form = browser.find_element_by_css_selector('#regist_btn')
    form.submit()
    print('login successful')

    browser.get('https://paiza.jp/career/mypage/results')
    time.sleep(1)
    print('move to my page')

    results = browser.find_elements_by_css_selector('div.basicBox')

    results_num = len(results)
    count = 0
    for result in results:
        title = result.find_element_by_css_selector('a').text.split(':')
        date = result.find_element_by_css_selector('.boxT > .boxTR').text.split('：')
        details = [r.text for r in result.find_elements_by_css_selector('.boxM > div.inrTxt > span')]
        if len(title) >= 2 and len(details) >= 9:
            # data[問題番号] = [タイトル,[ [言語,日時,スコア] ] ]
            data[title[0]] = [title[1],[[details[2],date[1],details[8]]]]

        print('{} / {} finished...'.format(count, results_num))
        count += 1

    # print(data)

    browser.get('https://paiza.jp/career/mypage/retry-results')

    is_viewmore_button = True
    while is_viewmore_button:
        try:
            form = browser.find_element_by_css_selector('#view_more > form > input.ch_button')
            form.submit()
            time.sleep(1)
        except:
            is_viewmore_button = False


    results = browser.find_elements_by_css_selector('#retry_results > div.basicBox')

    results_num = len(results)
    count = 0
    for result in results:
        title = result.find_element_by_css_selector('a').text.split(':')
        date = result.find_element_by_css_selector('.boxT > .boxTR').text.split('：')
        details = [r.text for r in result.find_elements_by_css_selector('.boxM > div.inrTxt > span')]
        if len(title) >= 2 and len(details) >= 6:
            print(details)
            # data[問題番号] = [言語,日時,スコア]
            data[title[0]][1].append([details[1],date[1],details[5]])
        print('{} / {} finished...'.format(count, results_num))
        count += 1

    # print(data)

    path = 'data/data_dict.txt'
    with open(path, mode='w') as f:
        f.write(str(data))

    browser.quit()

    return False