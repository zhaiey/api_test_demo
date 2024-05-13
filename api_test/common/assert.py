import pytest
import enums
from enums import AssertEnum
class AssertType:
    @classmethod
    def equals(cls, expect, actual):
        assert expect == actual

    @classmethod
    def less_than(cls, expect, actual):
        assert expect < actual

    @classmethod
    def less_than_or_equals(cls, expect, actual):
        assert expect <= actual

    @classmethod
    def greater_than(cls, expect, actual):
        assert expect > actual

    @classmethod
    def greater_than_or_equals(cls, expect, actual):
        assert expect >= actual

    @classmethod
    def not_equals(cls, expect, actual):
        assert expect != actual

    @classmethod
    def contains(cls, expect, actual):
        assert expect in actual

class Assert(AssertType):

    @classmethod
    def expect_check(cls,expect, actual, type):
        if type in AssertEnum._value2member_map_:
            function = AssertEnum(type).name
            if hasattr(AssertType, function):
                try:
                    getattr(AssertType, function)(expect, actual)
                    print("断言成功")
                except Exception:
                    raise AssertionError("断言失败")
            else:
                raise ValueError("相关断言函数不存在")
        else:
            raise ValueError("断言类型不存在")
if __name__ == "__main__":
    # Assert.expect_check(1,1,"==")
    # Assert.expect_check(1,2,"==")
    Assert.expect_check('4','1,2,3',"contains")
    # Assert.expect_check(1,2,">")

