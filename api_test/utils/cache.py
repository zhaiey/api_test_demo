from typing import Any

_cache_data = {}


class CacheHandle:

    @classmethod
    def update_cache(cls, name: str, value: str) -> bool:
        if name not in _cache_data:
            try:
                _cache_data[name] = value
                return True
            except Exception as e:
                raise ValueError('更新缓存失败') from e
        else:
            print("参数已存在，请勿重复添加")

    @classmethod
    def get_cache(cls, name: str) -> Any:
        if name in _cache_data.keys():
            return _cache_data[name]
        raise AttributeError("无该缓存名，请检查缓存名是否正确")

if __name__ == "__main__":
    CacheHandle.update_cache('bili1',15)
    CacheHandle.update_cache('bili1',14)
    print(CacheHandle.get_cache('bili1'))
    print(_cache_data)