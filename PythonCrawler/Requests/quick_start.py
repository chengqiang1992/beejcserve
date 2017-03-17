import requests

# r = requests.get('https://api.github.com/events')
# print(r)
# r1 = requests.post('http://httpbin.org/post', data = {'key':'value'})
# print(r1)
#
# r2 = requests.put('http://httpbin.org/put', data = {'key':'value'})
# print(r2)
# r3 = requests.delete('http://httpbin.org/delete')
# print(r3)
# r4 = requests.head('http://httpbin.org/get')
# print(r4)
# r5 = requests.options('http://httpbin.org/get')
# print(r5)
#
# payload = {'key1': 'value1', 'key2': 'value2'}
# r6 = requests.get('http://httpbin.org/get', params=payload)
# print(r6)
# print(r6.cookies)
# print(r6.headers)
# print(r6.text)
# print(r6.content)
# print(r6.url)
#
# # r7 = requests.get('http://github.com', timeout=0.001)
#
# r8 = requests.get('http://github.com')
# print('-------------------------------')
# print(r8)
# print(r8.content)
# print(r8.url)
# print(r8.status_code)
# print(r8.history)
#
# r9 = requests.get('http://github.com', allow_redirects=False)
# print('-----------------------------')
# print(r9)
# print(r9.content)
# print(r9.url)
# print(r9.status_code)
# print(r9.history)

# r10 = requests.get('https://www.baidu.com/')
# print('----------------------------')
# print(r10.cookies)
# print(r10.cookies['BDORZ'])
# print(r10.cookies['BAIDUID'])
# print(r10.cookies['BDORZ'])
# print(r10.cookies['BD_HOME'])

# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r11 = requests.get(url, cookies=cookies)
# print(r11.text)

# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# print(r.text)

r = requests.get('http://httpbin.org')
print(r.headers)
print(r.headers['Content-Type'])
print(r.headers.get('content-type'))
