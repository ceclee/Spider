import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1554203225905&di=d9e24a2401105ca0e640582403f058f6&imgtype=0&src=http%3A%2F%2Fdingyue.nosdn.127.net%2FlL1JH2YdpAWrzEhfp8BrJ8lTHa1602AEX9E7qpTpH5NzW1535203788506compressflag.jpg'
headers = {'User-Agent' : 'Mozilla/5.0'}

# 发请求获响应
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
# 获取bytes数据类型
html = res.content

# 写文件
with open('赵丽颖.jpg','wb') as f:
  f.write(html)










