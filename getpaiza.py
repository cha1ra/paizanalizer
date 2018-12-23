import requests
from module import user
from bs4 import BeautifulSoup



login_info = {
    'user[email]': user.info('email'),
    'user[password]': user.info('password')
}

login_url = 'https://paiza.jp/user_sessions/new_cbox'

session = requests.Session()
res = session.post(login_url, data=login_info)

print('status_code: ', res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')\



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