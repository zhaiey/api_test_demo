import pytest
from utils.read_case import test_data
from utils.api_clent import ApiRequest


@pytest.fixture(scope='class')
def qianzhi():
    print("*********************测试开始*********************")
    yield
    print("*********************测试结束*********************")

@pytest.mark.usefixtures('qianzhi')
class TestCase:
    @pytest.fixture(autouse=True)
    def first(self):
        print("\n测试用例开始执行")
        yield
        print("测试用例执行结束")
    # @allure.title('word')
    def test_nlu(self):
        # api_request = APIRequest(base_url, headers)
        ApiRequest.get()
        print(test_data['denglu1']['endpoint'])
if __name__ == "__main__":
    pytest.main(["-s", "run.py"])
