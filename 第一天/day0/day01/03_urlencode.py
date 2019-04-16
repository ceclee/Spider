import urllib.request
import urllib.parse

# 定义常用变量
headers = {'User-Agent':''}
baseurl = 'http://www.baidu.com/s?'
key = input('请输入要搜索的内容:')
# 编码,拼接URL地址
wd = urllib.parse.urlencode({'wd':key})
url = baseurl + wd
# 发请求,获响应
# 1.创建请求对象
request = urllib.request.Request(url,headers=headers)
# 2.获取响应对象
response = urllib.request.urlopen(request)
# 3.获取响应内容
html = response.read().decode('utf-8')
# html为一个字符串(超级长)
# 4.保存到本地文件 : 百度.html
with open('百度.html','w',encoding='utf-8') as f:
  f.write(html)













