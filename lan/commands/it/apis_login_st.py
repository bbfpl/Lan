# coding=utf-8
import unittest2
from lan import Request, Log
from model import Test


class TestUserLogin(Test):
    # 测试登录
    def test_login(self):
        Log.debug('开始测试 test_login')
        self.result = Request.get('http://139.196.192.35:39001/api/login')
        # Log.info(self.result)
        self.assertEqual(1, 1)


if __name__ == '__main__':
    print('开始')
    unittest2.main()