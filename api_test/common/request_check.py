
from jsonpath import jsonpath
from urllib.parse import quote
from api_test.config import BaseConfig
# from utils.random.random_data import RandomUtil
# from api_test.utils.file.operation_cache import OperationCache
from api_test.utils.read_cases import LoadCase
class Check:

    @classmethod
    def check(cls, info:dict, data:dict):
        """
        检查请求前相应的数据
        :param data: 用例基本信息
        :param data: 用例数据
        :return:
        """
        info, data = Check.check_url(info, data)
        data = Check.check_headers(data)
        data = Check.check_data(data)
        return info, data



    @classmethod
    def check_url(cls, info:dict, data:dict):
        """
        校验 url 中是否有参数
        :param info: 用例信息
        :param data: 用例数据
        :return:
        """
        url_list = info['url'].split('/')
        for index, value in enumerate(url_list):
            if value.startswith('$'):
                url_list[index] = jsonpath(data, value)[0]
                info['url'] = '/'.join(url_list)
        return info, data

    @classmethod
    def check_headers(cls, data:dict):
        """
        检查headers
        :param data: 用例数据
        :return:
        """
        headers = data['headers']
        if headers == 'null':
            headers = {}
        if headers:
            for k, v in headers.items():
                if v.startswith('$'):
                    if k == 'Authorization':
                        headers[k] = 'Bearer '+jsonpath(data, v)[0]
                    else:
                        headers[k] = jsonpath(data, v)[0]
                elif v.startswith('cache'):
                    headers[k] = CacheHandle.get_cache(BaseConfig.root_dir+v.split('.')[0]+'/'+v.split('.')[1])
        return data



if __name__ == "__main__":
    print(Check.check_url(LoadCase[1]))