import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
r.headers['content-type']             # application/json; charset=utf-8
r.encoding                              # utf-8
r.text                                  # {"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}
r.json()                                # {"message":"Bad credentials","documentation_url":"https://developer.github.com/v3"}