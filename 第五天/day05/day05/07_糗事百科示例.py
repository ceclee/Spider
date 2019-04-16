from selenium import webdriver


driver = webdriver.PhantomJS()
url = 'https://www.qiushibaike.com/text/'
driver.get(url)

# 单元素查找
ele = driver.find_element_by_class_name('content')
# print(ele.text)

eles = driver.find_elements_by_class_name('content')
for ele in eles:
  print(ele.text)
  print('*' * 40)