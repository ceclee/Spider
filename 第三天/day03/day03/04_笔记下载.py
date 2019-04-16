import requests
import re
import csv

class NoteSpider(object):
  def __init__(self):
    self.headers = {'User-Agent':'Mozilla/5.0'}
    # 使用普通代理
    self.proxies = {
          'http':'http://111.177.183.54:9999',
          'https':'https://111.177.183.54:9999'
    }
    # web客户端验证参数
    self.auth = ('tarenacode','code_2013')

  # 获取解析页面
  def get_page(self,url):
    # 获取页面
    res = requests.get(url,
                       headers=self.headers,
                       auth=self.auth,
                       proxies=self.proxies)
    res.encoding = 'utf-8'
    html = res.text
    # 解析页面
    p = re.compile('<a href="(.*?)/.*?</a>',re.S)
    r_list = p.findall(html)
    print(r_list)
    # r_list : ['..','AIDCode','','']
    self.write_page(r_list)

  # 保存数据
  def write_page(self,r_list):
    with open('Note.csv','w') as f:
      # 创建写入对象
      writer = csv.writer(f)
      for r in r_list:
        if r != '..':
          writer.writerow([r])

if __name__ == '__main__':
  spider = NoteSpider()
  spider.get_page('http://code.tarena.com.cn/')


# 111.177.183.198:9999


