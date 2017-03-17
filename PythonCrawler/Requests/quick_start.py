import requests

r = requests.get('https://api.github.com/events')
print(r)
r1 = requests.post('http://httpbin.org/post', data = {'key':'value'})
print(r1)

r2 = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r2)
r3 = requests.delete('http://httpbin.org/delete')
print(r3)
r4 = requests.head('http://httpbin.org/get')
print(r4)
r5 = requests.options('http://httpbin.org/get')
print(r5)

payload = {'key1': 'value1', 'key2': 'value2'}
r6 = requests.get('http://httpbin.org/get', params=payload)
print(r6)
print(r6.cookies)
print(r6.headers)
print(r6.text)
print(r6.content)
print(r6.url)

r7 = requests.get('http://github.com', timeout=0.001)
