# coding=utf-8
from tinydb import TinyDB
from utils import root, remove_file


class FileDb:
    """
    Json文件db
    """

    def __init__(self, dir='db', name=''):
        """
        初始化 获取db文件路径
        """
        self.db_path = root() + '/runtime/' + dir + '/' + name + '.json'

    def _db(self):
        """
        TinyDB实例化
        """
        return TinyDB(self.db_path)

    def inster(self, data):
        """
        插入数据
        {'a':1}
        """
        return self._db().insert(data)

    def inster_all(self, data):
        """
        插入多条
        """
        return self._db().insert_multiple(data)

    def select(self):
        """
        查询
        """
        return self._db().all()

    def remove_db(self):
        """
        删除
        """
        remove_file(self.db_path)


if __name__ == '__main__':
    print('测试db')
    FileDb().inster({
        'status': 1,
        'method_name': 2
    })
    # FileDb().remove_db()
