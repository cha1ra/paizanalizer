import requests
from module import user
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(3)

driver.get('https://paiza.jp')




login_info = {
    'utf8': '✓',
    'user[email]': user.info('email'),
    'user[password]': user.info('password'),
    'back': 'en_try/mypage/results'
}

login_url = 'https://paiza.jp'

# session = requests.Session()
# res = session.get(login_url)
# soup = BeautifulSoup(res.text, 'html.parser')
# auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
# # TODO: Selectで書くとどうなる？

# login_info['authenticity_token'] = auth_token
# print('status_code: ', res.status_code)

# login_url = 'https://paiza.jp/user_sessions'

# res = session.post(login_url, data=login_info)

# print('status_code: ', res.status_code)
# # print(res.text)

# login_url = 'https://paiza.jp/career/mypage/results'

# res = session.get(login_url)
# soup = BeautifulSoup(res.text, 'html.parser')

# print('status_code: ', res.status_code)
# print(soup.select('#tab-results > div.mb30'))





# r = requests.get('http://b.hatena.ne.jp/')
# content = r.content
# soup = BeautifulSoup(content, 'html.parser')

# print('-----')
# print(soup.select('div.entrylist-contents-main'))
# print('-----')

# for div in soup.select('div.entrylist-contents-main'):
    
#     # print(div)
#     title = div.h3
#     url = div.a
#     user = div.span
#     user_num = user.getText().split(' ')


'''

https://yukituna.com/1083/
request ... urllib の上位互換的なやつ
r = requests.post("http://httpbin.org/post")

URLにパラメータを渡す
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)

'''