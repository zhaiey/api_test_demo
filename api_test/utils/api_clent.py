# api_request.py
#encoding='utf-8'
import requests
import json
from get_token import mm
import requests
import pytest
import yaml
import os

# 获取当前脚本的绝对路径
from api_test.utils.get_token import mm
current_dir = os.path.dirname(os.path.abspath(__file__)) #当前目录
parent_dir = os.path.dirname(current_dir)#父级目录
yaml_file_path = os.path.join(parent_dir, 'data', 'changhai_denglu.yaml') #获取yaml绝对路径
print(yaml_file_path)
# 加载测试数据

with open(yaml_file_path, 'r') as file:
    test_data = yaml.safe_load(file)
# print(test_data['denglu1']['data'])
body = test_data['denglu1']['data']['code'] = mm
# print(test_data['denglu1']['data'])

class ApiRequest:
    def __init__(self):
        self.code = mm
        self.case_data = test_data
        self.url = 'http://192.168.5.47:32000'
    def get(self, endpoint, parmam, header= None):
        url = f"{self.url}{endpoint}{parmam}"
        response = requests.get(url, header)
        # print(response.status_code)
        return self._handle_response(response)

    def post(self, endpoint, parmam, header=None):
        url = f"{self.url}{endpoint}"
        # print(header)
        response = requests.post(url=url, json=parmam, headers=header)
        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 200:
            try:
                return response.json()
            except json.JSONDecodeError:
                return response.text
        else:
            raise Exception(f"Request failed with status {response.status_code}: {response.text}")

        # 使用示例


if __name__ == "__main__":
    # 假设你的API基础URL是 http://example.com/api/v1/
    print(ApiRequest().get(endpoint='/api/v1/auth/login',parmam= {"mobile":"18221731234","password":"e10adc3949ba59abbe56e057f20f883e","loginType":0,"random":"NXoUty","code":3},header={'Terrace':'HOSPITAL-CALL'}))
