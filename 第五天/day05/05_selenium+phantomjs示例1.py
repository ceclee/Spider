# 导入webdriver接口
from selenium import webdriver
import time

# 设置无界面模式
options = webdriver.ChromeOptions()
options.set_headless()
# 创建浏览器对象
driver = webdriver.Chrome(options=options)
# 向百度发起请求
driver.get('http://www.baidu.com/')
# 接收终端输入,发送到搜索框
key = input('请输入搜索内容:')
driver.find_element_by_id('kw').send_keys(key)
# 点击　百度一下　按钮
time.sleep(5)
driver.find_element_by_id('su').click()
# 获取屏幕截图
driver.save_screenshot('赵丽颖2.png')
# 关闭浏览器
driver.quit()