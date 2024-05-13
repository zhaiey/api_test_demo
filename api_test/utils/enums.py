from enum import Enum, unique

@unique
class AssertEnum(Enum):
    equals = "=="
    less_than = "<"
    less_than_or_equals = "<="
    greater_than = ">"
    greater_than_or_equals = ">="
    not_equals = "!="
    contains = "contains"

@unique
class DependsType(Enum):
    RESPONSE = 'response'
    REQUEST = 'request'
    SQLDATA = 'sql_data'
    CACHE = 'cache'

@unique
class CaseEnum(Enum):
    URL = 'url'
    METHOD = 'method'
    IS_RUN = 'is_run'
    TITLE = 'title'
    HEADERS = 'headers'
    COOKIES = 'cookies'
    IS_DEPEND = 'is_depend'
    DEPENDS_DATA = 'depends_data'
    REQUEST_TYPE = 'request_type'
    data = 'data'
    ENCODE = 'encode'

@unique
class RequestTypeEnum(Enum):
    JSON = "json"
    PARAMS = "params"
    FILE = "file"
    DATA = "data"
    EXPORT = "export"
    NONE = "none"

@unique
class RequestMethod(Enum):
    POST = 'post'
    GET = 'get'
    PUT = 'put'
    DELETE = 'delete'

# print(AssertEnum._value2member_map_)