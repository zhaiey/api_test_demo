import json

import ddddocr
import pytest
import requests
import cv2
import numpy as np
from PIL import Image
import ddddocr
url = 'http://192.168.5.47:32000/api/v1/auth/verify-code?random=XFSVhQ'
response = requests.get(url)
if response.status_code == 200:
    # 定义保存图片的文件名
    image_filename = 'downloaded_image.jpg'
    # 将图片内容写入文件
    with open(image_filename, 'wb') as file:
        file.write(response.content)
    # print(f"图片已成功保存到 {image_filename}")
else:
    print(f"请求失败，状态码：{response.status_code}")
# 打开图片
ocr = ddddocr.DdddOcr()
image = Image.open("downloaded_image.jpg")

text = ocr.classification(image)
# print("识别结果：", str(text))
ss = str(text)
ss = ss.split('+')
mm = int(ss[0]) + int(ss[1])
print(mm)
# url = 'http://192.168.5.47:32000/api/v1/auth/login'
# data = '{'+'"mobile":"18221731234","password":"e10adc3949ba59abbe56e057f20f883e","loginType":0,"random":"XFSVhQ","code":{}'.format(mm)+'}'
# headers ={'Content-Type': 'application/json', 'terrace':'HOSPITAL-CALL'}
#
# # def get_code():
# response = requests.post(url , data = data, headers = headers)
# code = response.json()['data']['token']['token']
# print('"'+str(code)+'"')
# print(response.json())
# return code
# if __name__ == "__main__":
#     print(get_code())
