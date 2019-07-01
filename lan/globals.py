global _global_dict
_global_dict = {}


# 设置全局变量
def set(key, val):
    _global_dict[key] = val


# 获取全局变量
def get(key):
    try:
        return _global_dict[key]
    except KeyError:
        return ""
