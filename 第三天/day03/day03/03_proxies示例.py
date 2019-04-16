import requests

# 测试网址,能显示出口IP
url = 'http://httpbin.org/get'
headers = {'User-Agent' : 'Mozilla/5.0'}
# 定义一个代理
proxies = {
    'http':'http://159.224.13.29:61366',
    'https':'https://159.224.13.29:61366'
  }
# proxies = {
#     'http':'http://309435365:szayclhp@116.255.191.105:16816'
# }

# 发请求
res = requests.get(url,
                   headers=headers,
                   proxies=proxies)
res.encoding = 'utf-8'
html = res.text

print(html)











