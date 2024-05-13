# content of conftest.py
import os

import pytest
# current_dir = os.path.dirname(os.path.abspath(__file__)) #当前目录
# parent_dir = os.path.dirname(current_dir)#父级目录
# yaml_file_path = os.path.join(parent_dir, 'data') #获取yaml绝对路径
# print(parent_dir)
# print(yaml_file_path)
# conftest.py

import pytest
import yaml
from pathlib import Path

class Load_Cases:

    testcases = {}

    def load_yaml_testcases(filename):
        filepath = Path(__file__).parent.parent/'data'/filename
        with filepath.open('r', encoding='utf-8') as f:
            return yaml.safe_load(f)


    @classmethod
    def load(cls):
        path = Path(__file__).parent.parent.joinpath('data')
        for v,filepath in enumerate(path.glob('*.yaml')):
            cls.testcases[v] = cls.load_yaml_testcases(filepath)
        return cls.testcases

LoadCase = Load_Cases.load()

#
if __name__ == '__main__':
    print(LoadCase)

