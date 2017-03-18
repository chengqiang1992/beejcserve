import requests

s = requests.Session()

# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})
# # both 'x-test' and 'x-test2' are sent
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print(r.text)

# r = s.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
# print(r.text)
#
# r = s.get('http://httpbin.org/cookies')
# print(r.text)
#
# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
print(r.headers)
print(r.request.headers)

