global _global_dict
_global_dict = {}


class Globals(object):
    """
    全局变量模块
    """

    @staticmethod
    def set(key, val):
        """
        设置全局变量
        """
        _global_dict[key] = val

    @staticmethod
    def get(key):
        """
        获取全局变量
        """
        try:
            return _global_dict[key]
        except KeyError:
            return ""
