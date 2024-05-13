# import pytest
# from utils.read_case import test_data
# from utils.api_clent import ApiRequest
#
#
class MyClass:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls, arg1):
        return cls.class_variable + " " + arg1

    @staticmethod
    def static_method(arg1):
        return "Static method called with " + arg1

    # 使用类名调用类方法和静态方法




















# @pytest.fixture(scope='class')
# def qianzhi():
#     print("*********************测试开始*********************")
#     yield
#     print("*********************测试结束*********************")
#
# @pytest.mark.usefixtures('qianzhi')
# class TestCase:
#     @pytest.fixture(autouse=True)
#     def first(self):
#         print("\n测试用例开始执行")
#         yield
#         print("测试用例执行结束")
#     # @allure.title('word')
#     def test_nlu(self):
#         # api_request = APIRequest(base_url, headers)
#         ApiRequest.get()
#         print(test_data['denglu1']['endpoint'])
# if __name__ == "__main__":
#     pytest.main(["-s", "run.py"])
