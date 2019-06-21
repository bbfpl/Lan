# 常用工具
import os


def root():
    """
    获取根目录
    """
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


def is_empty(val):
    """
    判断是否为空
    """
    if val == None or val == '' or val == 'null':
        return True
    else:
        return False


def mkdir(path):
    """
    创建目录
    """
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    """
    判断路径是否存在
    存在     True
    不存在   False
    """
    is_exists = os.path.exists(path)

    if not is_exists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        # print(path+' 目录已存在')
        return False


def open_file(path):
    """
    读取文件
    """
    file_object = open(path, 'r', encoding='utf-8')
    try:
        ftext = file_object.read()
    finally:
        file_object.close()

    return ftext


# 写入文件
def write_file(path, code):
    if os.path.exists(path) is False:
        file = open(path, 'w', encoding='utf-8')
        file.write(code)
        file.close()


# 删除文件
def remove_file(path):
    if os.path.exists(path) is True:
        os.remove(path)


if __name__ == '__main__':
    print(root())
