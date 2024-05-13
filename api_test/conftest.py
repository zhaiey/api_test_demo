import os

current_dir = os.path.dirname(os.path.abspath(__file__)) #当前目录
parent_dir = os.path.dirname(current_dir)#父级目录
yaml_file_path = os.path.join(parent_dir, 'data', 'changhai_denglu.yaml') #获取yaml绝对路径
print(yaml_file_path)