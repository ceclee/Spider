'''向百度发起请求,并获取响应内容'''
import urllib.request

url = 'http://www.baidu.com/'
# 向百度发起请求,得到了响应对象
response = urllib.request.urlopen(url)
# 获取响应对象内容
print(response.read().decode('utf-8'))


# encode() : 字符串->bytes类型
# decode() : bytes->字符串

