'''识别yzm1.jpg内容,转为字符串'''
import pytesseract
# 图片处理标准库
from PIL import Image

# 创建图片对象
img = Image.open('yzm1.jpg')
# 图片内容转字符串
result = pytesseract.image_to_string(img)
print(result)













