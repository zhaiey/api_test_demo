import requests
import pytest
import yaml
import os

# 获取当前脚本的绝对路径
from utils.get_token import mm
current_dir = os.path.dirname(os.path.abspath(__file__)) #当前目录
parent_dir = os.path.dirname(current_dir)#父级目录
yaml_file_path = os.path.join(parent_dir, 'data', 'changhai_denglu.yaml') #获取yaml绝对路径
print(yaml_file_path)
# 加载测试数据

with open(yaml_file_path, 'r') as file:
    test_data = yaml.safe_load(file)
print(test_data['denglu1']['data'])
body = test_data['denglu1']['data']['code'] = mm
print(test_data['denglu1']['data'])
# print(test_data)
