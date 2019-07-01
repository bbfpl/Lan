class Test(object):
    @staticmethod
    def get_discover_cases(discover):
        """
        获取discover里的所以用例 方法名称
        """
        data = []
        for item in discover:
            for i in str(item).split('testMethod='):
                for j in i.split('>'):
                    if 'test_' in j:
                        data.append({
                            'method_name': j,
                            'case': item
                        })
        return data

    @staticmethod
    def get_result_name(item):
        """
        获取方法名
        """
        return str(item[0]).split(' (')[0]

