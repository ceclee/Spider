from selenium import webdriver

# 创建浏览器对象
browser = webdriver.PhantomJS()
# 发请求
browser.get('https://mail.qq.com/')
# 切换到子框架
login_frame = browser.find_element_by_id(
                              'login_frame')
browser.switch_to_frame(login_frame)
# 发送用户名和密码
browser.find_element_by_id('u').send_keys('2621470058')
browser.find_element_by_id('p').send_keys('zhanshen001')
# 点击登录按钮
browser.find_element_by_id('login_button').click()
# 屏幕截图
browser.save_screenshot('success.png')





