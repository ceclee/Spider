import requests

headers = {'User-Agent':'Mozilla/5.0'}
url = 'http://www.baidu.com/s?'

key = input('请输入要搜索的内容:')
params = {
    'wd' : key,
    'pn' : '10'
  }
# 三步走,自动对params编码,后和基准url进行拼接
res = requests.get(url,params=params,headers=headers)
res.encoding = 'utf-8'
html = res.text

print(html)





