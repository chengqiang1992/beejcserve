# import builtwith
# try:
#     from builtwith import builtwith   # py3
# except:
#     from builtwith import builtwith
#
# builtwith.parse('https://www.sfdai.com/')
# print(builtwith.parse('https://www.sfdai.com/'))

# import whois
# print(whois.whois('appspot.com'))

import urllib
# def download(url):
#     return urllib.urlopen(url).read()
# def download(url, num_retries=2):
#     print('Downloading:', url)
#     try:
#         html = urllib.urlopen(url).read()
#     except urllib.URLError as e:
#         print('Download error:', e.reason)
#         html = None
#         if num_retries > 0:
#             if hasattr(e, 'code') and 500 <= e.code < 600:
#                 # recursively retry 5xx HTTP errors
#                 return download(url, num_retries-1)
#     return html
def download(url, user_agent='wrap', num_retries=2):
    print('Downloading:', url)
    headers = {'User-agent': user_agent}
    request = urllib.Request(url, headers=headers)
    try:
        html = urllib.urlopen(request).read()
    except urllib.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # retry 5xx HTTP errors
                return download(url, user_agent, num_retries-1)
    return html

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # download the sitemap links
    links = re.findall('<loc>(.*?)</loc>', sitemap)
    # download each link
    for link in links
        html = download(link)
        # scrape html here
        # ...