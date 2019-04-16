from YDM import *

# 1、写程序,把验证码图片保存到本地
# 2、调用在线打码平台,获取识别结果字符串
cid, result = yundama.decode(filename, codetype, timeout)
print(result)


