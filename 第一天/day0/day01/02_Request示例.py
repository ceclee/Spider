import urllib.request

url = 'http://www.baidu.com/'
headers = {'User-Agent' : 'Mozilla/5.0'}

# 1.创建请求对象(添加headers)
request = urllib.request.Request(url,headers=headers)
# 2.获取响应对象(urlopen)
response = urllib.request.urlopen(request)
# 3.获取内容(read)
html = response.read().decode('utf-8')

# 返回http响应码
print(response.getcode())






