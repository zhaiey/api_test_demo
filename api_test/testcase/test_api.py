# testcase/test_api.py
import json

import pytest
import requests
import yaml
from allure import severity, title, description, step
from utils.read_case import *
# 加载测试数据  
from utils.read_case import *

@pytest.mark.parametrize("testcases", test_data)
def test_api(testcase):
    @step("Send request to {endpoint} with {method}")
    def send_request_step():
        url = f"http://example.com/api/v1/{testcase['endpoint']}"
        print(url)
        headers = {
            'Content-Type': 'application/json',
            # 可以添加其他默认headers
        }
        headers.update(testcase.get('headers', {}))  # 合并自定义headers
        response = requests.request(testcase[0]['method'], url, headers=headers, data=testcase.get('data'))
        return response

    @step("Check response status code")
    def check_status_code_step(response):
        assert response.status_code == testcase[
            'expected_status_code'], f"Expected status code {testcase['expected_status_code']} but got {response.status_code}"

    @step("Check response content")
    def check_response_content_step(response):
        expected_response = testcase.get('expected_response', {})
        for key, value in expected_response.items():
            assert key in response.json(), f"Key '{key}' not found in response"
            assert response.json()[key] == value, f"Value mismatch for key '{key}'"

    response = send_request_step()
    check_status_code_step(response)
    check_response_content_step(response)

        # 如果需要，还可以添加其他验证步骤